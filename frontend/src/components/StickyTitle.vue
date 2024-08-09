<script setup lang="ts">
defineProps({
  title: String
})

import { ref, onMounted, watch } from 'vue'
const element = ref<HTMLElement | null>(null)
const topNav = ref<HTMLElement | null>(null)
const returnPosition = ref(0)
const sticky = ref(false)

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  topNav.value = document.querySelector('.tabsContainer')
})

const handleScroll = () => {
  if (!element.value) return
  if (!topNav.value) return
  if (element.value.getBoundingClientRect().top < topNav.value.getBoundingClientRect().height) {
    element.value.style.position = 'fixed'
    element.value.style.top = `${topNav.value?.getBoundingClientRect().height}px`
    returnPosition.value = window.scrollY
    sticky.value = true
  } else if (sticky && window.scrollY < returnPosition.value) {
    element.value.style.position = 'static'
    sticky.value = false
  }
}
</script>

<template>
  <div v-if="sticky" class="hidden-title">
    <h2>{{ title }}</h2>
  </div>
  <div class="sticky-title" ref="element">
    <h2>{{ title }}</h2>
  </div>
</template>

<style scoped>
.hidden-title {
  visibility: hidden;
}
</style>
