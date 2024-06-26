<script setup lang="ts">
import { ref } from 'vue'
import ThemeSelector from './ThemeSelector.vue'
let contentSelection = ref('home')
let homeElement: HTMLElement | null = null
let aboutElement: HTMLElement | null = null
let projectElement: HTMLElement | null = null
let resumeElement: HTMLElement | null = null
let arrowUpElement: HTMLElement | null = null
let arrowDownElement: HTMLElement | null = null

const up = () => {
  if (contentSelection.value === 'about') {
    homeElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'home'
  } else if (contentSelection.value === 'projects') {
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'about'
  } else if (contentSelection.value === 'resume') {
    projectElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'projects'
  }
}
const down = () => {
  if (contentSelection.value === 'home') {
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'about'
  } else if (contentSelection.value === 'about') {
    projectElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'projects'
  } else if (contentSelection.value === 'projects') {
    resumeElement?.scrollIntoView({ behavior: 'smooth' })
    contentSelection.value = 'resume'
  }
}

const teleport = (location: String) => {
  if (location === 'home') {
    homeElement?.scrollIntoView({ behavior: 'smooth' })
  } else if (location === 'about') {
    aboutElement?.scrollIntoView({ behavior: 'smooth' })
  } else if (location === 'projects') {
    projectElement?.scrollIntoView({ behavior: 'smooth' })
  } else if (location === 'resume') {
    resumeElement?.scrollIntoView({ behavior: 'smooth' })
  }
}

onscroll = () => {
  if (homeElement && aboutElement && projectElement && resumeElement) {
    const homeRect = homeElement.getBoundingClientRect()
    const aboutRect = aboutElement.getBoundingClientRect()
    const projectRect = projectElement.getBoundingClientRect()
    const resumeRect = resumeElement.getBoundingClientRect()

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
      if (arrowDownElement?.classList.contains('arrowDownDisappear')) {
        arrowUpElement?.classList.remove('arrowUpCentered')
        arrowUpElement?.classList.add('arrowUpFromCenter')
        arrowDownElement?.classList.remove('arrowDownDisappear')
        arrowDownElement?.classList.add('arrowDownAppear')
      }
    } else if (resumeRect.top === 0 || resumeRect.bottom >= window.innerHeight / 2) {
      contentSelection.value = 'resume'
      arrowUpElement?.classList.remove('arrowUpAppear')
      arrowUpElement?.classList.remove('arrowUpFromCenter')
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
  resumeElement = document.getElementById('resumeContainer')
  arrowUpElement = document.getElementById('arrowUp')
  arrowDownElement = document.getElementById('arrowDown')
  arrowDownElement?.classList.remove('arrowDownAppear')
  arrowDownElement?.classList.add('arrowDownCentered')
}
</script>

<template>
  <div class="navContainer">
    <div class="tabsContainer">
      <div class="tabs">
        <div class="tab" @click="teleport('home')">
          <v-icon v-if="contentSelection == 'home'" name="bi-house-fill" scale="2" color="teal" />
          <v-icon v-else name="bi-house" scale="2" />
        </div>
        <div class="tab" @click="teleport('about')">
          <v-icon v-if="contentSelection == 'about'" name="bi-person-fill" scale="2" color="teal" />
          <v-icon v-else name="bi-person" scale="2" />
        </div>
        <div class="tab" @click="teleport('projects')">
          <v-icon
            v-if="contentSelection == 'projects'"
            name="bi-code-slash"
            scale="2"
            color="teal"
          />
          <v-icon v-else name="bi-code-slash" scale="2" />
        </div>
        <div class="tab" @click="teleport('resume')">
          <v-icon
            v-if="contentSelection == 'resume'"
            name="bi-file-earmark-text-fill"
            scale="2"
            color="teal"
          />
          <v-icon v-else name="bi-file-earmark-text" scale="2" />
        </div>
      </div>
    </div>
    <div class="themeContainer">
      <ThemeSelector />
    </div>
    <div id="arrowUp" class="arrowUpDisappear">
      <v-icon name="bi-arrow-up-circle" scale="2" @click="up" />
    </div>
    <div id="arrowDown" class="arrowDownAppear">
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

.themeContainer {
  position: absolute;
  top: 0;
  margin-top: 25px;
}

.tabsContainer {
  display: flex;
  flex-direction: row;
  justify-content: center;
  position: absolute;
  top: 0;
  right: 0;
  width: 100vw;
  height: 5vh;
}
.tabs {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  width: 50%;
}

.tab {
  cursor: pointer;
}
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
</style>
