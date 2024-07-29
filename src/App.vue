<script setup>
import NavbarMenu from '@/components/NavbarMenu.vue'
import Footer from '@/components/Footer.vue'

</script>

<template>
  <!-- Designed by Atlantox https://atlantox.pythonanywhere.com/ -->
  <div class="row m-0 p-0 h6 align-items-start">
    <section class="row m-0 p-0 col-12 mb-5">
      <NavbarMenu/>
    </section>
    <section class="row m-0 p-0 col-12 align-items-start">
      <router-view></router-view>  
    </section>
    <section class="row m-0 p-0 col-12 align-items-start">
      <Footer/>
    </section>
  </div>
</template>

<style scoped lang="scss">
.my-sidebar{
  border-top-right-radius: 30px;
  border-bottom-right-radius: 30px;
  height:100vh;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
}

.menu-hider{
  font-size:40px;
  font-weight: 800;
}

a{
  color:white !important;
  text-decoration:none
}
</style>
