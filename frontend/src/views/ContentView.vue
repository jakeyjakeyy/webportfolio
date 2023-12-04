<script setup lang="ts">
import { ref, watch } from 'vue';
import Home from '@/components/Home.vue';
import About from '@/components/About.vue';
import Projects from '@/components/Projects.vue';


</script>

<template>
    <div class="content">
        <Home />
        <About />
        <Projects />
    </div>
</template>

<style scoped>
.content {
    padding: 1rem 1rem;
}
.selections {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 1rem;
}
.contentSelectionButton {
    background-color: var(--color-background-soft);
    border: none;
    border-radius: 0.25rem;
    padding: 0.5rem 1rem;
    margin: 0 0.25rem;
    cursor: pointer;
    outline: none;
    font-size: 1rem;
    font-weight: 500;
    color: var(--color-text);
    transition: all 0.2s ease-in-out;
}
.contentSelectionButton:hover, .contentSelectionButton:focus {
    background-color: var(--color-background);
    box-shadow: 0 0 0 2px var(--color-accent);
}

.contentSelectionButton.active {
    background-color: var(--color-accent);
}
</style>