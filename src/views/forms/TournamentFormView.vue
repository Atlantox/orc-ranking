<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useTournamentStore from '@/stores/tournaments'

import TournamentForm from '@/components/forms/TournamentForm.vue'

const route = useRoute()

const tournamentStore = useTournamentStore()

const targetTournament = ref([])
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  const recievedId = route.params.id

  if(recievedId !== undefined && recievedId !== ''){
    targetTournament.value = await tournamentStore.GetTournamentById(recievedId)
  }

  fetchReady.value = true
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start mt-5 pt-5">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="route.params.id === undefined || route.params.id === '' ? 'dashboard' : 'tournaments'"/>
    </div>
  </div>
  <PageTitle
    :title="(route.params.id === undefined || route.params.id === '' ? 'Registrar nuevo ' : 'Modificar ') + 'torneo'"
  />
  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <TournamentForm
    :targetTournament = "targetTournament"
    />
  </template>
</template>
