<script setup lang="ts">
import { ref, watch } from 'vue'
import githubInfo from './githubInfo.vue'
import Project from './Project.vue'
import StickyTitle from './StickyTitle.vue'
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
    <!-- <StickyTitle title="Projects" /> -->
    <h2 id="title">Projects</h2>
    <div class="githubInfoContainer">
      <Suspense>
        <githubInfo :id="projectActive" />
      </Suspense>
    </div>
    <div class="projects">
      <Project
        title="Social Media"
        description="A feature-rich web app that allows users to create accounts, post content, and interact with others through likes and comments. Built with a focus on user experience and scalability."
        :technologies="[
          'Vue',
          'Django',
          'Django REST Framework',
          'Docker',
          'PostgreSQL',
          'Redis',
          'WebSockets',
          'Nginx'
        ]"
        link="https://github.com/jakeyjakeyy/social"
        path="social"
        @click="toggleActive('social')"
        tabindex="0"
        @keypress="handleKeyPress"
      />
      <Project
        title="Password Manager"
        description="'The Vault' is a password manager that enables users to securely store, generate, and manage their passwords. Built following the NIST's Guideline for Using Cryptographic Standards in the Federal Government."
        :technologies="[
          'Vue',
          'Typescript',
          'Django',
          'Django REST Framework',
          'Docker',
          'PostgreSQL',
          'Web Crypto API'
        ]"
        link="https://github.com/jakeyjakeyy/password_manager"
        path="vault"
        @click="toggleActive('password_manager')"
        tabindex="0"
        @keypress="handleKeyPress"
      />
      <Project
        title="City Trip Planner"
        description="A web app that helps users plan city trips by discovering upcoming live events, nearby restaurants, and attractions. It uses OpenAI to generate personalized itineraries based on user preferences, and displays each option on an interactive map."
        :technologies="[
          'React',
          'Django',
          'Docker',
          'PostgreSQL',
          'Google Maps',
          'Google Places',
          'OpenAI API',
          'SeatGeek',
          'Ticketmaster'
        ]"
        link="https://github.com/jakeyjakeyy/cityplanner"
        @click="toggleActive('cityplanner')"
        id="cityplanner"
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
  margin-bottom: 1rem;
}

@media (max-width: 1200px) {
  .projects {
    flex-direction: row;
    justify-content: start;
    max-width: 100vw;
    overflow-x: scroll;
  }
}
@media (max-width: 768px) {
  .projects {
    padding-left: 2vw;
    scroll-snap-type: x mandatory;
  }
}
</style>
