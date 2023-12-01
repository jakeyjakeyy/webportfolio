<script setup lang="ts">
import { ref } from 'vue';
let contentSelection = ref("home");
</script>

<template>
    <div class="content">
        <h1 v-if="contentSelection=='home'">Content</h1>
    </div>
</template>