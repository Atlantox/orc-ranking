<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import usePlayerStore from '@/stores/players'

import PlayerForm from '@/components/forms/PlayerForm.vue'

const route = useRoute()

const playerStore = usePlayerStore()

const targetPlayer = ref([])
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  const recievedId = route.params.id

  if(recievedId !== undefined && recievedId !== ''){
    targetPlayer.value = await playerStore.FetchPlayerById(recievedId)
  }

  fetchReady.value = true
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start mt-5 pt-5">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="route.params.id === undefined || route.params.id === '' ? 'dashboard' : 'players'"/>
    </div>
  </div>
  <PageTitle
    :title="(route.params.id === undefined || route.params.id === '' ? 'Registrar nuevo ' : 'Modificar ') + 'jugador'"
  />
  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <PlayerForm
    :targetPlayer = "targetPlayer"
    />
  </template>
</template>
