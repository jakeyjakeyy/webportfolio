<script setup lang="ts">
import { ref, defineComponent } from 'vue'
defineProps({
  image: String,
  title: String,
  description: String,
  technologies: Array as () => string[],
  link: String,
  id: String,
  path: String
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
          <div>Technologies, Features, and APIs:</div>
          <div class="tech-list">
            <ul>
              <li v-for="technology in technologies?.slice(0, technologies.length / 2)">
                {{ technology }}
              </li>
            </ul>
            <ul v-if="technologies">
              <li
                v-for="technology in technologies.slice(
                  technologies.length / 2 + 1,
                  technologies.length
                )"
              >
                {{ technology }}
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="linkContainer">
        <div class="link">
          <a :href="link" target="_blank">Repo</a>
        </div>
        <div v-if="path" class="link">
          <a :href="`https://${path}.jakerichards.info`" target="_blank">Live Demo</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.project {
  display: flex;
  flex-direction: column;
  width: 25%;
  box-sizing: border-box;
  border: 1px solid var(--background);
  background-color: var(--secondary);
  border-radius: 80px;
  height: 550px;
  transition: all 0.2s ease-in-out;
  padding: 30px;
  padding-bottom: 15px;

  cursor: pointer;
}

@media (max-width: 1200px) {
  .project {
    width: 75vw;
    margin: 0 1rem;
  }
}

@media (max-width: 768px) {
  .project {
    height: 75vh;
    width: 95vw;
    margin: 0;
    flex-shrink: 0;
    margin-right: 1vw;
    scroll-snap-align: center;
  }
}

.project:hover {
  border: 1px solid var(--primary);
}

.active {
  border: 1px solid var(--accent);
  box-shadow: 4px 5px 4px 0 rgba(0, 0, 0, 0.2) inset;
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
  background-color: var(--secondary);
  border-radius: 50px;
  padding: 1rem;
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

.linkContainer {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  margin-top: 10px;
}

.link {
  display: flex;
  flex-direction: column;
  align-self: center;
  width: fit-content;
  background-color: var(--primary);
  border-radius: 1rem;
  padding: 0.25rem 0.5rem;
  margin-bottom: 5px;
  a {
    color: var(--background);
    text-align: center;
  }
}

.link:hover {
  background-color: var(--accent);
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
  text-align: center;
  padding-left: 1rem;
}

.technologies {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: start;
  padding-left: 1rem;
  height: 50%;
}

.tech-list {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: start;
  width: 100%;
  padding-right: 1rem;
}
</style>
