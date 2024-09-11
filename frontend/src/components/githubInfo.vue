<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import PieChart from './PieChart.vue'

const backendUrl = import.meta.env.VITE_BACKEND_URL

const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

const githubInfoData = ref(
  await fetch(`${backendUrl}/api/githubinfo/public`).then((res) => res.json())
)
const chartData = ref({
  labels: Object.keys(githubInfoData.value.languagePercentages),
  datasets: [
    {
      data: Object.values(githubInfoData.value.languagePercentages)
    }
  ]
})

const currentTime = new Date()
let lastActive: Date | null = new Date(githubInfoData.value.lastActive)
const timeDifference = currentTime.getTime() - lastActive.getTime()
const lastActiveRef = ref<HTMLElement | null>(null)
const pieChartRef = ref<HTMLElement | null>(null)

const formatTimeDifference = (ms: number) => {
  const seconds = Math.floor(ms / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)
  const days = Math.floor(hours / 24)

  if (days > 0) return `${days} days ago`
  if (hours > 0) return `${hours} hours ago`
  if (minutes > 0) return `${minutes} minutes ago`
  return `${seconds} seconds ago`
}

const timeDifferenceFormatted = computed(() => formatTimeDifference(timeDifference))

watch(
  // watch id for changes and update data
  () => props.id,
  async () => {
    if (props.id) {
      toggleActiveAnimation('hide')
      // get repo info
      githubInfoData.value = await fetch(`${backendUrl}/api/githubinfo/${props.id}`).then((res) =>
        res.json()
      )
      chartData.value = {
        labels: Object.keys(githubInfoData.value.languagePercentages),
        datasets: [
          {
            data: Object.values(githubInfoData.value.languagePercentages)
          }
        ]
      }
      if (!githubInfoData.value.lastActive) {
        lastActive = null
      } else {
        lastActive = new Date(githubInfoData.value.lastActive)
      }
    } else {
      toggleActiveAnimation('show')
      // If no repo id is provided, get all public repo info combined
      githubInfoData.value = await fetch(`${backendUrl}/api/githubinfo/public`).then((res) =>
        res.json()
      )
      chartData.value = {
        labels: Object.keys(githubInfoData.value.languagePercentages),
        datasets: [
          {
            data: Object.values(githubInfoData.value.languagePercentages)
          }
        ]
      }
      lastActive = new Date(githubInfoData.value.lastActive)
    }
  }
)

// Animation toggler for piechart and lastActive
const toggleActiveAnimation = (visibility: String) => {
  if (lastActiveRef.value !== null && pieChartRef.value !== null) {
    if (visibility === 'show') {
      lastActiveRef.value.classList.remove('animateOut')
      lastActiveRef.value.classList.add('animateIn')
      pieChartRef.value.classList.add('slideLeft')
      pieChartRef.value.classList.remove('slideRight')
    } else {
      lastActiveRef.value.classList.add('animateOut')
      lastActiveRef.value.classList.remove('animateIn')
      pieChartRef.value.classList.add('slideRight')
      pieChartRef.value.classList.remove('slideLeft')
    }
  }
}
</script>

<template>
  <div class="githubInfo">
    <div class="languages" ref="pieChartRef">
      <PieChart :data="chartData" :size="200" />
    </div>
    <div class="lastActive" ref="lastActiveRef">
      <h4>Last Commit</h4>
      <p>{{ timeDifferenceFormatted }}</p>
    </div>
  </div>
</template>

<style scoped>
.githubInfo {
  display: flex;
  flex-direction: row;
  padding: 1rem;
}

.lastActive {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.animateIn {
  animation: animateIn 0.75s;
}

.animateOut {
  animation: animateOut 0.75s forwards;
}

@keyframes animateIn {
  from {
    opacity: 0;
    transform: translateX(100%);
  }
  to {
    opacity: 1;
  }
}

@keyframes animateOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translateX(100%);
  }
}

.slideRight {
  animation: slideRight 0.75s forwards;
}

.slideLeft {
  animation: slideLeft 0.75s;
}

@keyframes slideRight {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(35%);
  }
}

@keyframes slideLeft {
  from {
    transform: translateX(35%);
  }
  to {
    transform: translateX(0);
  }
}

@media (max-width: 768px) {
  .githubInfo {
    flex-direction: column;
  }
  .lastActive {
    margin-top: 1rem;
  }
  .slideRight {
    animation: slideDown 0.75s forwards;
  }
  .slideLeft {
    animation: slideUp 0.75s forwards;
  }
}

@keyframes slideDown {
  from {
    transform: translateY(0%);
  }
  to {
    transform: translateY(25%);
  }
}

@keyframes slideUp {
  from {
    transform: translateY(25%);
  }
  to {
    transform: translateY(0%);
  }
}
</style>
