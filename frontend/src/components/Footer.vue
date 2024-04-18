<script setup lang="ts"></script>

<template>
  <footer>
    <div class="footerIcons">
      <div class="icon">
        <a href="https://www.github.com/jakeyjakeyy" aria-label="github">
          <v-icon name="fa-github" scale="1.25" />
        </a>
      </div>
      <div class="icon">
        <a href="mailto:contact@jakerichards.info" aria-label="email">
          <v-icon name="hi-solid-mail" scale="1.25" />
        </a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
footer {
  width: 100vw;
  height: 2.5rem;
  background-color: var(--primary);
  display: flex;
  justify-content: center;
  align-items: center;
}

.footerIcons {
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon {
  width: 25px;
  height: 25px;
  margin: 0 0.5rem;
}

a {
  color: var(--text);
}
</style>
