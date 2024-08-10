<script setup>
import { ref, onMounted } from 'vue'

import FormValidator from '@/utils/FormValidator'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useTournamentStore from '@/stores/tournaments'
import usePlayerStore from '@/stores/players'
import useFormatStore from '@/stores/formats'

const utilsStore = useUtilsStore()
const tournamentStore = useTournamentStore()
const playerStore = usePlayerStore()
const formatStore = useFormatStore()

const mounted = ref(false)
const formErrors = ref([])

const tournamentDate = ref('')
const tournamentFormat = ref('')
const tournamentObservation = ref('')
const tournamentParticipants = ref('')

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-3'
const labelStyle = 'text-center text-green text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const emits = defineEmits(['formOk'])
const props = defineProps({
    'targetTournament': {
        type: Object,
        default: {}
    }
})

onMounted(async () => {
    OnAppearAnimation('hide-up')
    await playerStore.FetchPlayers()
    await formatStore.FetchFormats()

    if(props.targetTournament !== undefined){
        tournamentObservation.value = props.targetTournament['name']         
    }
    
    mounted.value = true    
})

async function ValidateForm() {
    const validator = new FormValidator()
    formErrors.value = [] 
    const validationStructure = {
        'name':{ 
            'min': 2, 
            'max': 50, 
            'required': true, 
            'value': tournamentObservation.value 
        },
    }

    const emptyFields = validator.FieldsAreEmpty(validationStructure)
    if(emptyFields !== false){
        // uno o más campos están vacíos
        formErrors.value = emptyFields
    }

    const lengthOK = validator.FieldsMeetsLength(validationStructure)
    if (lengthOK !== true)
        formErrors.value = formErrors.value.concat(lengthOK)

    if(formErrors.value.length === 0){        
        if(Object.keys(props.targetTournament).length === 0){
            // Creating the tournament
            const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar este nuevo jugador?', 'question')
            if(confirmAction === false)
                return
            
            const cleanData = {
                'name': validationStructure['name']['value'],
            }

            const created = await tournamentStore.CreateTournament(cleanData)            
            if(created.success){
                utilsStore.ShowModal('Success', created.message, 'success')
                tournamentObservation.value = ''
                emits('formOk')
            }
            else
                utilsStore.ShowModal('Error', created.message, 'error')
        }  
    }    
}
</script>

<template>
    <form class="row m-0 p-0 justify-content-around align-items-start" @submit.prevent="ValidateForm">
        <template v-if="mounted.value === false">
            <LoadingGadget/>
        </template>
        <template v-else>
            <div class="col-12 row p-4 pt-5 fs-4 justify-content-around hide-up animated-1">
                <div class="col-12 col-lg-10 p-2 row myForm shadowed-l rounded bg-grey justify-content-center">
                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="deliver_date"><strong>Fecha</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-4 m-0 p-0">
                                    <input class="col-12 myInput" type="date" id="deliver_date" name="deliver_date" value="" v-model="tournamentDate" :disabled="Object.keys(props.targetTournament).length !== 0">
                                </div>
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="formats"><strong>Formato</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-8 col-lg-4">
                                <select class="myInput select2" id="formats" :v-model="tournamentFormat">
                                    <option value="">&nbsp;</option>
                                    <template
                                    v-for="format in formatStore.formats"
                                    :key="format.name">
                                        <option class="fw-normal" :value="format.name" :selected="tournamentFormat == format.name">
                                            {{ format.name }}
                                        </option>                                    
                                    </template>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="observation"><strong>Observación</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12 col-lg-8">
                                <textarea
                                class="myInput" 
                                maxlength="200" 
                                cols="30" 
                                rows="2"
                                id="observation"  
                                v-model="tournamentObservation" 
                                :disabled="Object.keys(props.targetTournament).length !== 0"></textarea> 
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <table class="col-12 col-lg-10 text-white mt-5">
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
                                <tr>
                                    <td class="p-1 border-green">
                                        <select name="" id=""></select>
                                    </td>
                                    <td class="p-1 border-green">
                                        <select name="" id=""></select>
                                    </td>
                                    <td class="p-1 border-green">
                                        <input type="number">
                                    </td>
                                    <td class="p-1 border-green">
                                        <input type="checkbox">
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
        
                    <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                        <div class="row m-0 p-0 col-12 justify-content-center">
                            <button class="col-6 col-lg-3 myBtn green-btn shadowed-l h3">
                                {{ Object.keys(props.targetTournament).length === 0 ? 'Registrar ' : 'Modificar ' }}
                            </button>
                        </div>
                    </div>
        
                    <div v-if="formErrors.length > 0" class="row m-0 p-0 justify-content-center my-2 mt-2">
                        <ul class="row m-0 p-0 col-12 justify-content-center list-unstyled text-center text-danger fs-5">
                            <li 
                            v-for="error, index in formErrors"
                            :key="index"
                            >
                                {{ error }}
                            </li>  
                        </ul>
                    </div>
    
                </div>

            </div>
        </template>

    </form>
</template>

<style scoped>
textarea{
    padding:5px;
}
</style>