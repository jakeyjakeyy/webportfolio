<script setup lang="ts">
const pdfSource = 'https://jakerichards.info/static/jakeRichardsResume.pdf'
</script>

<template>
  <div id="pdfContainer">
    <iframe :src="pdfSource" width="100%" height="100%"></iframe>
  </div>
</template>

<style scoped>
#pdfContainer {
  height: 75vh;
  width: 35vw;
  iframe {
    border: none;
  }
}

@media screen and (max-width: 768px) {
  #pdfContainer {
    width: 100%;
  }
}
</style>
