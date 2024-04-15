<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import Home from '@/components/Home.vue'
import About from '@/components/About.vue'
import Projects from '@/components/Projects.vue'
import Resume from '@/components/Resume.vue'
</script>

<template>
  <main class="content">
    <NavBar />
    <Home />
    <About />
    <Suspense>
      <Projects />
    </Suspense>
    <Resume />
  </main>
</template>

<style scoped>
.content {
  overflow: hidden;
}
</style>
