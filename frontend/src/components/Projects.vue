<script setup lang="ts">
import {ref} from 'vue';
import githubInfo from './githubInfo.vue';

</script>

<template>
    <div class="projectContainer">
        <h1>Projects</h1>
        <div class="githubInfoContainer">
            <Suspense>
                <githubInfo />
            </Suspense>
        </div>
        <div class="projects">
            <div class="project">
                <h2>Dwarf Fortress Chronicles</h2>
                <p>A webapp that takes a user's game data as input, parses that data, and generates stories by making requests to the OpenAI API</p>
            </div>
        </div>
    </div>
</template>

<style scoped>

.projectContainer {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.githubInfoContainer {
    display: flex;
    justify-content: center;
    padding: 1rem;
}

.projects {
    display: flex;
    flex-direction: column;
}

.project {
    min-height: 30rem;
    border: 1px solid var(--color-background-soft);
}

</style>