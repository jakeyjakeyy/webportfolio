<script setup lang="ts">
import { ref } from 'vue';
import About from '@/components/About.vue';
let contentSelection = ref("Home");
</script>

<template>
    <div class="content">
        <div class="selections">
            <button
            tabindex="0"
            @click="contentSelection='Home'" 
            @keyup.enter.space="contentSelection='Home'"
            :class="{active: contentSelection === 'Home'}" class="contentSelectionButton">
            Home
            </button>
            <button
            tabindex="0"
            @click="contentSelection='About'" 
            @keyup.enter.space="contentSelection='About'"
            :class="{active: contentSelection === 'About'}" class="contentSelectionButton">
            About
            </button>
            <button
            tabindex="0"
            @click="contentSelection='Projects'" 
            :class="{active: contentSelection === 'Projects'}" class="contentSelectionButton">
            Projects
            </button>
            <button
            tabindex="0"
            @click="contentSelection='Contact'" 
            :class="{active: contentSelection === 'Contact'}" class="contentSelectionButton">
            Contact
        </button>
        </div>
        <h1>{{ contentSelection }}</h1>
        <div v-if="contentSelection === 'Home'">
            <p>Thanks for vising my web portfolio!</p>
            <p>I'd love to hear from you, click <a href="mailto:jakerichards210@gmail.com">here</a> to send me an email, or view the Contact page to see my other contact information.</p>
        </div>
        <div v-if="contentSelection === 'About'">
            <About />
        </div>
    </div>
</template>

<style scoped>
.content {
    padding: 1rem 1rem;
    flex: 1 0 auto;
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
    transition: background-color 0.2s ease-in-out;
}
.contentSelectionButton:hover {
    background-color: var(--color-background);
}

.contentSelectionButton.active {
    background-color: var(--color-accent);
}
</style>