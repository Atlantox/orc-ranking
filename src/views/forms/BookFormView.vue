<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useBookStore from '@/stores/books'
import useCategoryStore from '@/stores/categories'

import BookForm from '@/components/forms/BookForm.vue'

const route = useRoute()

const categoryStore = useCategoryStore()
const bookStore = useBookStore()

const targetBook = ref([])
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  const recievedId = route.params.id

  
  if(recievedId !== undefined && recievedId !== ''){
    targetBook.value = await bookStore.FetchBookById(recievedId)
  }

  await FetchData()
  fetchReady.value = true
})

const FetchData = ( async () => {
  SpinSymbol()
  await bookStore.FetchEditorials()
  await bookStore.FetchAuthors()  
  await bookStore.FetchBookStates()
  await categoryStore.FetchCategories()
})

const SpinSymbol = (() =>{
  const spinIcon = document.getElementById('spin-icon')
  if (spinIcon !== null){
    spinIcon.classList.remove('spin-on')
    void spinIcon.offsetWidth
    spinIcon.classList.add('spin-on')
  }
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="route.params.id === undefined || route.params.id === '' ? 'dashboard' : 'books'"/>
    </div>
  </div>

  <PageTitle
    :title="(route.params.id === undefined || route.params.id === '' ? 'Registrar nuevo ' : 'Modificar ') + 'libro'"
  />

  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>
    <div class="row w-100 m-0 p-0 justify-content-center">
      <div class="col-1">
        <button 
        @click="FetchData()" 
        class="icon-container d-flex justify-content-center align-items-center rounded lb-border-terciary shadowed-l lb-bg-terciary-l p-2 mx-auto hide-up animated-1" 
        title="Refrescar autores y editoriales"
        >
            <i class="fa fa-rotate-left fs-1 my-auto text-white align-middle" id="spin-icon"></i>
        </button>
      </div>
    </div>
    
    <BookForm
    :targetBook = "targetBook"
    :editorials = "bookStore.editorials"
    :authors = "bookStore.authors"
    :bookStates = "bookStore.bookStates"
    :categories = "categoryStore.categories"
    @fetchAgain = "FetchData"
    />
  </template>
</template>

<style scoped>
 .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;
 
  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
}

 .tooltiptext{
  visibility: visible;
}
</style>
