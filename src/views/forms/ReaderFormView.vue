<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useReaderStore from '@/stores/readers'

import ReaderForm from '@/components/forms/ReaderForm.vue'

const route = useRoute()

const readerStore = useReaderStore()

const targetReader = ref([])
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  const recievedId = route.params.id
  
  if(recievedId !== undefined && recievedId !== ''){
    targetReader.value = await readerStore.FetchReaderById(recievedId)
  }

  fetchReady.value = true
})


</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="route.params.id === undefined || route.params.id === '' ? 'dashboard' : 'readers'"/>
    </div>
  </div>

  <PageTitle
    :title="(route.params.id === undefined || route.params.id === '' ? 'Registrar nuevo ' : 'Modificar ') + 'lector'"
  />

  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <ReaderForm
    :targetReader="targetReader"
    />
  </template>
</template>