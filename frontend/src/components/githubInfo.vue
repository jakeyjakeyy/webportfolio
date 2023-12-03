<script setup lang="ts">
import {ref} from 'vue';
import PieChart from './PieChart.vue';
import githubInfo from '../utils/githubInfo';

const githubInfoData = ref(await githubInfo("jakeyjakeyy"));


</script>

<template>
    <div class="githubInfo">
        <div class="lastActive">
            <h2>Last Active</h2>
            <p>{{ githubInfoData.lastActive }}</p>
        </div>
        <div class="languages">
            <h2>Languages</h2>
            <Suspense>
                <PieChart />
            </Suspense>
        </div>
    </div>
</template>

<style scoped>

.githubInfo {
    border: 1px solid var(--color-background-soft);
    padding: 1rem;
}

</style>