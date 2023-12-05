<script setup lang="ts">
import {ref} from 'vue';
import githubInfo from './githubInfo.vue';
import Project from './Project.vue';
import dfchronicles from '../../public/dfchronicles.png';

</script>

<template>
    <div class="projectContainer">
        <h3>Projects</h3>
        <div class="githubInfoContainer">
            <Suspense>
                <githubInfo />
            </Suspense>
        </div>
        <div class="projects">
            <Project 
            title="Dwarf Fortress Chronicles"
            description="A web app that allows users to view, create,  and share stories from the game Dwarf Fortress, while communicating with the OpenAI API to generate content for the user's game data."
            link="https://www.github.com/jakeyjakeyy/dfchronicles"
            />
            <Project />
            <Project />
        </div>
    </div>
</template>

<style scoped>

.projectContainer {
    display: flex;
    flex-direction: column;
    width: 100%;
    min-height: 100vh;
}

.githubInfoContainer {
    display: flex;
    justify-content: center;
    padding: 1rem;
}

.projects {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    min-height: fit-content;
}



</style>