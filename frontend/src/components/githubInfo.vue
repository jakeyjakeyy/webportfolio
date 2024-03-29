<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import PieChart from './PieChart.vue'

const backendUrl = 'https://jakerichards.info'
// const backendUrl = 'http://localhost:8000'
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
  () => props.id,
  async () => {
    if (props.id) {
      console.log(props.id)
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
      console.log('no id')
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
</script>

<template>
  <div class="githubInfo">
    <div class="languages">
      <PieChart :data="chartData" :size="200" />
    </div>
    <div v-if="lastActive" class="lastActive">
      <h4>Last Active</h4>
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

@media (max-width: 768px) {
  .githubInfo {
    flex-direction: column;
  }
  .lastActive {
    margin-top: 1rem;
  }
}

.lastActive {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}
</style>
