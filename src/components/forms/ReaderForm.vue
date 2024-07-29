<script setup>
import { ref, onMounted } from 'vue'

import FormValidator from '@/utils/FormValidator'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useReaderStore from '@/stores/readers'
import useLoanStore from '@/stores/loans'
import useSessionStore from '@/stores/session'

import LoanTable from '../tables/LoanTable.vue'


const utilsStore = useUtilsStore()
const readerStore = useReaderStore()
const loanStore = useLoanStore()
const sessionStore = useSessionStore()

const today = ref(new Date())

const mounted = ref(false)
const formErrors = ref([])

const readerCedula = ref('')
const readerNames = ref('')
const readerSurnames = ref('')
const readerPhone = ref('')
const readerGender = ref('')
const readerBirthdate = ref('')
const readerIsTeacher = ref([])

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-3'
const labelStyle = 'text-center text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const props = defineProps({
    'targetReader': {type: Object, default: {}}
})

const emits = defineEmits(['formOk'])

onMounted(async () => {
    var year = today.value.getFullYear() - 10
    var month = today.value.getMonth() + 1
    if(month < 10) month = '0' + month
    var day = today.value.getDate()
    if(day < 10) day = '0' + day
    today.value = year + '-' + month + '-' + day

    const birthdateInput = document.getElementById('birthdate')
    birthdateInput.max = today.value
    OnAppearAnimation('hide-up')
    if(Object.keys(props.targetReader).length !== 0){
        await loanStore.FetchLoanOfReaderId(props.targetReader.id)
        readerCedula.value = props.targetReader.cedula
        readerNames.value = props.targetReader.names
        readerSurnames.value = props.targetReader.surnames
        readerPhone.value = props.targetReader.phone
        readerGender.value = props.targetReader.gender
        if(props.targetReader.is_teacher === 0)
            readerIsTeacher.value = []
        else
            readerIsTeacher.value = [1]

        const myDate = new Date(props.targetReader.birthdate)
        
        var year = myDate.getFullYear()
        var month = myDate.getMonth() + 1
        if(month < 10) month = '0' + month
        var day = myDate.getDate() + 1
        if(day < 10) day = '0' + day
        
        readerBirthdate.value = year + '-' + month + '-' + day
    }
    mounted.value = true
})


const ValidateForm = (async (e) => {
    const validator = new FormValidator()

    formErrors.value = [] 
    const validationStructure = {
        'cedula':{ 
            'min': 7,
            'max': 11, 
            'required': true, 
            'value': readerCedula.value 
        },
        'names':{
            'min': 2, 
            'max': 60, 
            'required': true, 
            'value': readerNames.value 
        },
        'surnames':{
            'min': 2, 
            'max': 60, 
            'required': true, 
            'value': readerSurnames.value 
        },
        'birthdate':{
            'min': 8, 
            'max': 10, 
            'required': true, 
            'value': readerBirthdate.value 
        },
        'phone':{
            'min': 7,
            'max': 15, 
            'required': true, 
            'value': readerPhone.value 
        }
    }    

    const emptyFields = validator.FieldsAreEmpty(validationStructure)
    if(emptyFields !== false){
        // uno o más campos están vacíos
        formErrors.value = emptyFields
    }

    const lengthOK = validator.FieldsMeetsLength(validationStructure)
    if (lengthOK !== true)
        formErrors.value = formErrors.value.concat(lengthOK)

    if(!['M', 'F'].includes(readerGender.value)){
        formErrors.value.push('El campo género es requerido')
    }

    if(readerIsTeacher.value.length === 0)
        readerIsTeacher.value = ['0']
    else
        readerIsTeacher.value = ['1']

    if(!['0', '1'].includes(readerIsTeacher.value[0])){
        formErrors.value.push('El campo "es docente" debe ser 1 o 0')
    }

    if(new Date(readerBirthdate.value) >= new Date()){
        formErrors.value.push('El cumpleaños debe ser anterior a la fecha actual')
    }    



    if(formErrors.value.length === 0){        
        if(Object.keys(props.targetReader).length === 0){
            // Creating the reader
            const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar este nuevo lector?', 'question')
            if(confirmAction === false)
                return

            const cleanReaderData = {
                'cedula': String(validationStructure['cedula']['value']),
                'names': validationStructure['names']['value'],
                'surnames': validationStructure['surnames']['value'],
                'phone':validationStructure['phone']['value'],
                'gender': readerGender.value,
                'birthdate': validationStructure['birthdate']['value'],
                'is_teacher': readerIsTeacher.value[0],
            }

            const created = await readerStore.CreateReader(cleanReaderData)            
            if(created.success){
                emits('formOk')
                utilsStore.ShowModal('Success', created.message, 'success')
                readerCedula.value = ''
                readerNames.value = ''
                readerSurnames.value = ''
                readerPhone.value = ''
                readerGender.value = ''
                readerBirthdate.value = ''
                readerIsTeacher.value = []
            }
            else
                utilsStore.ShowModal('Error', created.message, 'error')
        }
        else{
            // Updating the reader
            const confirmAction = await utilsStore.ConfirmModal('¿Desea editar este lector?', 'question')
            if(confirmAction === false)
                return

            let cleanReaderData = {}

            if(props.targetReader['cedula'] !== String(readerCedula.value)) cleanReaderData['cedula'] = String(readerCedula.value)
            if(props.targetReader['names'] !== readerNames.value) cleanReaderData['names'] = readerNames.value
            if(props.targetReader['surnames'] !== readerSurnames.value) cleanReaderData['surnames'] = readerSurnames.value
            if(props.targetReader['phone'] !== readerPhone.value) cleanReaderData['phone'] = readerPhone.value
            if(props.targetReader['gender'] !== readerGender.value) cleanReaderData['gender'] = readerGender.value
            if(props.targetReader['birthdate'] !== readerBirthdate.value) cleanReaderData['birthdate'] = readerBirthdate.value
            if(props.targetReader['is_teacher'] !== parseInt(readerIsTeacher.value[0])) cleanReaderData['is_teacher'] = readerIsTeacher.value[0]

            if(Object.keys(cleanReaderData).length === 0)
                utilsStore.ShowModal('Info', 'No se realizaron cambios', 'info')
            else{
                const updated = await readerStore.UpdateReader(props.targetReader['id'], cleanReaderData)
                if (updated.success){
                    emits('formOk')
                    utilsStore.ShowModal('Success', updated.message, 'success')
                }
                else
                    utilsStore.ShowModal('Error', updated.message, 'error')            
            }
        }          
    }    


})
</script>

<template>
    <form class="row m-0 p-0 justify-content-around align-items-start" @submit.prevent="ValidateForm">
        <template v-if="mounted.value === false">
            <LoadingGadget/>
        </template>
        <template v-else>
            <div class="col-12 row p-4 pt-5 fs-4 justify-content-around hide-up animated-1">
                <div class="col-12 col-lg-10 p-2 row myForm shadowed-l rounded lb-bg-terciary-ul justify-content-center">        
                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="cedula"><strong>Cédula</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-10 col-lg-5">
                                <input type="number" class="myInput" maxlength="11" id="cedula" autofocus v-model="readerCedula">
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="names"><strong>Nombres</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-10 col-lg-7">
                                <input type="text" class="myInput" maxlength="60" id="names" v-model="readerNames">
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="surnames"><strong>Apellidos</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-10 col-lg-7">
                                <input type="text" class="myInput" maxlength="60" id="surnames" v-model="readerSurnames">
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="phone"><strong>Teléfono</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-10 col-lg-5">
                                <input type="text" class="myInput" minlength="10" maxlength="15" id="phone" v-model="readerPhone">
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="gender"><strong>Género</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-3 m-0 p-0 my-1">
                                    <label class="col-6 text-end" for="gender-m">M</label>
                                    <input class="col-1 my-auto" type="radio" id="gender-m" name="gender" value="M" v-model="readerGender">
                                </div>
                                <div class="row col-12 col-lg-3 m-0 p-0 my-1">
                                    <label class="col-6 text-end" for="gender-f">F</label>
                                    <input class="col-1 my-auto" type="radio" id="gender-f" name="gender" value="F" v-model="readerGender">
                                </div>
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="birthdate"><strong>Fecha de nacimiento</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                                    <input class="col-12 myInput" type="date" id="birthdate" name="birthdate" value="" v-model="readerBirthdate">
                                </div>
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="teacher"><strong>Es docente</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                                    <input class="col-1 mx-auto mx-lg-0" type="checkbox" id="teacher" name="teacher" value="1" v-model="readerIsTeacher">
                                </div>
                            </div>
                        </div>
                    </div>       

                    <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                        <div class="row m-0 p-0 col-12 justify-content-center">
                            <button class="col-6 col-lg-3 myBtn terciary-btn shadowed-l h3">
                                {{ Object.keys(props.targetReader).length === 0 ? 'Registrar ' : 'Modificar ' }}
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

                <template v-if="sessionStore.userData.permissons.includes('Préstamos')">
                    <!-- Reader's loans -->
                    <div v-if="Object.keys(props.targetReader).length !== 0 && mounted === true" class="col-12 col-lg-10 p-2 row shadowed-l rounded lb-bg-terciary-ul justify-content-center mt-5">
                        <h2 class="w-100 text-center h1 my-3 fw-bold">
                            Préstamos de {{ props.targetReader.names }}
                        </h2>
                        <div class="w-100 p-2 fs-6">
                            <LoanTable
                            :loans="loanStore.loans"
                            />
                        </div>
                    </div>
                </template>
            </div>
        </template>
    </form>
</template>

<style scoped>
h1{
  font-size:50px !important;
}
</style>