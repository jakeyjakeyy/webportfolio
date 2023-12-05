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
        <div class="content">
            <!-- <div class="image">
                <img :src="image" alt="project image">
            </div> -->
            <div class="title">
                <h3>{{ title }}</h3>
            </div>
            <div class="description">
                <p>{{ description }}</p>
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
    flex-direction: column;
    align-items: center;
    width: 30%;
    height: fit-content;
    border: 1px solid var(--color-background-soft);
    background-color: var(--color-background-soft);
    border-radius: 80px;
    height: 550px;
}

img {
    max-height: 100%;
    max-width: 100%;
}

.image {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
}

.content {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    height: 100%;
    padding: 3rem 3rem 1rem;
}

.title {
    font-size: 2rem;
    text-align: center;
}

.link {
    display: flex;
    justify-content: center;
}

</style>