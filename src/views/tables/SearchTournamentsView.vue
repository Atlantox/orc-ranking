<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'

import useTournamentStore from '@/stores/tournaments.js'
import useSessionStore from '@/stores/session'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import TournamentTable from '@/components/tables/TournamentTable.vue'
import PageTitleView from '@/components/PageTitle.vue';

const tournamentStore = useTournamentStore()
const sessionStore = useSessionStore()
const route = useRoute()

const filterTranslator = {
  'current': 'de la temporada actual',
  'active': 'activos',
  'inactive': 'inactivos',
  'all': '(todos)'
}

onMounted(async ()  => {
  await tournamentStore.FetchCurrentTournaments()

  const filter = route.params.filter
  if(['', undefined, 'current'].includes(filter))
    await tournamentStore.FetchCurrentTournaments()
  else if(filter === 'active')
    await tournamentStore.FetchActiveTournaments()
  else if(filter === 'inactive')
    await tournamentStore.FetchInactiveTournaments()  
  else if(filter === 'all')
    await tournamentStore.FetchAllTournaments()
  else
    await tournamentStore.FetchCurrentTournaments()

})

</script>

<template>
  <div class="row w-100 m-0 p-0 px-5 bg-dark-grey mt-5 pt-5">
    <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
      <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
        <BackButtonGadget :back_to="sessionStore.authenticated ? 'dashboard' : 'home'"/>
      </div>
    </div>
    <PageTitleView
    :title="['', undefined, 'current'].includes(route.params.filter) ? 'Torneos de la temporada actual' : ('Torneos ' + filterTranslator[route.params.filter])"
    />    
    <div class="row m-0 p-0 col-12 py-4 shadowed-l rounded bg-grey justify-content-center my-5">
      <template v-if="sessionStore.authenticated">
        <AddButtonGadget
        v-if = "sessionStore.userData.permissons.includes('Torneos')"
        :url = "'add_tournament'"
        :title = "'Registrar nuevo torneo'"
        />
      </template>

      <template
      v-if="tournamentStore.tournaments === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>
        
        <div class="w-100 m-0 p-3 px-5 table-container text-green">
          <TournamentTable
            :tournaments="tournamentStore.tournaments"/>
        </div>
      </template>
    </div>
  </div>
</template>