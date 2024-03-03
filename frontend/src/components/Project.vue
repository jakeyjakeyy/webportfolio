<script setup lang="ts">
import { defineProps, ref, defineComponent } from 'vue'
defineProps({
  image: String,
  title: String,
  description: String,
  technologies: Array as () => string[],
  link: String,
  id: String
})
const curIndex = ref(0)
</script>

<template>
  <div class="project" :id="id">
    <div class="content">
      <!-- <div class="image">
                <img :src="image" alt="project image">
            </div> -->
      <div class="title">
        <h3>{{ title }}</h3>
      </div>
      <div class="body">
        <div class="description">
          <p>{{ description }}</p>
        </div>
        <div class="technologies">
          <ul>
            <li v-for="technology in technologies?.slice(0, 5)">
              {{ technology }}
            </li>
          </ul>
          <ul v-if="technologies && technologies.length > 5">
            <li v-for="technology in technologies.slice(5, -1)">{{ technology }}</li>
          </ul>
        </div>
      </div>
      <div class="link">
        <a :href="link">Link</a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.project {
  display: flex;
  flex-direction: column;
  width: 25%;
  height: fit-content;
  border: 1px solid var(--color-background-soft);
  background-color: var(--color-background-soft);
  border-radius: 80px;
  height: 550px;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
}

@media (max-width: 1200px) {
  .project {
    width: 75%;
  }
}

.project:hover {
  border: 1px solid var(--color-accent);
}

.active {
  border: 1px solid var(--color-accent);
  box-shadow: 4px 5px 4px 0 var(--color-background) inset;
  transform: scale(0.99);
}

img {
  max-height: 100%;
  max-width: 100%;
}

.image {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
}

.content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  padding: 3rem 3rem 1rem;
}

.title {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  font-size: 2rem;
  text-align: center;
  height: 35%;
}

.link {
  display: flex;
  justify-content: center;
}

.body {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 100%;
}

.description {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: start;
  padding-left: 1rem;
  height: 50%;
}

.technologies {
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
  text-align: start;
  padding-left: 1rem;
  height: 50%;
}
</style>
