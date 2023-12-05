<script setup lang="ts">
let contentSelection: String = 'home'
const up = () => {
  if (contentSelection === 'about') {
    const element = document.getElementById('homeContainer')
    element?.scrollIntoView({ behavior: 'smooth' })
    contentSelection = 'home'
  } else if (contentSelection === 'projects') {
    const element = document.getElementById('aboutContainer')
    element?.scrollIntoView({ behavior: 'smooth' })
    contentSelection = 'about'
  }
}
const down = () => {
  console.log(contentSelection)
  if (contentSelection === 'home') {
    const element = document.getElementById('aboutContainer')
    element?.scrollIntoView({ behavior: 'smooth' })
    contentSelection = 'about'
  } else if (contentSelection === 'about') {
    const element = document.getElementById('projectContainer')
    element?.scrollIntoView({ behavior: 'smooth' })
    contentSelection = 'projects'
  }
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
