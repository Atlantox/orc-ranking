<script setup>
import { ref, onMounted } from 'vue'

import FormValidator from '@/utils/FormValidator'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useWarningStore from '@/stores/warnings'
import usePlayerStore from '@/stores/players'
import useSeasonStore from '@/stores/seasons'


const utilsStore = useUtilsStore()
const playerStore = usePlayerStore()
const seasonStore = useSeasonStore()
const warningStore = useWarningStore()

const mounted = ref(false)
const formErrors = ref([])
const today = ref(new Date())

const warningPlayer = ref('')
const warningDate = ref('')
const warningReason = ref('')
const warningSeason = ref('')

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-3'
const labelStyle = 'text-center text-green text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const emits = defineEmits(['formOk'])

onMounted(async () => {
    OnAppearAnimation('hide-up')    
    
    await playerStore.FetchPlayers()
    await seasonStore.FetchSeasons()

    mounted.value = true    

    var year = today.value.getFullYear()
    var month = today.value.getMonth() + 1
    if(month < 10) month = '0' + month
    var day = today.value.getDate()
    if(day < 10) day = '0' + day
    today.value = year + '-' + month + '-' + day

    const tournamentDateInput = document.getElementById('date')
    tournamentDateInput.max = today.value

    $('#player').select2(); $('#player').on('select2:select', function (e) { warningPlayer.value = e.target.value; });
    $('#season').select2(); $('#season').on('select2:select', function (e) { warningSeason.value = e.target.value; });
})

async function ValidateForm() {
    const validator = new FormValidator()
    formErrors.value = [] 
    const validationStructure = {
        'player':{ 
            'min': 1, 
            'max': 11, 
            'required': true, 
            'value': warningPlayer.value
        },
        'date':{ 
            'min': 8, 
            'max': 10, 
            'required': true, 
            'value': warningDate.value
        },
        'season':{ 
            'min': 1, 
            'max': 11, 
            'required': true, 
            'value': warningSeason.value
        },
        'reason':{ 
            'min': 1, 
            'max': 255, 
            'required': true, 
            'value': warningReason.value
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
        // Creating the warning
        const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar este nuevo warning?', 'question')
        if(confirmAction === false)
            return
        
        const cleanData = {
            'player': validationStructure['player']['value'],
            'date': validationStructure['date']['value'],
            'season': validationStructure['season']['value'],
            'reason': validationStructure['reason']['value'],
        }

        const created = await warningStore.CreateWarning(cleanData)            
        if(created.success){
            utilsStore.ShowModal('Success', created.message, 'success')
            warningPlayer.value = ''
            warningDate.value = ''
            warningReason.value = ''
            warningSeason.value = ''
            $('#player').val('')
            $('#player').trigger('change')
            $('#season').val('')
            $('#season').trigger('change')
            emits('formOk')
        }
        else
            utilsStore.ShowModal('Error', created.message, 'error')
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
                            <label :class="labelStyle" for="date"><strong>Fecha</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-4 m-0 p-0">
                                    <input 
                                    class="col-12 myInput" 
                                    type="date" 
                                    id="date"
                                    name="date" 
                                    value="" 
                                    v-model="warningDate" 
                                    >
                                </div>
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="player"><strong>Jugador</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-8 col-lg-4">
                                <select 
                                class="myInput" 
                                id="player" 
                                v-model="warningPlayer"
                                >
                                    <option value="">&nbsp;</option>
                                    <template
                                    v-for="player in playerStore.players"
                                    :key="player.id">
                                        <option class="fw-normal" :value="player.id">
                                            {{ player.name }}
                                        </option>                                    
                                    </template>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="season"><strong>Temporada</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-8 col-lg-4">
                                <select 
                                class="myInput" 
                                id="season" 
                                v-model="warningSeason"
                                >
                                    <option value="">&nbsp;</option>
                                    <template
                                    v-for="season in seasonStore.seasons"
                                    :key="season.id">
                                        <option class="fw-normal" :value="season.id">
                                            {{ season.name }}
                                        </option>                                    
                                    </template>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="reason">Razón</label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12 col-lg-8">
                                <textarea
                                class="myInput" 
                                maxlength="255" 
                                cols="30" 
                                rows="2"
                                id="reason"  
                                v-model="warningReason" 
                                ></textarea> 
                            </div>
                        </div>
                    </div>
        
                    <div class="row m-0 p-0 justify-content-center my-2 mt-5">
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