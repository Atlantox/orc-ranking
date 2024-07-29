<script setup>
import { onMounted } from 'vue'

import useCategoryStore from '@/stores/categories.js'
import useSessionStore from '@/stores/session'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import AddButtonGadget from '@/components/myGadgets/AddButtonGadget.vue'

import CategoryTable from '@/components/tables/CategoryTable.vue'
import PageTitleView from '@/components/PageTitle.vue';

const categoryStore = useCategoryStore()
const sessionStore = useSessionStore()

onMounted(async ()  => {
  await categoryStore.FetchCategories()
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
    :title="'Listado de categorías'"
    />
    <div class="row m-0 p-0 col-12 py-4 shadowed-l rounded lb-bg-terciary-ul justify-content-center">
      <AddButtonGadget
      v-if = "sessionStore.userData.permissons.includes('Categorías')"
      :url = "'add_category'"
      :title = "'Registrar nueva categoría'"
      />
      <template
      v-if="categoryStore.categories === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>
        <div class="w-100 m-0 p-3 px-5 table-container">
          <CategoryTable
            :categories="categoryStore.categories"
          />
        </div>
      </template>
    </div>
  </div>
</template>