<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useTournamentStore from '@/stores/tournaments'

import TournamentDetails from '@/components/detailers/TournamentDetails.vue'

const route = useRoute()

const tournamentStore = useTournamentStore()

const targetTournament = ref([])
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  const recievedId = route.params.id
  targetTournament.value = await tournamentStore.GetTournamentById(recievedId)
  fetchReady.value = true
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start mt-5 pt-5">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget back_to="tournaments"/>
    </div>
  </div>
  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <PageTitle
      :title="'Torneo Nº ' + targetTournament.data.id"
    />
    <TournamentDetails
    :targetTournament = "targetTournament"
    />
  </template>
</template>
