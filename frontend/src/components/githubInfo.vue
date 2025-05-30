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

const pieChartRef = ref<HTMLElement | null>(null)

watch(
  // watch id for changes and update data
  () => props.id,
  async () => {
    if (props.id) {
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
    } else {
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
    }
  }
)

// Animation toggler for piechart
const toggleActiveAnimation = (visibility: String) => {
  if (pieChartRef.value !== null) {
    if (visibility === 'show') {
      pieChartRef.value.classList.add('slideLeft')
      pieChartRef.value.classList.remove('slideRight')
    } else {
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
  </div>
</template>

<style scoped>
.githubInfo {
  display: flex;
  flex-direction: row;
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
