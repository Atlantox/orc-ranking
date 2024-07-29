<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';
import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()

const props = defineProps({
    readers: {type: Array, default: []}
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
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Nombre</th>
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Género</th>
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Teléfono</th>
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Es docente</th>
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Acción</th>
                </tr>
            </thead>
            <tbody>
                <tr 
                v-for="reader in props.readers"
                :key="reader.id">
                    <td class="border-1"><strong>({{ reader.cedula }})</strong> {{ reader.names + ' ' + reader.surnames }}</td>
                    <td class="border-1 text-center fs-5">{{ reader.gender }}</td>
                    <td class="border-1">{{ reader.phone }}</td>
                    <td class="border-1">
                        
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-12 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <i :class="'text-black fs-1 bi bi-' + (reader.is_teacher === 0 ? 'x text-danger' : 'check text-success')"></i>
                                </div>
                            </div>
                        </div>
                    </td>
                    <td class="border-1">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-12 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <router-link :to="{name:'add_reader', params: {id: reader.id}}">
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