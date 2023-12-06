<script setup lang="ts">
import { ref, computed } from 'vue'
import githubInfo from '../utils/githubInfo'
import PieChart from './PieChart.vue'

const githubInfoData = ref(await githubInfo('jakeyjakeyy'))
const chartData: Object = {
  labels: Object.keys(githubInfoData.value.languagePercentages),
  datasets: [
    {
      data: Object.values(githubInfoData.value.languagePercentages)
    }
  ]
}

const currentTime = new Date()
const lastActive = new Date(githubInfoData.value.lastActive)
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
</script>

<template>
  <div class="githubInfo">
    <div class="languages">
      <PieChart :data="chartData" />
    </div>
    <div class="lastActive">
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

.lastActive {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}
</style>
