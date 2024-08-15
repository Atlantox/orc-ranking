<script setup>
import {  onMounted } from 'vue'

import OnAppearAnimation from '@/utils/ElegantDisplayer'

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-6'
const labelStyle = 'text-center text-green text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-6 justify-content-center justify-content-md-start'

const props = defineProps({
    'targetTournament': {
        type: Object,
        default: {}
    }
})

onMounted(async () => {
    OnAppearAnimation('hide-up') 
})

</script>

<template>
    <div class="row m-0 p-0 justify-content-around align-items-start" @submit.prevent="ValidateForm">
        <div class="col-12 row p-4 pt-5 fs-4 justify-content-around hide-up animated-1">
            <div class="col-12 col-lg-10 p-2 row myForm shadowed-l rounded bg-grey justify-content-center">
                <div class="row col-12 m-0 p-0 justify-content-center">
                    <div class="row col-12 col-lg-4 m-0 p-0 justify-content-center">
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="date">Fecha</label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
                                    <div class="row col-12 m-0 p-0">
                                        <span class="text-center text-lg-start text-white">
                                            {{ props.targetTournament.data.date }}
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="format">Formato</label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
                                    <span class="text-center text-lg-start text-white">
                                        {{ props.targetTournament.data.format }}
                                    </span>
                                </div>
                            </div>
                        </div>
        
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="observation">Observación</label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
                                    <span class="text-center text-lg-start text-white">
                                        {{ props.targetTournament.data.observation === '' ? 'Ninguna' : props.targetTournament.data.observation }}
                                    </span>
                                </div>
                            </div>
                        </div>
        
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="observation">Ativo</label>
                            </div>
                            <div :class="inputContainerStyle">
                                <i :class="'text-center text-lg-start fa fa-circle text-' + (props.targetTournament.data.active === 0 ? 'danger' : 'green')"></i>
                            </div>
                        </div>                        
                    </div>

                    <div class="row col-12 col-lg-4 m-0 p-0 justify-content-center">
                        <div :class="formRowStyle">
                        <h3 class="w-100 m-0 p-0 text-center text-green">
                            Presencia de color
                        </h3>
                        <ul class="w-100 list-unstyled m-0 p-0 text-white text-center">
                            <li 
                            v-for="color in props.targetTournament.colors"
                            :key="color.name"
                            class=""
                            >
                            <i :class="'fa fa-circle text-' + color.color"></i>&nbsp;{{ color.percent }}% ({{ color.quantity }})
                            </li>
                        </ul>
                    </div>
                    </div>
                </div>                

                <div :class="formRowStyle">
                    <table  class="col-12 col-lg-10 text-white mt-5">
                        <thead class="text-center">
                            <tr>
                                <th class="p-1 border-green h1 text-white bg-black" colspan="4">Participantes</th>
                            </tr>
                            <tr>
                                <th class="p-1 border-green bg-dark-grey">Jugador</th>
                                <th class="p-1 border-green bg-dark-grey">Deck</th>
                                <th class="p-1 border-green bg-dark-grey">Puntos/Victorias</th>
                                <th class="p-1 border-green bg-dark-grey">Ganador</th>                                    
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                            v-for="participant, index in props.targetTournament.results"
                            :key="index"
                            class="text-center"
                            >
                                <td class="p-1 border-green">
                                    <div class="w-100 px-2">
                                        {{ participant.player }}
                                    </div>
                                </td>
                                <td class="p-1 border-green">
                                    <div class="w-100 px-2">
                                        {{ participant.deck }}
                                    </div>
                                </td>
                                <td class="p-1 border-green">
                                    <div class="w-100 px-2">
                                        {{ participant.wins }}
                                    </div>
                                </td>
                                <td class="p-1 border-green">
                                    <div class="w-100 px-2">
                                        <i :class="'fa fa-circle text-' + (participant.winner === 0 ? 'danger' : 'green')"></i>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>