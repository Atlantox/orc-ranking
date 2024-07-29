<script setup>
import { onMounted } from 'vue'

import useReaderStore from '@/stores/readers.js'
import useSessionStore from '@/stores/session'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import ReaderTable from '@/components/tables/ReaderTable.vue'
import PageTitleView from '@/components/PageTitle.vue';

const readerStore = useReaderStore()
const sessionStore = useSessionStore()

onMounted(async ()  => {
  await readerStore.FetchReaders()
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
    :title="'Listado de los lectores'"
    />
    <div class="row m-0 p-0 col-12 py-4 shadowed-l rounded lb-bg-terciary-ul justify-content-center">
      <AddButtonGadget
      v-if = "sessionStore.userData.permissons.includes('Lectores')"
      :url = "'add_reader'"
      :title = "'Registrar nuevo lector'"
      />
      <template
      v-if="readerStore.readers === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>
        <div class="w-100 m-0 p-3 px-5 table-container hide-up">
          <ReaderTable
            :readers="readerStore.readers"/>
        </div>
      </template>
    </div>
  </div>
</template>