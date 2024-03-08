<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer.vue'
import ContentView from './views/ContentView.vue'
</script>

<template>
  <div class="app">
    <ContentView />
    <Footer />
  </div>
</template>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  height: 100%;
  width: 100vw;
  margin: 0;
  overflow: hidden;
  background-color: var(--background);
  color: var(--text);
}
</style>
