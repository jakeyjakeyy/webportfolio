<!--  data = { "JavaScript": 64.38, "Python": 20.88, "CSS": 13.7, "HTML": 0.63, "Dockerfile": 0.4 } -->
<script setup lang="ts">
import { Chart as ChartJS, ArcElement, Tooltip, Legend, Colors } from 'chart.js'
import { Pie } from 'vue-chartjs'
ChartJS.register(ArcElement, Tooltip, Legend, Colors)

defineProps({
    data: Object
})
</script>

<template>
    <div class="pieChart">
        <Pie id="githubInfoPie" :data="data" />
    </div>
</template>