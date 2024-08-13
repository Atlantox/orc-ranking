<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'
import PlayerDetails from '@/components/detailers/PlayerDetails.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import usePlayerStore from '@/stores/players'
import useSessionStore from '@/stores/session'

import OnAppearAnimation from '@/utils/ElegantDisplayer'

const route = useRoute()

const playerStore = usePlayerStore()
const sessionStore = useSessionStore()

const targetPlayer = ref({})
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  targetPlayer.value = {}
  var recievedId = route.params.id
  
  if(recievedId !== undefined && recievedId !== '')
    targetPlayer.value = await playerStore.FetchPlayerById(recievedId)
  else
    router.push({name: 'players'})
  
  fetchReady.value = true
  OnAppearAnimation('hide-up')
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="sessionStore.authenticated === true ? 'dashboard' : 'players'"/>
    </div>
  </div>

  <PageTitle
    :title="targetPlayer.name"
  />

  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <PlayerDetails
    :targetPlayer="targetPlayer"
    />
  </template>
</template>

<style scoped>

</style>
