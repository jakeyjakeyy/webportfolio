<script setup lang="ts">
import { ref, onMounted } from 'vue'
import githubInfo from './githubInfo.vue'
import Project from './Project.vue'
import dfchronicles from '../../public/dfchronicles.png'
let projectElements: NodeListOf<Element>

const projectActive = ref('')

onMounted(() => {
  projectElements = document.querySelectorAll('.project')
  projectElements.forEach((element) => {
    element.addEventListener('click', () => {
      if (element.classList.contains('active')) {
        element.classList.remove('active')
        projectActive.value = ''
      } else {
        projectElements.forEach((element) => {
          element.classList.remove('active')
        })
        projectActive.value = element.id
        element.classList.toggle('active')
      }
    })
  })
})
</script>

<template>
  <div id="projectContainer">
    <h3>Projects</h3>
    <div class="githubInfoContainer">
      <Suspense>
        <githubInfo v-if="projectActive == ''" id="'none'" />
        <githubInfo v-else :id="projectActive" />
      </Suspense>
    </div>
    <div class="projects">
      <Project
        title="Dwarf Fortress Chronicles"
        description="A web app that allows users to view, create,  and share stories from the game Dwarf Fortress, while communicating with the OpenAI API to generate content for the user's game data."
        :technologies="['React', 'Django', 'PostgreSQL', 'Docker', 'OpenAI API']"
        link="https://www.github.com/jakeyjakeyy/dfchronicles"
        id="dfchronicles"
      />
      <Project
        title="City Trip Planner"
        description="A web app that allows users to create an itinerary from a custom generated list of locations to visit based on their interests."
        :technologies="[
          'React',
          'Django',
          'PostgreSQL',
          'Docker',
          'Google Maps API',
          'Google Places API',
          'OpenAI API',
          'SeatGeek API',
          'Ticketmaster API'
        ]"
        link="https://github.com/jakeyjakeyy/cityplanner"
        id="cityplanner"
      />

      <Project />
    </div>
  </div>
</template>

<style scoped>
#projectContainer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
  background: var(--color-background);
  padding: 0 2rem 0;
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

@media (max-width: 1200px) {
  .projects {
    flex-direction: row;
    justify-content: space-evenly;
  }
}
</style>
