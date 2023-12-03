<script setup lang="ts">
    defineProps({
        image: String,
        title: String,
        description: String,
        link: String,
        technologies: Array    
    })
</script>

<template>
    <div class="project">
        <div class="image">
            <img :src="image" />
        </div>
        <div class="content">
            <div class="title">
                <h2>{{ title }}</h2>
            </div>
            <div class="description">
                <p>{{ description }}</p>
            </div>
            <div class="technologies">
                <h3>Technologies</h3>
                <ul>
                    <li v-for="technology in technologies">{{ technology }}</li>
                </ul>
            </div>
            <div class="link">
                <a :href="link">Link</a>
            </div>
        </div>
    </div>
</template>

<style scoped>

.project {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
}

img {
    max-height: 100%;
    max-width: 100%;
}

.image {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    overflow: hidden;
    border-radius: 100px;
    width: 45%;
}

.content {
    display: flex;
    flex-direction: column;
    justify-content: start;
    width: 55%;
    padding: 1rem;
}

.title {
    font-size: 2rem;
}

</style>