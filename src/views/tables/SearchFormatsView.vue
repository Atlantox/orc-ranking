<script setup>
import { onMounted } from 'vue'

import useFormatStore from '@/stores/formats.js'
import useSessionStore from '@/stores/session'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import FormatTable from '@/components/tables/FormatTable.vue'
import PageTitleView from '@/components/PageTitle.vue';

const formatStore = useFormatStore()
const sessionStore = useSessionStore()

onMounted(async ()  => {
  await formatStore.FetchFormats()
})

</script>

<template>
  <div class="row w-100 m-0 p-0 px-5 bg-dark-grey mt-5 pt-5">
    <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
      <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
        <BackButtonGadget :back_to="'dashboard'"/>
      </div>
    </div>
    <PageTitleView
    :title="'Listado de formatos'"
    />    
    <div class="row m-0 p-0 col-12 py-4 shadowed-l rounded bg-grey justify-content-center my-5">
      <template v-if="sessionStore.authenticated">
        <AddButtonGadget
        v-if = "sessionStore.userData.permissons.includes('Formatos')"
        :url = "'add_format'"
        :title = "'Registrar nuevo formato'"
        />
      </template>

      <template
      v-if="formatStore.formats === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>
        
        <div class="w-100 m-0 p-3 px-5 table-container text-green">
          <FormatTable
            :formats="formatStore.formats"/>
        </div>
      </template>
    </div>
  </div>
</template>