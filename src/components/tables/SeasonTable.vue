<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';

import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()

const props = defineProps({
    seasons: {type: Array, default: []}
})

onMounted(() => {
    utilsStore.InitializeDatatables()
    OnAppearAnimation('hide-up') 
})

</script>

<template>
    <div class="w-100 m-0 p-0 hide-up animated-1">
        <table class="w-100 h6 m-0 text-white" id="normal-dt">
            <thead>
                <tr class="text-white fs-3">
                    <th class="text-center fw-normal bg-black border-green">Fecha de inicio</th>
                    <th class="text-center fw-normal bg-black border-green">Nombre</th>
                    <th class="text-center fw-normal bg-black border-green">Torneos registrados</th>
                    <th class="text-center fw-normal bg-black border-green">Ver</th>
                </tr>
                </thead>
            <tbody class="fs-4">
                <tr 
                class="text-white"
                v-for="season in props.seasons"
                :key="season.id">
                    <td class="border-green text-center">{{ season.date }}</td>
                    <td class="border-green text-center">{{ season.name }}</td>
                    <td class="border-green text-center">{{ season.tournaments }}</td>
                    <td class="border-1">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-12 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <router-link :to="{name:'add_season', params: {id: season.id}}">
                                        <i class="text-white bi bi-pencil text-center m-0 p-0"></i>
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