<script setup lang="ts">
import { on } from 'events'
import { onMounted, ref } from 'vue'
let themeLight = ref(true)
let root: HTMLElement = document.getElementById('app') as HTMLElement

const toggleTheme = () => {
  themeLight.value = !themeLight.value
  if (root && themeLight.value) {
    root.classList.add('light')
    root.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  } else if (root) {
    root.classList.add('dark')
    root.classList.remove('light')
    localStorage.setItem('theme', 'dark')
  }
}

onMounted(() => {
  const localTheme = localStorage.getItem('theme')
  if (localTheme === 'light') {
    themeLight.value = true
  } else if (localTheme === 'dark') {
    themeLight.value = false
    root.classList.add('dark')
    root.classList.remove('light')
  }
})
</script>

<template>
  <div v-if="themeLight" class="themeSelector">
    <v-icon name="fa-moon" scale="1" @click="toggleTheme" />
  </div>
  <div v-else class="themeSelector">
    <v-icon name="fa-sun" scale="1" @click="toggleTheme" />
  </div>
</template>

<style scoped>
.themeSelector {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  width: 100%;
  height: 100%;
  cursor: pointer;
  color: var(--text);
}
</style>
