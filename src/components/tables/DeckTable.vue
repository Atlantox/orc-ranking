<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';
import useSessionStore from '@/stores/session';

import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()
const sessionStore = useSessionStore()

const props = defineProps({
    decks: {type: Array, default: []}
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
                    <th class="text-center fw-normal bg-black border-green">Colores</th>
                    <th class="text-center fw-normal bg-black border-green">Participaciones</th>
                    <th class="text-center fw-normal bg-black border-green">Victorias</th>
                    <th class="text-center fw-normal bg-black border-green">Ver</th>
                </tr>
                </thead>
            <tbody class="fs-5">
                <tr 
                class="text-white"
                v-for="deck in props.decks"
                :key="deck.id">
                    <td class="border-green text-center">{{ deck.name }}</td>
                    <td class="border-green text-center fs-4">
                        <span v-for="color, id in deck.colors" :key="id" :class="'text-' + color">
                            {{ color }} &nbsp;
                        </span>
                    </td>
                    <td class="border-green text-center">{{ deck.participations }}</td>
                    <td class="border-green text-center">{{ deck.wins }}</td>
                    <td class="border-green">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-6 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <router-link :to="{name:'', params: {id: deck.id}}">
                                        <i class="text-white bi bi-eye text-center m-0 p-0"></i>
                                    </router-link>
                                </div>
                            </div>

                            <template v-if="sessionStore.authenticated">
                                <div class="row col-6 m-0 p-1 col-3 fs-2" v-if="sessionStore.userData.permissons.includes('Mazos')">
                                    <div class="w-100 hover-bigger text-center m-0 p-0">
                                        <router-link :to="{name:'add_deck', params: {id: deck.id}}">
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