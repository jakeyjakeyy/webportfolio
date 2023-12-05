<script setup lang="ts">
let contentSelection: String = 'home'
let homeElement: HTMLElement | null = null
let aboutElement: HTMLElement | null = null
let projectElement: HTMLElement | null = null
const up = () => {
  if (contentSelection === 'about') {
    homeElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection = 'home'
  } else if (contentSelection === 'projects') {
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection = 'about'
  }
}
const down = () => {
  if (contentSelection === 'home') {
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection = 'about'
  } else if (contentSelection === 'about') {
    projectElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection = 'projects'
  }
}

onscroll = () => {
  if (homeElement && aboutElement && projectElement) {
    const bottom = window.innerHeight
    const homeRect = homeElement.getBoundingClientRect()
    const aboutRect = aboutElement.getBoundingClientRect()
    const projectRect = projectElement.getBoundingClientRect()
    if (homeRect.top === 0 || homeRect.bottom >= window.innerHeight / 2) {
      console.log('home')
      contentSelection = 'home'
    } else if (aboutRect.top === 0 || aboutRect.bottom >= window.innerHeight / 2) {
      console.log('about')
      contentSelection = 'about'
    } else if (projectRect.top === 0 || projectRect.bottom >= window.innerHeight / 2) {
      console.log('projects')
      contentSelection = 'projects'
    }
  }
}

onload = () => {
  homeElement = document.getElementById('homeContainer')
  aboutElement = document.getElementById('aboutContainer')
  projectElement = document.getElementById('projectContainer')
}
</script>

<template>
  <div class="navContainer">
    <v-icon name="bi-arrow-up-circle" scale="2" @click="up" />
    <v-icon name="bi-arrow-down-circle" scale="2" @click="down" />
  </div>
</template>

<style scoped>
.navContainer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  right: 0;
  height: 100vh;
  padding: 1rem;
  z-index: 100;
}
</style>
