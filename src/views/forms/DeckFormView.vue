<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useDeckStore from '@/stores/decks'

import DeckForm from '@/components/forms/DeckForm.vue'

const route = useRoute()

const deckStore = useDeckStore()

const targetDeck = ref([])
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  await deckStore.FetchColors()
  const recievedId = route.params.id

  if(recievedId !== undefined && recievedId !== ''){
    targetDeck.value = await deckStore.FetchDeckById(recievedId)
  }

  fetchReady.value = true
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start mt-5 pt-5">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="route.params.id === undefined || route.params.id === '' ? 'dashboard' : 'decks'"/>
    </div>
  </div>
  <PageTitle
    :title="(route.params.id === undefined || route.params.id === '' ? 'Registrar nuevo ' : 'Modificar ') + 'deck'"
  />
  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <DeckForm
    :targetDeck = "targetDeck"
    :colors = "deckStore.colors"
    />
  </template>
</template>
