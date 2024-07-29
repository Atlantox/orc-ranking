<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useBookStore from '@/stores/books'
import useReaderStore from '@/stores/readers'
import useLoanStore from '@/stores/loans'

import LoanForm from '@/components/forms/LoanForm.vue'

const route = useRoute()

const bookStore = useBookStore()
const readerStore = useReaderStore()
const loanStore = useLoanStore()

const targetLoan = ref([])
const fetchReady = ref(false)

onMounted( async () => {
  await FetchData()
  fetchReady.value = true
})

const FetchData = ( async () => {
  await readerStore.FetchReaders()
  const recievedId = route.params.id

  if(recievedId !== undefined && recievedId !== ''){
    targetLoan.value = await loanStore.FetchLoanById(recievedId)
  }

  if(recievedId !== undefined && recievedId !== '')
    await bookStore.FetchBooks()
  else
    await bookStore.FetchBooksWithFilter({'state': 'En biblioteca'})
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="route.params.id === undefined || route.params.id === '' ? 'dashboard' : 'loans'"/>
    </div>
  </div>
  <PageTitle
    :title="(route.params.id === undefined || route.params.id === '' ? 'Registrar nuevo ' : 'Ver ') + 'préstamo'"
  />
  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <LoanForm
    :books = "bookStore.books"
    :readers = "readerStore.readers"
    :targetLoan = "targetLoan"
    @fetchAgain = "FetchData"
    />
  </template>
</template>
