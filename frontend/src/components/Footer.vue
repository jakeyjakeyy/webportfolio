<script setup lang="ts"></script>

<template>
  <footer>
    <div class="footerIcons">
      <div class="icon">
        <a href="https://www.github.com/jakeyjakeyy" aria-label="github" target="_blank">
          <v-icon name="fa-github" scale="1.25" />
        </a>
      </div>
      <div class="icon">
        <a href="mailto:contact@jakerichards.info" aria-label="email" target="_blank">
          <v-icon name="hi-solid-mail" scale="1.25" />
        </a>
      </div>
      <div class="icon">
        <a
          href="https://www.linkedin.com/in/jakerichards-info/"
          aria-label="linkedin"
          target="_blank"
        >
          <v-icon name="co-linkedin" scale="1.25" />
        </a>
      </div>
    </div>
    <div class="version">
      <p>v1.3.3</p>
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

.version {
  position: absolute;
  right: 1rem;
  font-size: smaller;
  color: var(--text);
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
