<script setup lang="ts">
import { ref } from 'vue'
let themeLight = ref(false)

const toggleTheme = () => {
  themeLight.value = !themeLight.value
}
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
