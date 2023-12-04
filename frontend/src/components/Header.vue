<script setup lang="ts">

</script>

<template>
  <div class="header">
    <h1 class="green">Jake Richards</h1>
    <h3>
      <!-- Web Development and Software Engineering -->
      Web and Software Development
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: bold;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
