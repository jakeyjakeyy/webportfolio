<!--  data = { "JavaScript": 64.38, "Python": 20.88, "CSS": 13.7, "HTML": 0.63, "Dockerfile": 0.4 } -->
<script setup lang="ts">
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'
import { ref } from 'vue';
import githubInfo from '../utils/githubInfo';
const githubInfoData = ref(await githubInfo("jakeyjakeyy"));

ChartJS.register(ArcElement, Tooltip, Legend)
const chartData = {
    labels: Object.keys(githubInfoData.value.languagePercentages),
    datasets: [{
        data: Object.values(githubInfoData.value.languagePercentages),
        backgroundColor: [
            '#FF6384',
            '#36A2EB',
            '#FFCE56',
            '#FFCE56',
            '#AACE56'
        ]
    }],
}
console.log(chartData);

</script>

<template>
    <div class="pieChart">
        <Pie :data="chartData" />
    </div>
</template>