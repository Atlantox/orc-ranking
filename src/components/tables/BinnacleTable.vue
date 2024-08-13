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
  const spinIcon = document.getElementById('spin-icon')
  if (spinIcon !== null){
      spinIcon.classList.remove('spin-on')
      void spinIcon.offsetWidth
      spinIcon.classList.add('spin-on')
  }
  emit('ResetBinnacle')
})

</script>

<template>
    <div class="w-100 m-0 p-0 hide-up animated-1 text-white">
      <div class="row w-100 m-0 p-0 fs-5 p-3">
        <h3 class="w-100 text-white">
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
          <span class="w-auto shadowed-l bg-black p-2 text-center rounded">
            <i class="fa fa-rotate-left fs-1 my-auto text-green align-middle" id="spin-icon"></i>
          </span>
        </div>
      </div>
        <table class="w-100 h6 m-0 text-white" id="normal-dt">
            <thead>
            <tr class="text-white">
                <th class="text-center orc-font fs-4 fw-normal bg-black border-green">Usuario</th>
                <th class="text-center orc-font fs-4 fw-normal bg-black border-green">Acción</th>
                <th class="text-center orc-font fs-4 fw-normal bg-black border-green">IP</th>
                <th class="text-center orc-font fs-4 fw-normal bg-black border-green">Fecha</th>
            </tr>
            </thead>
            <tbody>
            <tr 
            v-for="binnacle in props.binnacle"
            :key="binnacle.id"
            class="fs-4"
            >
                <td class="border-green text-center">{{ binnacle.nickname }}</td>
                <td class="border-green">{{ binnacle.action }}</td>
                <td class="border-green text-center">{{ binnacle.ip_address }}</td>
                <td class="border-green text-center">{{ new Date(binnacle.created_at).toLocaleDateString('es-VE', { hour: '2-digit', minute: '2-digit', timeZone: 'America/Caracas'}) }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>