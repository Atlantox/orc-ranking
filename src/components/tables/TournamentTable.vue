<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';
import useSessionStore from '@/stores/session';

import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()
const sessionStore = useSessionStore()

const props = defineProps({
    tournaments: {type: Array, default: []}
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
                    <th class="text-center fw-normal bg-black border-green">Formato</th>
                    <th class="text-center fw-normal bg-black border-green">Observación</th>
                    <th class="text-center fw-normal bg-black border-green">Participantes</th>
                    <th class="text-center fw-normal bg-black border-green">Ganador</th>
                    <th class="text-center fw-normal bg-black border-green">Ver</th>
                </tr>
                </thead>
            <tbody class="fs-5">
                <tr 
                class="text-white"
                v-for="tournament in props.tournaments"
                :key="tournament.id">
                    <td class="border-green text-center">{{ tournament.date }}</td>
                    <td class="border-green text-center">{{ tournament.format }}</td>
                    <td class="border-green text-center">{{ tournament.observation }}</td>
                    <td class="border-green text-center">{{ tournament.participants }}</td>
                    <td class="border-green text-center">{{ tournament.winner }}</td>
                    <td class="border-green">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-6 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <router-link :to="{name:'', params: {id: tournament.id}}">
                                        <i class="text-white bi bi-eye text-center m-0 p-0"></i>
                                    </router-link>
                                    
                                </div>
                            </div>

                            <template v-if="sessionStore.authenticated">
                                <div class="row col-6 m-0 p-1 col-3 fs-2" v-if="sessionStore.userData.permissons.includes('Jugadores')">
                                    <div class="w-100 hover-bigger text-center m-0 p-0">
                                        <router-link :to="{name:'', params: {id: tournament.id}}">
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