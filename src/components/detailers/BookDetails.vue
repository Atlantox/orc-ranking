<script setup>
import { ref } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router'

import LoanTable from '../tables/LoanTable.vue';

import useBookStore from '@/stores/books';
import useLoanStore from '@/stores/loans';
import useSessionStore from '@/stores/session';

const labelStyle = 'fw-bold text-end p-2 w-50 w-lg-auto'

const bookStore = useBookStore()
const loanStore = useLoanStore()
const sessionStore = useSessionStore()
const route = useRoute()

const emit = defineEmits(['changeBook'])

const sameAuthorBooks = ref([])
const sameCategoryBooks = ref([])

const props = defineProps({
    'targetBook': {type: Object, default: {}}
})

const ChangeBook = ((bookId) => {
  emit('changeBook', bookId)
})

onMounted(async () => {
  OnAppearAnimation('hide-up')
  if(sessionStore.authenticated === true)
    await loanStore.FetchLoansOfBook(route.params.id)

  sameAuthorBooks.value = await bookStore.GetBooksOfAuthor(props.targetBook.author_id, route.params.id)
  sameCategoryBooks.value = await bookStore.GetBooksOfCategories(props.targetBook.category_ids, route.params.id)
})

</script>

<template>
    <div class="hide-up animated-1 row w-100 m-0 p-0 justify-content-center align-items-start p-1 p-lg-4">
        <div class="row m-0 p-0 col-11 col-lg-8 shadowed-l rounded lb-bg-terciary-ul justify-content-around my-4">
          <div class="row m-0 p-0 col-12 col-lg-6 p-3">
            <div class="row m-0 p-0 col-12 h3">
              <table>
                <tr>
                  <td :class="labelStyle">Estado:</td>
                  <td :class="'fw-bold text-' + (props.targetBook.state === 'En biblioteca' ? 'success' : 'danger') ">{{ props.targetBook.state }}</td>
                </tr>
                <tr>
                  <td :class="labelStyle">Autor:</td>
                  <td>{{ props.targetBook.author }}</td>
                </tr>
              </table>
            </div>
          </div>
      
          <div class="row m-0 p-0 col-12 col-lg-6 p-3">
            <div class="row m-0 p-0 col-12 h3">
              <table>
                <tr>
                  <td :class="labelStyle">Editorial:</td>
                  <td>{{ props.targetBook.editorial }}</td>
                </tr>
                <tr>
                  <td :class="labelStyle">Páginas:</td>
                  <td>{{ props.targetBook.pages }}</td>
                </tr>
              </table>
            </div>
          </div>

          <div class="row m-0 p-0 col-12 p-3">
            <div class="row m-0 p-0 my-3  col-12 h3 text-center justify-content-center">
                <h3 class="fw-bold col-12 m-0">
                  Categorías
                </h3>
                <p class="fst-italic col-11 col-lg-8">
                  {{ props.targetBook.category_names.join(', ') }}
                </p>
            </div>

            <div v-if="props.targetBook.description !== ''" class="row m-0 p-0 my-3 col-12 h3 text-center justify-content-center">
                <h3 class="fw-bold m-0">
                  Descripción:
                </h3>
                <p class="fst-italic col-11 col-lg-8">
                  « {{ props.targetBook.description }} »
                </p>
            </div>
          </div>

        </div>

        <div class="row m-0 p-0 col-11 col-lg-4 justify-content-around align-items-start p-0 p-lg-4">

          <template v-if="props.targetBook.author !== null">
            <div class="row m-0 p-0 col-12 p-3 shadowed-l rounded lb-bg-terciary-ul my-2">
              <h4 class="text-center w-100">
                Otros libros de <strong>{{ props.targetBook.author }}</strong>
              </h4>
              <template v-if="sameAuthorBooks.length > 0">
                <a
                v-for="book in sameAuthorBooks"
                :key="book.id"
                class="col-12 col-lg-6 p-2 text-center text-black hover-spacing hover-bold fs-4 cursor-pointer" 
                @click="ChangeBook(book.id)">
                  {{ book.title }}
                </a>             
              </template>
              <template v-else>
                <span class="text-center w-100">
                  Por los momentos no hay
                </span>
              </template>
            </div>
          </template>
          
          <div class="row m-0 p-0 col-12 p-3 shadowed-l rounded lb-bg-terciary-ul my-2">
            <h4 class="text-center w-100">
              Libros de categorías relacionadas
            </h4>
            <template v-if="sameCategoryBooks.length > 0">
              <a
              v-for="book in sameCategoryBooks"
              :key="book.id"
              class="col-12 col-lg-6 p-2 text-center text-black hover-spacing hover-bold fs-4 cursor-pointer" 
              @click="ChangeBook(book.id)">
                {{ book.title }}
              </a>   
              </template>
              <template v-else>
                <span class="text-center w-100">
                  Por los momentos no hay
                </span>
              </template>
            </div>
          </div>

          <template v-if="sessionStore.authenticated === true">
            <!-- Book's loans -->
            <div v-if="loanStore.loans !== undefined && sessionStore.userData.permissons.includes('Préstamos')" class="col-12 col-lg-10 p-2 row shadowed-l rounded lb-bg-terciary-ul justify-content-center mt-5">
              <h2 class="w-100 text-center h1 my-3 fw-bold">
                  Préstamos del libro
              </h2>
              <div class="w-100 p-2 fs-6">
                  <LoanTable
                  :loans="loanStore.loans"
                  />
              </div>
            </div>
          </template>
    </div>

</template>

<style scoped>

</style>