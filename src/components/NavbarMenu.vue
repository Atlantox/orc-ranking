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
    <nav class="navbar navbar-expand-lg navbar-dark p-0 bg-black" style="padding:0 !important" id="headerNav">
      <div class="container-fluid">
        <router-link class="navbar-brand d-block d-lg-none" :to="{name: 'home'}">
          <img src="@/assets/images/orc.png" height="80" />
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class=" collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav mx-auto fs-5">
            <li class="nav-item" v-if="sessionStore.authenticated">
              <router-link class="nav-link mx-2 text-green cursor-pointer my-nav-link" aria-current="page" :to="{name: 'home'}">Dashboard</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link mx-2 text-green cursor-pointer my-nav-link" aria-current="page" :to="{name: 'players'}">Jugadores</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link mx-2 text-green cursor-pointer my-nav-link" :to="{name: 'decks'}">Decks</router-link>
            </li>

            <li class="nav-item d-none d-lg-block">
              <router-link class="nav-link mx-4" :to="{name: 'home'}">
                <img class="big-orc" src="@/assets/images/orc.png" height="80" />
              </router-link>
            </li>

            <li class="nav-item">
              <router-link class="nav-link mx-2 text-green cursor-pointer my-nav-link" :to="{name: 'tournaments'}">Torneos</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link mx-2 text-green cursor-pointer my-nav-link" :to="{name: 'home'}">Acerca</router-link>
            </li>
            <li class="nav-item dropdown" v-if="sessionStore.authenticated">
              <a class="nav-link mx-2 dropdown-toggle text-green cursor-pointer my-nav-link" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                {{ sessionStore.userData.nickname }}
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <li><router-link class="dropdown-item" :to="{name: 'home'}">Mi cuenta</router-link></li>
                <li><router-link class="dropdown-item" @click="CloseSession">Cerrar sesión</router-link></li>
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

.my-nav-link{
  transition: 0.1s;
}

.my-nav-link:hover{
  border-bottom: 2px rgb(87, 211, 97) solid;
}
</style>
