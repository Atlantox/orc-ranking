<script setup>
import { ref, onMounted } from 'vue'

import { useRouter } from 'vue-router'

import FormValidator from '@/utils/FormValidator'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useTournamentStore from '@/stores/tournaments'
import usePlayerStore from '@/stores/players'
import useFormatStore from '@/stores/formats'
import useDeckStore from '@/stores/decks'

const utilsStore = useUtilsStore()
const router = useRouter()
const tournamentStore = useTournamentStore()
const playerStore = usePlayerStore()
const formatStore = useFormatStore()
const deckStore = useDeckStore()

const mounted = ref(false)
const formErrors = ref([])
const today = ref(new Date())
const minPlayers = 4

const tournamentDate = ref('')
const tournamentFormat = ref('')
const tournamentObservation = ref('')
const tournamentParticipants = ref([])
const participantsIds = ref(0)

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
    await deckStore.FetchDecks()

    if(Object.keys(props.targetTournament).length !== 0){
        tournamentParticipants.value = props.targetTournament.data.results       
    }
    else{
        var year = today.value.getFullYear()
        var month = today.value.getMonth() + 1
        if(month < 10) month = '0' + month
        var day = today.value.getDate()
        if(day < 10) day = '0' + day
        today.value = year + '-' + month + '-' + day

        const deliverDateInput = document.getElementById('date')
        deliverDateInput.max = today.value
    }
    
    mounted.value = true    
})

async function ValidateForm() {
    const validator = new FormValidator()
    formErrors.value = [] 
    const validationStructure = {
        'date':{
            'min': 8, 
            'max': 10, 
            'required': true, 
            'value': tournamentDate.value 
        },
        'format':{
            'min': 2, 
            'max': 100, 
            'required': true, 
            'value': tournamentFormat.value 
        },
        'observation':{
            'min': 0, 
            'max': 200, 
            'required': false, 
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

    const filledParticipants = []
    // Deleting empty participants
    for(let i = 0; i < tournamentParticipants.value.length; i++){
        const currentParticipant = tournamentParticipants.value[i]
        if(
            currentParticipant.player.value !== '' &&
            currentParticipant.deck !== '' &&
            currentParticipant.wins !== ''
        )
            filledParticipants.push(currentParticipant)
    }

    tournamentParticipants.value = filledParticipants

    // Validating participants
    const participantList = []
    const deckList = []
    const cleanParticipants = []

    if(tournamentParticipants.value.length < minPlayers)
        formErrors.value.push('El mínimo de participantes permitidos es 4')

    tournamentParticipants.value.forEach((participant) => {
        var error = false
        if(participantList.includes(participant.player)){
            formErrors.value.push('Algún participante está repetido ' + participant.player)
            error = true
        }
        else
            participantList.push(participant.player)

        if(deckList.includes(participant.deck)){
            formErrors.value.push('Algún deck está repetido ' + participant.deck)
            error = true
        }
        else
            deckList.push(participant.deck)

        if(error === false){
            cleanParticipants.push({
                "player": participant.player,
                "deck": participant.deck,
                "wins": participant.wins,
                "winner": participant.winner === true ? 1 : 0,
            })
        }
    })

    if(formErrors.value.length === 0){        
        if(Object.keys(props.targetTournament).length === 0){
            // Creating the tournament
            const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar este nuevo torneo?', 'question')
            if(confirmAction === false)
                return
            
            const cleanData = {
                'date': validationStructure['date']['value'],
                'format': tournamentFormat.value,
                'observation': validationStructure['observation']['value'],
                'participants': cleanParticipants
            }

            const created = await tournamentStore.CreateTournament(cleanData)            
            if(created.success){
                utilsStore.ShowModal('Success', created.message, 'success')
                emits('formOk')

                tournamentObservation.value = ''
                tournamentDate.value = ''
                tournamentFormat.value = ''
                tournamentParticipants.value = []
            }
            else
                utilsStore.ShowModal('Error', created.message, 'error')
        }  
    }    
}


const AddPartcipant = (async () => {
    const newParticipant = {
        id: participantsIds.value,
        player: ref(''),
        deck: ref(''),
        wins: ref(''),
        winner: ref(false)
    }
    participantsIds.value++
    tournamentParticipants.value.push(newParticipant)

    await new Promise(r => setTimeout(r, 50));
    const playerId = 'player-' + newParticipant.id
    const deckId = 'deck-' + newParticipant.id
    $('#' + playerId).select2() 
    $('#' + deckId).select2() 


    $('#' + playerId).on('select2:select', function (e) { 
        newParticipant.player.value = e.target.value;
        document.getElementById('select2-' + playerId + '-container').classList.remove('border-red') 

    });

    $('#' + deckId).on('select2:select', function (e) { 
        newParticipant.deck.value = e.target.value;
        document.getElementById('select2-' + deckId + '-container').classList.remove('border-red') 

    });
})

const DeleteParticipant = ((id) =>{
    var index = 0

    for(let i = 0; i < tournamentParticipants.value.length; i++){
        if(tournamentParticipants.value[i].id === id)
            break
        index++
    }
    
    tournamentParticipants.value.splice(index, 1)
})

const DeactivateTournament = (async () => {
    const confirmAction = await utilsStore.ConfirmModal('¿Desea desactivar este torneo? No podrá activarlo nuevamente', 'question')
    if(confirmAction === false)
        return

    const deactivated = await tournamentStore.DeactivateTournament(props.targetTournament.data.id)
    if(deactivated.success){
        utilsStore.ShowModal('Success', deactivated.message, 'success')
        router.push({name: 'dashboard'})
    }
    else
        utilsStore.ShowModal('Error', deactivated.message, 'error')

})
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
                            <label :class="labelStyle" for="date"><strong>Fecha</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-4 m-0 p-0">
                                    <input 
                                    v-if="Object.keys(props.targetTournament).length === 0"
                                    class="col-12 myInput" 
                                    type="date" 
                                    id="date"
                                    name="date" 
                                    value="" 
                                    v-model="tournamentDate" 
                                    >
                                    <span v-else class="text-center text-lg-start text-white">
                                        {{ props.targetTournament.data.date }}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="format"><strong>Formato</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-8 col-lg-4">
                                <select 
                                v-if="Object.keys(props.targetTournament).length === 0"
                                class="myInput" 
                                id="format" 
                                v-model="tournamentFormat"
                                >
                                    <option value="">&nbsp;</option>
                                    <template
                                    v-for="format in formatStore.formats"
                                    :key="format.id">
                                        <option class="fw-normal" :value="format.name" :selected="tournamentFormat == format.name">
                                            {{ format.name }}
                                        </option>                                    
                                    </template>
                                </select>
                                <span v-else class="text-center text-lg-start text-white">
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
                            <div class="row col-12 col-lg-8">
                                <textarea
                                v-if="Object.keys(props.targetTournament).length === 0"
                                class="myInput" 
                                maxlength="200" 
                                cols="30" 
                                rows="2"
                                id="observation"  
                                v-model="tournamentObservation" 
                                ></textarea> 
                                <span v-else class="text-center text-lg-start text-white">
                                    {{ props.targetTournament.data.observation === '' ? 'Ninguna' : props.targetTournament.data.observation }}
                                </span>
                            </div>
                        </div>
                    </div>

                    <div v-if="Object.keys(props.targetTournament).length !== 0" :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="observation">Ativo</label>
                        </div>
                        <div :class="inputContainerStyle">
                            <i :class="'text-center text-lg-start fa fa-circle text-' + (props.targetTournament.data.active === 0 ? 'danger' : 'green')"></i>
                        </div>
                    </div>

                    <div v-if="Object.keys(props.targetTournament).length === 0" :class="formRowStyle">
                        <table  class="col-12 col-lg-10 text-white mt-5">
                            <thead class="text-center">
                                <tr>
                                    <th class="p-1 border-green h1 text-white bg-black" 
                                    :colspan="Object.keys(props.targetTournament).length === 0 ? 5 : 4">Participantes</th>
                                </tr>
                                <tr>
                                    <th class="p-1 border-green bg-dark-grey fw-normal" style="width:25%">Jugador</th>
                                    <th class="p-1 border-green bg-dark-grey fw-normal" style="width:45%">Deck</th>
                                    <th class="p-1 border-green bg-dark-grey fw-normal" style="width:10%">Puntos/Victorias</th>
                                    <th class="p-1 border-green bg-dark-grey fw-normal" style="width:10%">Ganador</th>
                                    <th v-if="Object.keys(props.targetTournament).length === 0" class="p-1 border-green bg-dark-grey" style="width:10%">
                                        Borrar
                                    </th>
                                    
                                </tr>
                            </thead>
                            <tbody>
                                <tr
                                v-for="participant, index in tournamentParticipants"
                                :key="index"
                                >
                                    <td class="p-1 border-green">
                                        <div class="w-100 px-2">
                                            <select class="select2" :id="'player-' + participant.id" v-model="participant.player">
                                                <option value=""></option>
                                                <option 
                                                v-for="player in playerStore.players"
                                                :key="player.id"
                                                class="fw-normal" 
                                                :value="player.id" 
                                                >
                                                    {{ player.name }}
                                                </option> 
                                            </select>
                                        </div>
                                    </td>
                                    <td class="p-1 border-green">
                                        <div class="w-100 px-2">
                                            <select class="w-100 select2" :id="'deck-' + participant.id" v-model="participant.deck">
                                                <option value=""></option>
                                                <option 
                                                v-for="deck in deckStore.decks"
                                                :key="deck.id"
                                                class="fw-normal" 
                                                :value="deck.id" 
                                                >
                                                    {{ deck.name }}
                                                </option> 
                                            </select>
                                        </div>
                                    </td>
                                    <td class="p-1 border-green">
                                        <div class="w-100 px-2 d-flex justify-content-center">
                                            <input class="col-6" type="text" onkeypress="return ((event.charCode >= 48 && event.charCode <= 57) || event.charCode === 46)" v-model="participant.wins">
                                        </div>
                                    </td>
                                    <td class="p-1 border-green">
                                        <input class="mx-auto" type="checkbox" v-model="participant.winner">
                                    </td>
                                    <td v-if="Object.keys(props.targetTournament).length === 0" class="p-3 border-green">
                                        <button class="col-12 myBtn green-btn p-1" @click.prevent="DeleteParticipant(participant.id)">
                                            <i class="fa fa-trash text-danger fs-3"></i>
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        
                        <div :colspan="Object.keys(props.targetTournament).length === 0 ? 5 : 4">
                            <div class="row m-0 p-3 justify-content-center">
                                <button class="col-8 col-lg-3 myBtn green-btn shadowed-l" @click.prevent="AddPartcipant" title="Agregar participante">
                                    <i class="fa fa-plus text-green fs-1"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div v-else :class="formRowStyle">
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

                    <div v-if="Object.keys(props.targetTournament).length !== 0" class="row m-0 p-0 justify-content-center my-2 mt-5">
                        <div v-if="props.targetTournament.data.active === 1" class="row m-0 p-0 col-12 justify-content-center">
                            <button class="col-6 col-lg-3 myBtn green-btn shadowed-l h3 border-danger" @click.prevent="DeactivateTournament" style="color:red!important">
                                Desactivar torneo
                            </button>
                        </div>
                    </div>        
                    <div v-else class="row m-0 p-0 justify-content-center my-2 mt-5">
                        <div class="row m-0 p-0 col-12 justify-content-center">
                            <button class="col-6 col-lg-3 myBtn green-btn shadowed-l h3">
                                Registrar
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