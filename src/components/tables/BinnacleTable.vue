<script setup>
import { ref, onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';

import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()

const initialDate = ref()
const finalDate = ref()
const emit = defineEmits(['ChangeDate', 'ResetBinnacle'])

const props = defineProps({
    binnacle: {type: Array, default: []}
})

onMounted(() => {
  utilsStore.InitializeDatatables()
  OnAppearAnimation('hide-up')
})

const ChangeDate = (() => {
    if((initialDate.value !== undefined && finalDate.value !== undefined))
        emit('ChangeDate', {'initial_date': initialDate.value, 'final_date': finalDate.value})
})

const ResetBinnacle = (() => {
    emit('ResetBinnacle')
})

</script>

<template>
    <div class="w-100 m-0 p-0 hide-up animated-1">
        <div class="row w-100 m-0 p-0 fs-5 p-3">
        <h3 class="w-100">
          Filtrar por fecha
        </h3>
        <div class="col-6 col-lg-2 fs-6">
          Inicio: 
          <input class="col-12 myInput" type="date" id="initial_date" name="initial_date" v-model="initialDate" @change="ChangeDate">
        </div>

        <div class="col-6 col-lg-2 fs-6">
          Fin:
          <input class="col-12 myInput" type="date" id="final_date" name="final_date" v-model="finalDate" @change="ChangeDate">
        </div>
        <div class="col-12 col-lg-1 con-container d-flex justify-content-center align-items-center" @click="ResetBinnacle">
            <i class="fa fa-rotate-left fs-1 my-auto text-white align-middle shadowed-l lb-bg-terciary-l p-2 rounded" id="spin-icon"></i>
        </div>
      </div>
        <table class="w-100 h6 m-0" id="normal-dt">
            <thead>
            <tr class="text-white">
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Usuario</th>
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Acción</th>
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">IP</th>
                <th class="text-center lb-bg-terciary border-1 border-white fs-4">Fecha</th>
            </tr>
            </thead>
            <tbody>
            <tr 
            v-for="binnacle in props.binnacle"
            :key="binnacle.id">
                <td class="border-1 text-center">{{ binnacle.nickname }}</td>
                <td class="border-1">{{ binnacle.action }}</td>
                <td class="border-1 text-center">{{ binnacle.ip_address }}</td>
                <td class="border-1 text-center">{{ new Date(binnacle.created_at).toLocaleDateString('es-VE', { hour: '2-digit', minute: '2-digit', timeZone: 'America/Caracas'}) }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>