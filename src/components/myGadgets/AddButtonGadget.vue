<script setup>
const props = defineProps({
    'url': String,
    'title': String
})
</script>

<template>
    <div class="add-button " :title="props.title">
        <router-link class="align-middle" :to="{name: props.url}">
            <div class="icon-container d-flex justify-content-center align-items-center rounded lb-border-primary shadowed-l bg-white hover-bigger">
                <i class="fa fa-plus fs-1 my-auto lb-text-primary-dark align-middle "></i>
            </div>
        </router-link>
    </div>
</template>

<style scoped>

</style>