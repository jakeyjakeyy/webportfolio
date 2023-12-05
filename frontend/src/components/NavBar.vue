<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'
const props = defineProps({
  contentSelection: String
})

const emit = defineEmits(['update:contentSelection'])

const up = () => {
  if (props.contentSelection === 'home') {
    emit('update:contentSelection', 'projects')
  } else if (props.contentSelection === 'projects') {
    emit('update:contentSelection', 'about')
  } else if (props.contentSelection === 'about') {
    emit('update:contentSelection', 'home')
  }
}
const down = () => {
  if (props.contentSelection === 'home') {
    emit('update:contentSelection', 'about')
  } else if (props.contentSelection === 'about') {
    emit('update:contentSelection', 'projects')
  } else if (props.contentSelection === 'projects') {
    emit('update:contentSelection', 'home')
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
