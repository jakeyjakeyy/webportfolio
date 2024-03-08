<script setup lang="ts"></script>

<template>
  <footer>
    <div class="footerIcons">
      <div class="icon">
        <a href="https://www.github.com/jakeyjakeyy" aria-label="github">
          <v-icon name="fa-github" scale="1.25" />
        </a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
footer {
  width: 100%;
  height: 2.5rem;
  background-color: var(--background-soft);
  display: flex;
  justify-content: center;
  align-items: center;
}
.icon {
  width: 25px;
  height: 25px;
}

a {
  color: var(--text);
}
</style>
```
