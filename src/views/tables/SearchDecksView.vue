<script setup>
import { ref, onMounted } from 'vue'

import useDeckStore from '@/stores/decks.js'
import useSessionStore from '@/stores/session'
import useSeasonStore from '@/stores/seasons'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import DeckTable from '@/components/tables/DeckTable.vue'
import PageTitleView from '@/components/PageTitle.vue';

const deckStore = useDeckStore()
const sessionStore = useSessionStore()
const seasonStore = useSeasonStore()

const selectedSeason = ref("")

onMounted(async ()  => {
  await deckStore.FetchDecks()
  await seasonStore.FetchSeasons()  

  seasonStore.seasons.forEach((s) => {
    if(s.active === 1)
      selectedSeason.value = s.id
  })
})

const FetchDecksBySeason = (async () => {
  await deckStore.FetchDecksBySeason(selectedSeason.value)
})

</script>

<template>
  <div class="row w-100 m-0 p-0 px-3 px-lg-5 bg-dark-grey mt-5 pt-5">
    <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
      <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
        <BackButtonGadget :back_to="sessionStore.authenticated ? 'dashboard' : 'home'"/>
      </div>
    </div>
    <PageTitleView
    :title="'Listado de mazos'"
    />    
    <div class="row m-0 p-0 col-12 py-4 shadowed-l rounded bg-grey justify-content-center my-5">
      <template v-if="sessionStore.authenticated">
        <AddButtonGadget
        v-if = "sessionStore.userData.permissons.includes('Mazos')"
        :url = "'add_deck'"
        :title = "'Registrar nuevo mazo'"
        />
      </template>


      <template
      v-if="seasonStore.seasons === undefined">
        <LoadingGadget/>
      </template>
      <div v-else class="row col-100 m-0 p-0 fs-5 p-3 justify-content-center justify-content-lg-start">
        <h3 class="col-100 text-white text-center text-lg-start">
          Filtrar por temporada
        </h3>
        <div class="col-6 col-lg-2 fs-6 px-1 px-lg-5">
          <select class="myInput px-2 w-100 fs-4 text-center" id="season-select" @change="FetchDecksBySeason" v-model="selectedSeason">
            <option 
            v-for="season in seasonStore.seasons"
            :key="season.id"
            :value="season.id"
            :selected="season.active === 1"
            class="align-middle text-center"
            >
              Season {{ season.name }}
            </option>
          </select>
        </div>
      </div>

      <template
      v-if="deckStore.decks === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>
        
        <div class="w-100 m-0 p-3 px-1 px-lg-5 table-container text-green">
          <DeckTable
            :decks="deckStore.decks"/>
        </div>
      </template>
    </div>
  </div>
</template>