<script setup lang="ts">
import PDFViewer from './PDFViewer.vue'
</script>

<template>
  <div id="resumeContainer">
    <h2 id="title">Resume and Contact</h2>
    <div class="content">
      <div class="contactLinks">
        <div class="linkTitle">
          <h3>Contact Information and Links</h3>
        </div>
        <div class="linkItem">
          <a href="mailto:contact@jakerichards.info" aria-label="email">
            <v-icon name="hi-solid-mail" scale="1.25" color="white" />
          </a>
          <a href="mailto:contact@jakerichards.info" aria-label="email">
            <p>contact@jakerichards.info</p>
          </a>
        </div>
        <div class="linkItem">
          <v-icon name="bi-telephone-fill" scale="1.25" color="white" />
          <p>(408) 713-8181</p>
        </div>
        <div class="linkItem">
          <a href="https://www.github.com/jakeyjakeyy" aria-label="github">
            <v-icon name="fa-github" scale="1.25" color="white" />
          </a>
          <a href="https://www.github.com/jakeyjakeyy"><p>GitHub</p></a>
        </div>
        <div class="linkItem">
          <a href="https://www.jakerichards.info/static/jakeRichardsResume.pdf" aria-label="resume">
            <v-icon name="bi-file-earmark-pdf-fill" scale="1.25" color="white" />
          </a>
          <a href="https://www.jakerichards.info/static/jakeRichardsResume.pdf" aria-label="resume"
            ><p>Resume</p>
          </a>
        </div>
      </div>
      <PDFViewer />
    </div>
  </div>
</template>

<style scoped>
#resumeContainer {
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  min-height: 100vh;
  padding: 0 3rem 0;
}

.contactLinks {
  display: flex;
  flex-direction: column;
  width: 30%;
  height: 100%;
  background: var(--background);
  border-radius: 1rem;
}
.linkTitle {
  width: 75%;
  padding-bottom: 1rem;
}
.linkItem {
  display: flex;
  flex-direction: row;
  padding-left: 1rem;
  p {
    color: var(--text);
    margin-left: 1rem;
  }
  a:hover,
  p:hover {
    color: var(--accent);
  }
}

@media screen and (max-width: 768px) {
  #resumeContainer {
    padding: 0 1rem 0;
  }
}

#title {
  margin: 2vh;
}

.content {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: start;
  width: 100%;
  height: 100%;
  background: var(--color-background);
  border-radius: 1rem;
  margin-top: 5rem;
}
</style>
