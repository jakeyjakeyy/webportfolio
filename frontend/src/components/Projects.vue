<script setup lang="ts">
import { ref, watch } from 'vue'
import githubInfo from './githubInfo.vue'
import Project from './Project.vue'
import dfchronicles from '../../public/dfchronicles.png'
let projectElements: NodeListOf<Element>

const projectActive = ref('')
watch(projectActive, (newValue) => {
  projectElements = document.querySelectorAll('.project')
  projectElements.forEach((element) => {
    if (element.classList.contains('active')) {
      element.classList.remove('active')
    }
  })
  if (newValue === '') return
  let activeElement = document.getElementById(newValue)
  activeElement?.classList.add('active')
})

const toggleActive = (id: string) => {
  if (projectActive.value === id) {
    projectActive.value = ''
  } else {
    projectActive.value = id
  }
}

const handleKeyPress = (event: KeyboardEvent) => {
  if (event.key === 'Enter') {
    toggleActive((event.target as HTMLElement)?.id)
  }
}
</script>

<template>
  <div id="projectContainer">
    <h3>Projects</h3>
    <div class="githubInfoContainer">
      <Suspense>
        <githubInfo :id="projectActive" />
      </Suspense>
    </div>
    <div class="projects">
      <Project
        title="Web Portfolio"
        description="This website! A web app that allows users to view my projects, information, and contact me."
        :technologies="[
          'Vue',
          'Vite',
          'Typescript',
          'Docker',
          'PostgreSQL',
          'Caching',
          'DigitalOcean Droplet'
        ]"
        link="https://github.com/jakeyjakeyy/webportfolio"
        @click="toggleActive('webportfolio')"
        id="webportfolio"
        tabindex="0"
        @keypress="handleKeyPress"
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
        @click="toggleActive('cityplanner')"
        id="cityplanner"
        tabindex="0"
        @keypress="handleKeyPress"
      />
      <Project
        title="Dwarf Fortress Chronicles"
        description="A web app that allows users to view, create,  and share stories from the game Dwarf Fortress, while communicating with the OpenAI API to generate content for the user's game data."
        :technologies="['React', 'Django', 'PostgreSQL', 'Docker', 'OpenAI API']"
        link="https://www.github.com/jakeyjakeyy/dfchronicles"
        @click="toggleActive('dfchronicles')"
        id="dfchronicles"
        tabindex="0"
        @keypress="handleKeyPress"
      />
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
