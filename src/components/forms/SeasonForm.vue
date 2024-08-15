<script setup>
import { ref, onMounted } from 'vue'

import FormValidator from '@/utils/FormValidator'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useSeasonStore from '@/stores/seasons'


const utilsStore = useUtilsStore()
const seasonStore = useSeasonStore()

const mounted = ref(false)
const formErrors = ref([])
const today = ref(new Date())

const seasonName = ref('')
const seasonDate = ref('')

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-3'
const labelStyle = 'text-center text-green text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const emits = defineEmits(['formOk'])
const props = defineProps({
    'targetSeason': {
        type: Object,
        default: {}
    }
})

onMounted(async () => {
    OnAppearAnimation('hide-up')

    if(Object.keys(props.targetSeason).length !== 0){
        seasonName.value = props.targetSeason['name']       
        seasonDate.value = props.targetSeason['date']  
    }
    else{
        var year = today.value.getFullYear()
        var month = today.value.getMonth() + 1
        if(month < 10) month = '0' + month
        var day = today.value.getDate()
        if(day < 10) day = '0' + day
        today.value = year + '-' + month + '-' + day

        const seasonDateInput = document.getElementById('date')
        seasonDateInput.max = today.value
    }
    
    mounted.value = true    
})

async function ValidateForm() {
    const validator = new FormValidator()
    formErrors.value = [] 
    const validationStructure = {
        'name':{ 
            'min': 1, 
            'max': 10, 
            'required': true, 
            'value': seasonName.value 
        },
        'date':{
            'min': 8, 
            'max': 10, 
            'required': true, 
            'value': seasonDate.value 
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
        if(Object.keys(props.targetSeason).length === 0){
            // Creating the season
            const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar este nueva temporada?', 'question')
            if(confirmAction === false)
                return
            
            const cleanData = {
                'name': validationStructure['name']['value'],
                'date': validationStructure['date']['value'],
            }

            const created = await seasonStore.CreateSeason(cleanData)            
            if(created.success){
                utilsStore.ShowModal('Success', created.message, 'success')
                seasonName.value = ''
                seasonDate.value = ''
                emits('formOk')
            }
            else
                utilsStore.ShowModal('Error', created.message, 'error')
        }
        else{
            // Renaming the season
            const confirmAction = await utilsStore.ConfirmModal('¿Desea renombrar esta temporada?', 'question')
            if(confirmAction === false)
                return

            let cleanData = {}

            if(props.targetSeason['name'] !== seasonName.value) cleanData['name'] = seasonName.value

            if(Object.keys(cleanData).length === 0)
                utilsStore.ShowModal('Info', 'No se realizaron cambios', 'info')
            else{
                const updated = await seasonStore.RenameSeason(props.targetSeason['id'], cleanData)
                if (updated.success){
                    emits('formOk')
                    utilsStore.ShowModal('Success', updated.message, 'success')
                }
                else
                    utilsStore.ShowModal('Error', updated.message, 'error')
            }
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
                            <label :class="labelStyle" for="name"><strong>Nombre</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12 col-lg-4">
                                <input type="text" class="myInput" maxlength="10" id="name" autofocus v-model="seasonName">
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="date"><strong>Fecha</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-4 m-0 p-0">
                                    <input 
                                    v-if="Object.keys(props.targetSeason).length === 0"
                                    class="col-12 myInput" 
                                    type="date" 
                                    id="date"
                                    name="date" 
                                    value="" 
                                    v-model="seasonDate" 
                                    >
                                    <span v-else class="text-center text-lg-start text-white">
                                        {{ props.targetSeason.date }}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
        
                    <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                        <div class="row m-0 p-0 col-12 justify-content-center">
                            <button class="col-6 col-lg-3 myBtn green-btn shadowed-l h3">
                                {{ Object.keys(props.targetSeason).length === 0 ? 'Registrar ' : 'Modificar ' }}
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