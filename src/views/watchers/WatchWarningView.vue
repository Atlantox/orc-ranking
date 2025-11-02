<script setup>

import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'
import WarningDetails from '@/components/detailers/WarningDetails.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useWarningStore from '@/stores/warnings'

import OnAppearAnimation from '@/utils/ElegantDisplayer'

const route = useRoute()
const router = useRouter()
const warningStore = useWarningStore()

const targetWarning = ref({})
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  targetWarning.value = {}
  var recievedId = route.params.id
  
  if(recievedId !== undefined && recievedId !== ''){
    targetWarning.value = await warningStore.FetchWarningById(recievedId)
    if(targetWarning.value === false)
      router.push({name: 'warnings', params:{filter: 'all'}})
  }
  else
    router.push({name: 'warnings', params:{filter: 'all'}})
  
  fetchReady.value = true
  OnAppearAnimation('hide-up')
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="'dashboard'"/>
    </div>
  </div>

  <PageTitle
    :title="'Detalles de warning'"
  />

  

  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <WarningDetails
    :targetWarning="targetWarning"
    />
  </template>
</template>

<style scoped>

</style>
