<script setup lang="ts">
import { ref } from 'vue'
import NavBar from '@/components/NavBar.vue'
import Home from '@/components/Home.vue'
import About from '@/components/About.vue'
import Projects from '@/components/Projects.vue'
</script>

<template>
  <div class="content">
    <NavBar />
    <Home />
    <About />
    <Suspense>
      <Projects />
    </Suspense>
  </div>
</template>

<style scoped>
.content {
  overflow: hidden;
}
</style>
