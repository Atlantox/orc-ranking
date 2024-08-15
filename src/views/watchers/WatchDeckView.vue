<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'
import DeckDetails from '@/components/detailers/DeckDetails.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useDeckStore from '@/stores/decks'

import OnAppearAnimation from '@/utils/ElegantDisplayer'

const route = useRoute()

const deckStore = useDeckStore()

const targetDeck = ref({})
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  targetDeck.value = {}
  var recievedId = route.params.id
  
  if(recievedId !== undefined && recievedId !== '')
    targetDeck.value = await deckStore.FetchDeckById(recievedId)
  else
    router.push({name: 'decks'})
  
  fetchReady.value = true
  OnAppearAnimation('hide-up')
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="'decks'"/>
    </div>
  </div>

  <PageTitle
    :title="targetDeck.name"
  />

  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <DeckDetails
    :targetDeck="targetDeck"
    />
  </template>
</template>

<style scoped>

</style>
