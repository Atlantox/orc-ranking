<script setup>
import { onMounted } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer.js'
const props = defineProps({
    'title': String
})


onMounted(() => {
    OnAppearAnimation('hide-up')  
})

</script>

<template>
    <div class="row m-0 p-0 justify-content-center my-3">
        <div class="col-12 col-lg-8 m-0 p-0 my-2">
            <h1 class="w-100 text-center hide-up fw-bold m-0 text-black outline-black">
                {{ props.title }}
            </h1>
        </div>
    </div>
</template>

<style scoped>
h1{
    font-size:60px;
    transition:0.8s;
    letter-spacing: 2px;
    color: #7ad9c3;
}

@media (max-width: 500px) {
    h1{
        font-size:42px;
    }
  }
</style>
