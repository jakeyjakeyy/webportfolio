<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'
import ArrowButton from './ArrowButton.vue'
const list = ['Web', 'Frontend', 'Backend']
const index = ref(0)
const interval = ref<NodeJS.Timeout | number>(0)

const change = () => {
  const last = index.value
  index.value = (index.value + 1) % list.length
  if (last === index.value) {
    change()
  }
}

const start = () => {
  interval.value = setInterval(change, 3000)
}

onMounted(() => {
  index.value = Math.floor(Math.random() * list.length)
  start()
})
</script>

<template>
  <div id="homeContainer">
    <div class="welcome">
      <div class="name">
        <h1 class="primary">Jake</h1>
        <h1>Richards</h1>
      </div>
      <div class="description">
        <h3 class="dynamic">{{ list[index] }}</h3>
        <h3>Development</h3>
      </div>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: bold;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

#homeContainer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  height: 100vh;
  min-height: fit-content;
  background-color: var(--color-background);
}
.description {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.dynamic {
  margin-right: 0.5rem;
  color: var(--secondary);
  font-weight: bold;
  text-align: center;
  width: 30%;
}

.primary {
  color: var(--primary);
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
