<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';
import useSessionStore from '@/stores/session';

import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()
const sessionStore = useSessionStore()

const props = defineProps({
    players: {type: Array, default: []}
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
                    <th class="text-center fw-normal bg-black border-green">Nombre</th>
                    <th class="text-center fw-normal bg-black border-green">Puntos totales</th>
                    <th class="text-center fw-normal bg-black border-green">Torneos participados</th>
                    <th class="text-center fw-normal bg-black border-green">Victorias</th>
                    <th class="text-center fw-normal bg-black border-green">Ver</th>
                </tr>
                </thead>
            <tbody class="fs-4">
                <tr 
                class="text-white"
                v-for="player in props.players"
                :key="player.id">
                    <td class="border-green text-center">{{ player.name }}</td>
                    <td class="border-green text-center">{{ player.points === null ? 0 : player.points }}</td>
                    <td class="border-green text-center">{{ player.tournaments === null ? 0 : player.tournaments }}</td>
                    <td class="border-green text-center">{{ player.wins === null ? 0 : player.wins }}</td>
                    <td class="border-green">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-6 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <router-link :to="{name:'see_player', params: {id: player.id}}">
                                        <i class="text-white bi bi-eye text-center m-0 p-0"></i>
                                    </router-link>
                                    
                                </div>
                            </div>

                            <template v-if="sessionStore.authenticated">
                                <div class="row col-6 m-0 p-1 col-3 fs-2" v-if="sessionStore.userData.permissons.includes('Jugadores')">
                                    <div class="w-100 hover-bigger text-center m-0 p-0">
                                        <router-link :to="{name:'add_player', params: {id: player.id}}">
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