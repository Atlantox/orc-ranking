<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const DisplayLogin = (() => {
  router.push({name: 'admin_login'})
})
</script>

<template>
    <!-- Designed by Atlantox https://atlantox.pythonanywhere.com/ -->
    <div class="row m-0 p-0 justify-content-center my-4 mb-0 bg-black">
        <div class="col-12 mt-5 p-0 text-center py-2 text-white">
            Made by 
            <a href="https://atlantox.pythonanywhere.com/">
                Atlantox7
                <img style="width:40px;" src="@/assets/icons/atlantox-icon.png" alt="">
            </a>
        </div>
        <span class="text-black text-center" @dblclick="DisplayLogin">
            AZUL HASTA LA MUERTE
        </span>
    </div>
</template>