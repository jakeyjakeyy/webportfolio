<script setup lang="ts">
import { ref, watch } from 'vue'
let contentSelection = ref('home')
let homeElement: HTMLElement | null = null
let aboutElement: HTMLElement | null = null
let projectElement: HTMLElement | null = null
let arrowUpElement: HTMLElement | null = null
let arrowDownElement: HTMLElement | null = null
let autoMotion: Boolean = false
let timeoutId: number | null = null

const up = () => {
  if (contentSelection.value === 'about') {
    autoMotion = true
    homeElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'home'
  } else if (contentSelection.value === 'projects') {
    autoMotion = true
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'about'
  }
  // Prevents the icons from bugging out when scrolling too fast
  if (timeoutId) clearTimeout(timeoutId)
  timeoutId = setTimeout(() => {
    autoMotion = false
  }, 500)
}
const down = () => {
  if (contentSelection.value === 'home') {
    autoMotion = true
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'about'
  } else if (contentSelection.value === 'about') {
    autoMotion = true
    projectElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'projects'
  }
  // Prevents the icons from bugging out when scrolling too fast
  if (timeoutId) clearTimeout(timeoutId)
  timeoutId = setTimeout(() => {
    autoMotion = false
  }, 500)
}

onscroll = () => {
  if (homeElement && aboutElement && projectElement && !autoMotion) {
    const homeRect = homeElement.getBoundingClientRect()
    const aboutRect = aboutElement.getBoundingClientRect()
    const projectRect = projectElement.getBoundingClientRect()
    if (homeRect.top === 0 || homeRect.bottom >= window.innerHeight / 2) {
      contentSelection.value = 'home'
    } else if (aboutRect.top === 0 || aboutRect.bottom >= window.innerHeight / 2) {
      contentSelection.value = 'about'
    } else if (projectRect.top === 0 || projectRect.bottom >= window.innerHeight / 2) {
      contentSelection.value = 'projects'
    }
  }

  onkeydown = (e: KeyboardEvent) => {
    e.preventDefault()
    if (e.key === 'ArrowUp') {
      up()
    } else if (e.key === 'ArrowDown') {
      down()
    }
  }
}

onload = () => {
  homeElement = document.getElementById('homeContainer')
  aboutElement = document.getElementById('aboutContainer')
  projectElement = document.getElementById('projectContainer')
  arrowUpElement = document.getElementById('arrowUp')
  arrowDownElement = document.getElementById('arrowDown')
}

watch(contentSelection, () => {
  if (contentSelection.value === 'home') {
  } else if (contentSelection.value === 'about') {
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
  } else if (contentSelection.value === 'projects') {
    projectElement?.scrollIntoView({ behavior: 'smooth' })
  }
})
</script>

<template>
  <div class="navContainer">
    <div v-if="contentSelection !== 'home'" id="arrowUp">
      <v-icon name="bi-arrow-up-circle" scale="2" @click="up" />
    </div>
    <div v-if="contentSelection !== 'projects'" id="arrowDown">
      <v-icon name="bi-arrow-down-circle" scale="2" @click="down" />
    </div>
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
