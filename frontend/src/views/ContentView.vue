<script setup lang="ts">
import { ref } from 'vue';
let contentSelection = ref("Home");
</script>

<template>
    <div class="content">
        <div class="selections">
            <div v-on:click="contentSelection='Home'" :class="{active: contentSelection === 'Home'}" class="contentSelectionButton">Home</div>
            <div v-on:click="contentSelection='About'" :class="{active: contentSelection === 'About'}" class="contentSelectionButton">About</div>
            <div v-on:click="contentSelection='Projects'" :class="{active: contentSelection === 'Projects'}" class="contentSelectionButton">Projects</div>
            <div v-on:click="contentSelection='Contact'" :class="{active: contentSelection === 'Contact'}" class="contentSelectionButton">Contact</div>
        </div>
        <h1>{{ contentSelection }}</h1>
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
    margin: 0 1rem;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    background-color: var(--color-background-soft);
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}
.contentSelectionButton:hover {
    background-color: var(--color-background);
}

.contentSelectionButton.active {
    background-color: var(--color-accent);
}
</style>