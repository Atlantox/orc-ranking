<script setup>
import { onMounted } from 'vue'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'

import BinnacleTable from '@/components/tables/BinnacleTable.vue'
import PageTitleView from '@/components/PageTitle.vue'

import useBinnacleStore from '@/stores/binnacle'

const binnacleStore = useBinnacleStore()

onMounted(async ()  => {
  await FetchBinnacle()
})

const ResetBinnacle = (async () => {
  await FetchBinnacle()
})

const ChangeDate = (async (data) => {
  await binnacleStore.FetchBinnacleBetweenDates(data['initial_date'], data['final_date'])
})

const FetchBinnacle = (async () => {
  await binnacleStore.FetchBinnacle()
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
    :title="'Histórico de bitácora'"
    />
    <div class="row m-0 p-0 col-12 py-4 shadowed-l rounded lb-bg-terciary-ul justify-content-center">
      <template
      v-if="binnacleStore.binnacle === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>
        <div class="w-100 m-0 p-3 px-5 table-container">
          <BinnacleTable
            :binnacle="binnacleStore.binnacle"
            @ChangeDate="ChangeDate"
            @ResetBinnacle="ResetBinnacle"
          />
        </div>
      </template>
    </div>
  </div>
</template>