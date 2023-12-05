<script setup lang="ts">
const props = defineProps({
  destination: String
})

const buttonClick = (e: any) => {
  if (props.destination) {
    const element = document.getElementById(props.destination)
    element?.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<template>
  <v-icon name="bi-arrow-down-circle" scale="2" />
</template>
