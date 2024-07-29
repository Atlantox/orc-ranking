<script setup>
import { useRouter } from 'vue-router'
import useSessionStore from '@/stores/session.js'
const sessionStore = useSessionStore()
const router = useRouter()

const ToggleNavbar = (() => {
    const collapser = document.getElementById('navbarCollapse')
    if(collapser.classList.contains('show'))
        collapser.classList.remove('show')
    else
        collapser.classList.add('show')
})

const CloseSession = (() => {
    sessionStore.DestroySession()
    router.push({name: 'home'})
})

</script>

<template>
    <!-- Designed by Atlantox https://atlantox.pythonanywhere.com/ -->
    <nav class="navbar navbar-expand-lg navbar-dark p-0 bg-dark-grey" style="padding:0 !important" id="headerNav">
      <div class="container-fluid">
        <rounter-link class="navbar-brand d-block d-lg-none" :to="{name: 'home'}">
          <img src="@/assets/images/orc.png" height="80" />
        </rounter-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class=" collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav mx-auto fs-5">
            <li class="nav-item">
              <rounter-link class="nav-link mx-2 text-orange" aria-current="page" :to="{name: 'home'}">Dashboard</rounter-link>
            </li>
            <li class="nav-item">
              <rounter-link class="nav-link mx-2 text-orange" aria-current="page" :to="{name: 'home'}">Jugadores</rounter-link>
            </li>
            <li class="nav-item">
              <rounter-link class="nav-link mx-2 text-orange" :to="{name: 'home'}">Mazos</rounter-link>
            </li>

            <li class="nav-item d-none d-lg-block">
              <router-link class="nav-link mx-4" :to="{name: 'home'}">
                <img class="big-orc" src="@/assets/images/orc.png" height="80" />
              </router-link>
            </li>

            <li class="nav-item">
              <rounter-link class="nav-link mx-2 text-orange" :to="{name: 'home'}">Torneos</rounter-link>
            </li>
            <li class="nav-item">
              <rounter-link class="nav-link mx-2 text-orange" :to="{name: 'home'}">Acerca</rounter-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link mx-2 dropdown-toggle text-orange" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                USUARIO
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <li><rounter-link class="dropdown-item" :to="{name: 'home'}">Mi cuenta</rounter-link></li>
                <li><rounter-link class="dropdown-item" :to="{name: 'home'}">Cerrar sesión</rounter-link></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</template>

<style scoped>
.navbar .dropdown-toggle::after {
  content: "\f282";
  display: inline-block;
  font-family: bootstrap-icons !important;
  font-size: var(--copyright-font-size);
  font-style: normal;
  font-weight: normal !important;
  font-variant: normal;
  text-transform: none;
  line-height: 1;
  vertical-align: -.125em;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
  left: 2px;
  border: 0;
}

.navbar-brand{
    transform:scale(1.5)
}

.big-orc{
    transform:scale(1.8) translateY(20px);
}

.navbar{
    box-shadow:0 5px 5px rgba(112, 112, 112, 0.7) !important;
}
</style>
