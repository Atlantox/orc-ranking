<script setup>
import { onMounted } from 'vue'

import useBookStore from '@/stores/books.js'
import useSessionStore from '@/stores/session'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import AuthorTable from '@/components/tables/AuthorTable.vue'
import PageTitleView from '@/components/PageTitle.vue';

const bookStore = useBookStore()
const sessionStore = useSessionStore()

onMounted(async ()  => {
  await bookStore.FetchAuthors()
})

</script>

<template>
  <div class="row w-100 m-0 p-0 px-5">
    <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
      <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
        <BackButtonGadget :back_to="'dashboard'"/>
      </div>
    </div>
    <PageTitleView
    :title="'Listado de autores'"
    />    
    <div class="row m-0 p-0 col-12 py-4 shadowed-l rounded lb-bg-terciary-ul justify-content-center">
      <AddButtonGadget
      v-if = "sessionStore.userData.permissons.includes('Autores')"
      :url = "'add_author'"
      :title = "'Registrar nuevo autor'"
      />

      <template
      v-if="bookStore.authors === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>
        
        <div class="w-100 m-0 p-3 px-5 table-container">
          <AuthorTable
            :authors="bookStore.authors"/>
        </div>
      </template>
    </div>
  </div>
</template>