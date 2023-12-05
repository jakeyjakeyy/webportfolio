<script setup lang="ts">
const props = defineProps({
  destination: String,
  direction: String
})

const buttonClick = () => {
  console.log(props.destination)
  if (props.destination) {
    const element = document.getElementById(props.destination)
    element?.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<template>
  <div class="arrowButton">
    <v-icon
      :name="props.direction === 'down' ? 'bi-arrow-down-circle' : 'bi-arrow-up-circle'"
      scale="2"
      :onclick="buttonClick"
    />
  </div>
</template>

<style scoped>
.arrowButton {
  cursor: pointer;
}
</style>
