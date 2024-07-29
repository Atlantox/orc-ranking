<script setup>
const props = defineProps({
    back_to: String
})
</script>

<template>
    <router-link class="align-middle" :to="{name: props.back_to}">
        <div class="icon-container d-flex justify-content-center align-items-center rounded lb-border-terciary hover-bigger shadowed-l lb-bg-terciary-l w-100 h-100">
            <i class="fa fa-arrow-left fs-1 my-auto text-white align-middle "></i>
        </div>
    </router-link>
</template>

<style scoped>
.icon-container{
    width:60px;
    height:60px;
}
</style>