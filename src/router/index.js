import { createRouter, createWebHistory } from 'vue-router'

import useSessionStore from '@/stores/session.js'

import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/DashboardView.vue'
import AboutView from '@/views/AboutView.vue'

import LoginFormView from '../views/forms/LoginFormView.vue'
import PlayerFormView from '@/views/forms/PlayerFormView.vue'
import UserFormView from '@/views/forms/UserFormView.vue'
import MyAccountFormView from '@/views/forms/MyAccountFormView.vue'
import FormatFormView from '@/views/forms/FormatFormView.vue'
import DeckFormView from '@/views/forms/DeckFormView.vue'
import TournamentFormView from '@/views/forms/TournamentFormView.vue'
import SeasonFormView from '@/views/forms/SeasonFormView.vue'

import SearchPlayersView from '@/views/tables/SearchPlayersView.vue'
import SearchDecksView from '@/views/tables/SearchDecksView.vue'
import SearchTournamentsView from '@/views/tables/SearchTournamentsView.vue'
import SearchUsersView from '@/views/tables/SearchUsersView.vue'
import SearchBinnacleView from '@/views/tables/SearchBinnacleView.vue'
import SearchFormatsView from '@/views/tables/SearchFormatsView.vue'
import SearchSeasonsView from '@/views/tables/SearchSeasonsView.vue'

import WatchPlayerView from '@/views/watchers/WatchPlayerView.vue'
import WatchTournamentView from '@/views/watchers/WatchTournamentView.vue'
import WatchDeckView from '@/views/watchers/WatchDeckView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/admin_login',
      name: 'admin_login',
      component: LoginFormView,
      meta:{ requireNotAuth: true }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta:{ requireAuth: true }
    },

    // PLAYERS
    {
      path: '/search_players',
      name: 'players',
      component: SearchPlayersView,
    },
    {
      path: '/add_player/:id?',
      name: 'add_player',
      component: PlayerFormView,
      meta:{ requireAuth: true, playerPermisson: true }
    },
    {
      path: '/see_player/:id',
      name: 'see_player',
      component: WatchPlayerView,
    },

    // DECKS
    {
      path: '/search_decks',
      name: 'decks',
      component: SearchDecksView,
    },
    {
      path: '/add_deck/:id?',
      name: 'add_deck',
      component: DeckFormView,
      meta:{ requireAuth: true, deckPermisson: true }
    },
    {
      path: '/see_deck/:id',
      name: 'see_deck',
      component: WatchDeckView,
    },

    // TOURNAMENTS
    {
      path: '/search_tournaments/:filter?',
      name: 'tournaments',
      component: SearchTournamentsView,
    },
    {
      path: '/add_tournament/:id?',
      name: 'add_tournament',
      component: TournamentFormView,
      meta:{ requireAuth: true, tournamentPermisson: true }
    },  
    {
      path: '/see_tournament/:id',
      name: 'see_tournament',
      component: WatchTournamentView,
    },   

    // FORMATS
    {
      path: '/search_formats',
      name: 'formats',
      component: SearchFormatsView,
    },
    {
      path: '/add_format/:id?',
      name: 'add_format',
      component: FormatFormView,
      meta:{ requireAuth: true, formatPermisson: true }
    },

    // SEASONS
    {
      path: '/seasons/',
      name:'seasons',
      component: SearchSeasonsView,
      meta:{ requireAuth: true, seasonPermisson: true }
    },
    {
      path: '/add_season/:id?',
      name: 'add_season',
      component: SeasonFormView,
      meta:{ requireAuth: true, seasonPermisson: true }
    },

    // USERS
    {
      path: '/add_user/:id?',
      name: 'add_user',
      component: UserFormView,
      meta:{ requireAuth: true, editorPermisson: true }
    },
    {
      path: '/search_users',
      name: 'users',
      component: SearchUsersView,
      meta:{ requireAuth: true, editorPermisson: true }
    },
    {
      path: '/account',
      name: 'account',
      component: MyAccountFormView,
      meta:{ requireAuth: true }
    },

    // BINNACLE
    {
      path: '/binnacle',
      name: 'binnacle',
      component: SearchBinnacleView,
      meta:{ requireAuth: true, binnaclePermisson: true }
    },
  ]
})

router.beforeEach(async (to, from, next) => {
  
  const sessionStore = useSessionStore()
  var routeOk = true

  if(sessionStore.authenticated){
    // Si está autenticado, validamos que el usuario esté activo, sino le cerramos la sesión
    var userIsActive = await sessionStore.MyUserIsActive()
    if(userIsActive === false){
      sessionStore.DestroySession()
      routeOk = false
    }

    if(sessionStore.lastLoginDate === null){
      // No tiene fecha de último logeo
      sessionStore.DestroySession()
      routeOk = false
    }
    else{
      var today = new Date()
      var diffHours = Math.abs(sessionStore.lastLoginDate - today) / 36e5;
      if(diffHours >= 24){
        // si el usuario tiene 24 horas o más estando autenticado, le cerramos la sesión
        sessionStore.DestroySession()
        routeOk = false
      }
    }
  }

  if(to.meta.requireAuth){
    if(!sessionStore.authenticated)
      routeOk = false
    else{
      

      if(to.meta.playerPermisson && !(sessionStore.userData.permissons.includes('Jugadores'))){
        routeOk = false
      }

      if(to.meta.deckPermisson && !(sessionStore.userData.permissons.includes('Mazos'))){
        routeOk = false
      }

      if(to.meta.tournamentPermisson && !(sessionStore.userData.permissons.includes('Torneos'))){
        routeOk = false
      }

      if(to.meta.seasonPermisson && !(sessionStore.userData.permissons.includes('Temporadas'))){
        routeOk = false
      }

      if(to.meta.formatPermisson && !(sessionStore.userData.permissons.includes('Formatos'))){
        routeOk = false
      }

      if(to.meta.editorPermisson && !(sessionStore.userData.permissons.includes('Editor'))){
        routeOk = false
      }

      if(to.meta.binnaclePermisson && !(sessionStore.userData.permissons.includes('Bitácora'))){
        routeOk = false
      }
    }
  }
  else{
    if(sessionStore.authenticated){
      if(to.meta.requireNotAuth)
        routeOk = false
    }
  }

  if(routeOk === true)
    next()
  else
    next('/')

})

export default router
