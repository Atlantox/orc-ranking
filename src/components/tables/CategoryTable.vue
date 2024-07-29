<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';

import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()

const props = defineProps({
    categories: {type: Array, default: []}
})

onMounted(() => {
    utilsStore.InitializeDatatables()
    OnAppearAnimation('hide-up') 
})

</script>

<template>
    <div class="w-100 m-0 p-0 hide-up animated-1">
        <table class="w-100 h6 m-0" id="normal-dt">
            <thead>
                <tr class="text-white fs-4">
                    <th class="text-center lb-bg-terciary border-1">Nombre</th>
                    <th class="text-center lb-bg-terciary border-1">Ver</th>
                </tr>
                </thead>
            <tbody class="fs-5">
                <tr 
                v-for="category in props.categories"
                :key="category.id">
                    <td class="border-1 text-center">{{ category.name }}</td>
                    <td class="border-1">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-12 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <router-link :to="{name:'add_category', params: {id: category.id}}">
                                        <i class="text-black bi bi-pencil text-center m-0 p-0"></i>
                                    </router-link>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>