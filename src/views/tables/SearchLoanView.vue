<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

import useLoanStore from '@/stores/loans.js'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import LoanTable from '@/components/tables/LoanTable.vue'
import PageTitleView from '@/components/PageTitle.vue';
import useSessionStore from '@/stores/session'


const loanStore = useLoanStore()
const sessionStore = useSessionStore()
const route = useRoute()
const fetched = ref(false)

onMounted(async ()  => {
  const filter = route.params.filter
  if(['', undefined, 'pending'].includes(filter))
    await loanStore.FetchPendingLoans()
  else if(filter === 'returned')
    await loanStore.FetchReturnedLoans()
  else if(filter === 'active'){
    await loanStore.FetchActiveLoans()
  }
  else if(filter === 'inactive')
    await loanStore.FetchInactiveLoans()
  else
    await loanStore.FetchPendingLoans()

  fetched.value = true
})

const stateTranslator = {
  'pending': 'pendientes',
  'active': 'activos',
  'returned': 'devueltos',
  'inactive': 'inactivos'
}

</script>

<template>
  <div class="row w-100 m-0 p-0 px-5">
    <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
      <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
        <BackButtonGadget :back_to="'dashboard'"/>
      </div>
    </div>
    <PageTitleView
    :title="'Lista de préstamos ' + (['', undefined, 'pending'].includes(route.params.filter) ? 'pendientes' : stateTranslator[route.params.filter])"
    />
    <div class="row m-0 p-0 col-12 py-4 shadowed-l rounded lb-bg-terciary-ul justify-content-center">
      <AddButtonGadget
      v-if = "sessionStore.userData.permissons.includes('Préstamos')"
      :url = "'add_loan'"
      :title = "'Registrar nuevo préstamo'"
      />
      <template
      v-if="fetched === false">
        <LoadingGadget/>
      </template>
      <template v-else>
        <div class="w-100 m-0 p-3 px-5 table-container">
          <LoanTable
            :loans="loanStore.loans"
          />
        </div>
      </template>
    </div>
  </div>
</template>