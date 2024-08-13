<script setup>
import { onMounted } from 'vue'

import useDeckStore from '@/stores/decks.js'
import useSessionStore from '@/stores/session'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import DeckTable from '@/components/tables/DeckTable.vue'
import PageTitleView from '@/components/PageTitle.vue';

const deckStore = useDeckStore()
const sessionStore = useSessionStore()

onMounted(async ()  => {
  await deckStore.FetchDecks()
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
      v-if="deckStore.decks === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>
        
        <div class="w-100 m-0 p-3 px-5 table-container text-green">
          <DeckTable
            :decks="deckStore.decks"/>
        </div>
      </template>
    </div>
  </div>
</template>