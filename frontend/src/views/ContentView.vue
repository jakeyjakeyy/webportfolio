<script setup lang="ts">
import { ref } from 'vue'
import NavBar from '@/components/NavBar.vue'
import Home from '@/components/Home.vue'
import About from '@/components/About.vue'
import Projects from '@/components/Projects.vue'

const contentSelection = ref('home')
</script>

<template>
  <div class="content">
    <NavBar
      :contentSelection="contentSelection"
      @update:contentSelection="contentSelection = $event"
    />
    <Home v-show="contentSelection == 'home'" />
    <About v-show="contentSelection == 'about'" />
    <Projects v-show="contentSelection == 'projects'" />
  </div>
</template>

<style scoped>
.selections {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1rem;
}
.contentSelectionButton {
  background-color: var(--color-background-soft);
  border: none;
  border-radius: 0.25rem;
  padding: 0.5rem 1rem;
  margin: 0 0.25rem;
  cursor: pointer;
  outline: none;
  font-size: 1rem;
  font-weight: 500;
  color: var(--color-text);
  transition: all 0.2s ease-in-out;
}
.contentSelectionButton:hover,
.contentSelectionButton:focus {
  background-color: var(--color-background);
  box-shadow: 0 0 0 2px var(--color-accent);
}

.contentSelectionButton.active {
  background-color: var(--color-accent);
}
</style>
