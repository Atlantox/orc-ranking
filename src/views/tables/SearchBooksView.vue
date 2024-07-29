<script setup>
import { ref, onMounted } from 'vue'

import useUtilsStore from '@/stores/utils'
import useBookStore from '@/stores/books.js'
import useSessionStore from '@/stores/session'
import useCategoryStore from '@/stores/categories'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import BooksTable from '@/components/tables/BooksTable.vue'
import PageTitleView from '@/components/PageTitle.vue'

const utilsStore = useUtilsStore()
const bookStore = useBookStore()
const sessionStore = useSessionStore()
const categoryStore = useCategoryStore()

const targetFetched = ref(false)

const categoryFilter = ref('')
const authorFilter = ref('')
const editorialFilter = ref('')

const ApplyFilters = (async () => {
  targetFetched.value = false
  var filters = {}

  if(categoryFilter.value !== '')
    filters['category'] = categoryFilter.value

  if(authorFilter.value !== '')
    filters['author'] = authorFilter.value

  if(editorialFilter.value !== '')
    filters['editorial'] = editorialFilter.value

    if(Object.keys(filters).length === 0)
      await bookStore.FetchBooks()
    else
      await bookStore.FetchBooksWithFilter(filters)  

    targetFetched.value = true
})

onMounted(async ()  => {  
  utilsStore.InitializeSelect2()
  $('#categories').on('select2:select', function (e) {
    categoryFilter.value = e.target.value
    ApplyFilters()
  });

  $('#author').on('select2:select', function (e) {
    authorFilter.value = e.target.value
    ApplyFilters()
  });

  $('#editorial').on('select2:select', function (e) {
    editorialFilter.value = e.target.value
    ApplyFilters()
  });

  await bookStore.FetchBooks()  
  await categoryStore.FetchCategories()  
  await bookStore.FetchAuthors()  
  await bookStore.FetchEditorials()  

  targetFetched.value = true
})

</script>

<template>
  <div class="row w-100 m-0 p-0 px-5">
    <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
      <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
        <BackButtonGadget :back_to="sessionStore.authenticated ? 'dashboard' : 'home'"/>
      </div>
    </div>
    <PageTitleView
    :title="'Nuestros libros'"
    />
    <div class="row m-0 p-0 col-12 shadowed-l rounded lb-bg-terciary-ul">
      <template
      v-if="sessionStore.authenticated === true">
        <div class="col-12 m-2 mt-4 d-flex justify-content-center">
          <AddButtonGadget        
          v-if = "sessionStore.userData.permissons.includes('Libros')"
          :url = "'add_book'"
          :title = "'Registrar nuevo libro'"
          />
        </div>
      </template>

      <div class="row w-100 m-0 p-0 fs-5 p-3">
        <h3 class="w-100">
          Filtrar por...
        </h3>
        <div class="col-6 col-lg-2 fs-6 my-3 my-lg-0">
          Categoría: 
          <select class="select2 fs-6" id="categories">
            <option value="">&nbsp;</option>
            <option
            v-for="category in categoryStore.categories"
            :key="category.id"
            :value="category.id"
            >
            {{ category.name }}
          </option>
          </select>
        </div>

        <div class="col-6 col-lg-2 fs-6 my-3 my-lg-0">
          Autor:
          <select class="select2 fs-6" id="author">
            <option value="">&nbsp;</option>
            <option
            v-for="author in bookStore.authors"
            :key="author.id"
            :value="author.id"
            >
            {{ author.name }}
          </option>
          </select>
        </div>

        <div class="col-6 col-lg-2 fs-6 my-3 my-lg-0">
          Editorial: 
          <select class="select2 fs-6" id="editorial">
            <option value="">&nbsp;</option>
            <option
            v-for="editorial in bookStore.editorials"
            :key="editorial.id"
            :value="editorial.id"
            >
            {{ editorial.name }}
          </option>
          </select>
        </div>
      </div>
      <template
      v-if="targetFetched === false"
      >
        <LoadingGadget/>
      </template>
      <template v-else>
        <div class="w-100 m-0 p-3 px-2 px-lg-5 table-container" id="table-container">
          <BooksTable
            :books="bookStore.books"/>
        </div>
      </template>
    </div>
  </div>
</template>