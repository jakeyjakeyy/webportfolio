<script setup lang="ts">
import { ref } from 'vue'
let contentSelection = ref('home')
let homeElement: HTMLElement | null = null
let aboutElement: HTMLElement | null = null
let projectElement: HTMLElement | null = null
let arrowUpElement: HTMLElement | null = null
let arrowDownElement: HTMLElement | null = null

const up = () => {
  if (contentSelection.value === 'about') {
    homeElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'home'
  } else if (contentSelection.value === 'projects') {
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'about'
  }
}
const down = () => {
  if (contentSelection.value === 'home') {
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'about'
  } else if (contentSelection.value === 'about') {
    projectElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'projects'
  }
}

onscroll = () => {
  if (homeElement && aboutElement && projectElement) {
    const homeRect = homeElement.getBoundingClientRect()
    const aboutRect = aboutElement.getBoundingClientRect()
    const projectRect = projectElement.getBoundingClientRect()
    if (homeRect.top === 0 || homeRect.bottom >= window.innerHeight / 2) {
      contentSelection.value = 'home'
      arrowUpElement?.classList.remove('arrowUpAppear')
      arrowUpElement?.classList.remove('arrowUpFromCenter')
      arrowUpElement?.classList.add('arrowUpDisappear')
      arrowDownElement?.classList.remove('arrowDownFromCenter')
      arrowDownElement?.classList.add('arrowDownCentered')
    } else if (aboutRect.top === 0 || aboutRect.bottom >= window.innerHeight / 2) {
      contentSelection.value = 'about'
      if (arrowUpElement?.classList.contains('arrowUpDisappear')) {
        arrowUpElement?.classList.remove('arrowUpDisappear')
        arrowUpElement?.classList.add('arrowUpAppear')
      } else if (arrowUpElement?.classList.contains('arrowUpCentered')) {
        arrowUpElement?.classList.remove('arrowUpCentered')
        arrowUpElement?.classList.add('arrowUpFromCenter')
      }
      if (arrowDownElement?.classList.contains('arrowDownCentered')) {
        arrowDownElement?.classList.remove('arrowDownCentered')
        arrowDownElement?.classList.add('arrowDownFromCenter')
      } else if (arrowDownElement?.classList.contains('arrowDownDisappear')) {
        arrowDownElement?.classList.remove('arrowDownDisappear')
        arrowDownElement?.classList.add('arrowDownAppear')
      }
    } else if (projectRect.top === 0 || projectRect.bottom >= window.innerHeight / 2) {
      contentSelection.value = 'projects'
      arrowUpElement?.classList.remove('arrowUpAppear')
      arrowUpElement?.classList.add('arrowUpCentered')
      arrowDownElement?.classList.remove('arrowDownFromCenter')
      arrowDownElement?.classList.add('arrowDownDisappear')
    }
  }

  onkeydown = (e: KeyboardEvent) => {
    if (e.key === 'ArrowUp') {
      e.preventDefault()
      up()
    } else if (e.key === 'ArrowDown') {
      e.preventDefault()
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
  arrowDownElement?.classList.remove('arrowDownAppear')
  arrowDownElement?.classList.add('arrowDownCentered')
}
</script>

<template>
  <div class="navContainer">
    <div id="arrowUp" class="arrowUpDisappear">
      <v-icon name="bi-arrow-up-circle" scale="2" @click="up" />
    </div>
    <div id="arrowDown" class="arrowDownAppear">
      <v-icon name="bi-arrow-down-circle" scale="2" @click="down" />
    </div>
  </div>
</template>

<style scoped>
@keyframes arrowUpAppear {
  0% {
    opacity: 0;
    transform: translateY(-100px);
  }
  100% {
    opacity: 1;
    transform: translateY(-25px);
  }
}
@keyframes arrowDownAppear {
  0% {
    opacity: 0;
    transform: translateY(100px);
  }
  100% {
    opacity: 1;
    transform: translateY(25px);
  }
}

@keyframes arrowUpDisappear {
  0% {
    opacity: 1;
    transform: translateY(-25px);
  }
  100% {
    opacity: 0;
    transform: translateY(-100px);
  }
}

@keyframes arrowDownDisappear {
  0% {
    opacity: 1;
    transform: translateY(25px);
  }
  100% {
    opacity: 0;
    transform: translateY(100px);
  }
}

@keyframes arrowUpCentered {
  0% {
    transform: translateY(-25px);
  }
  100% {
    transform: translateY(0px);
  }
}

@keyframes arrowDownCentered {
  0% {
    transform: translateY(25px);
  }
  100% {
    transform: translateY(0px);
  }
}

@keyframes arrowUpFromCenter {
  0% {
    transform: translateY(0px);
  }
  100% {
    transform: translateY(-25px);
  }
}

@keyframes arrowDownFromCenter {
  0% {
    transform: translateY(0px);
  }
  100% {
    transform: translateY(25px);
  }
}

.arrowUpAppear {
  animation: arrowUpAppear 0.5s ease-in-out forwards;
}

.arrowUpDisappear {
  animation: arrowUpDisappear 0.5s ease-in-out forwards;
}

.arrowUpCentered {
  animation: arrowUpCentered 0.5s ease-in-out forwards;
}

.arrowUpFromCenter {
  animation: arrowUpFromCenter 0.5s ease-in-out forwards;
}

.arrowDownAppear {
  animation: arrowDownAppear 0.5s ease-in-out forwards;
}

.arrowDownCentered {
  animation: arrowDownCentered 0.5s ease-in-out forwards;
}

.arrowDownFromCenter {
  animation: arrowDownFromCenter 0.5s ease-in-out forwards;
}

.arrowDownDisappear {
  animation: arrowDownDisappear 0.5s ease-in-out forwards;
}

.navContainer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  right: 0;
  height: 100vh;
  width: 60px;
  z-index: 100;
  color: var(--text);
}
.hidden {
  opacity: 0;
}

#arrowUp,
#arrowDown {
  cursor: pointer;
  position: absolute;
}
</style>
