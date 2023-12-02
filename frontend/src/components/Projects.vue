<script setup lang="ts">
import {ref} from 'vue';
import githubInfo from '../utils/githubInfo';

const githubInfoData = ref(await githubInfo("jakeyjakeyy"));
console.log(githubInfoData);

</script>

<template>
    <div class="projects">
        <h1>Projects</h1>
        <div class="project">
            <h2>Project 1</h2>
            <p>Project 1 description</p>
        </div>
        <div class="githubInfo">
            <div class="lastActive">
                <h2>Last Active</h2>
                <p>{{ githubInfoData.lastActive }}</p>
            </div>
            <div class="languages">
                <h2>Languages</h2>
                <p>{{ githubInfoData.languagePercentages }}</p>
            </div>
        </div>
    </div>
</template>