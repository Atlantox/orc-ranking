<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';
import useSessionStore from '@/stores/session';

import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()
const sessionStore = useSessionStore()

const props = defineProps({
    results: {type: Array, default: []}
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
                    <th class="text-center fw-normal bg-black border-green">Fecha</th>
                    <th class="text-center fw-normal bg-black border-green">Jugador</th>
                    <th class="text-center fw-normal bg-black border-green">Mazo</th>
                    <th class="text-center fw-normal bg-black border-green">Puntos/Victorias</th>
                    <th class="text-center fw-normal bg-black border-green">Ganador</th>
                    <th class="text-center fw-normal bg-black border-green">Formato</th>
                    <th class="text-center fw-normal bg-black border-green">Observación</th>
                    <th class="text-center fw-normal bg-black border-green">Temporada</th>
                    <th v-if="sessionStore.authenticated" class="text-center fw-normal bg-black border-green">Activo</th>
                    <th class="text-center fw-normal bg-black border-green">Ver</th>
                </tr>
                </thead>
            <tbody class="fs-4">
                <tr 
                class="text-white"
                v-for="result in props.results"
                :key="result.id">
                    <td class="border-green text-center">{{ result.date }}</td>
                    <td class="border-green text-center">{{ result.player }}</td>
                    <td class="border-green text-center">{{ result.deck }}</td>
                    <td class="border-green text-center">{{ result.wins }}</td>
                    <td class="border-green text-center">
                        <i :class="'fa fa-circle text-' + (result.winner === 0 ? 'danger' : 'green')"></i>
                    </td>
                    <td class="border-green text-center">{{ result.format }}</td>
                    <td class="border-green text-center">{{ result.observation === '' ? 'Ninguna' : result.observation }}</td>
                    <td class="border-green text-center">{{ result.season }}</td>
                    <td v-if="sessionStore.authenticated" class="border-green text-center">
                        <i :class="'fa fa-circle text-' + (result.active === 0 ? 'danger' : 'green')"></i>
                    </td>
                    <td class="border-green">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-6 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <router-link :to="{name:'see_tournament', params: {id: result.id}}">
                                        <i class="text-white bi bi-eye text-center m-0 p-0"></i>
                                    </router-link>
                                    
                                </div>
                            </div>

                            <template v-if="sessionStore.authenticated">
                                <div class="row col-6 m-0 p-1 col-3 fs-2" v-if="sessionStore.userData.permissons.includes('Torneos')">
                                    <div class="w-100 hover-bigger text-center m-0 p-0">
                                        <router-link :to="{name:'add_tournament', params: {id: result.id}}">
                                            <i class="text-white bi bi-pencil text-center m-0 p-0"></i>
                                        </router-link>
                                        
                                    </div>
                                </div>
                            </template>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>