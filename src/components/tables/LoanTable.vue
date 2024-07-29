<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';
import useSessionStore from '@/stores/session';

import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()
const sessionStore = useSessionStore()

const props = defineProps({
    loans: {type: Array, default: []}
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
            <tr class="text-white">
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Lector</th>
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Libro</th>
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Fecha de entrega</th>
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Fecha de devolución</th>
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Observación</th>
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Acción</th>
            </tr>
            </thead>
            <tbody>
            <tr 
            v-for="loan in props.loans"
            :key="loan.id">
                <td class="border-1"><strong>({{ loan.cedula }})</strong> {{ loan.fullname }}</td>
                <td class="border-1">{{ loan.title }}</td>
                <td class="border-1 text-center">{{ new Date(loan.full_deliver_date).toLocaleDateString('es-VE', { hour: '2-digit', minute: '2-digit', timeZone: 'America/Caracas'}) }}</td>
                <td class="border-1 text-center">{{ loan.return_date === null ? 'No tiene' : new Date(loan.full_return_date).toLocaleDateString('es-VE', { hour: '2-digit', minute: '2-digit', timeZone: 'America/Caracas'}) }}</td>
                <td class="border-1">{{ loan.observation }}</td>
                <td class="border-1">
                    <div class="row m-0 p-0 text-center justify-content-around">
                        <div class="row col-4 m-0 p-0 fs-3" v-if="sessionStore.userData.permissons.includes('Préstamos')">
                            <div class="w-100 hover-bigger text-center m-0 p-0">
                                <router-link :to="{name:'add_loan', params: {id: loan.loan_id}}">
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