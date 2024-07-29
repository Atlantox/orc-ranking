<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

import FormValidator from '@/utils/FormValidator'

import ReaderForm from './ReaderForm.vue'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useLoanStore from '@/stores/loans'

import LargeModalGadget from '../myGadgets/LargeModalGadget.vue'

const utilsStore = useUtilsStore()
const loanStore = useLoanStore()
const router = useRouter()

const mounted = ref(false)
const formErrors = ref([])
const today = ref(new Date())

const loanReader = ref('')
const loanBook = ref('')
const loanObservation = ref('')
const loanDeliverDate = ref('')
const loanActive = ref('')

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-3'
const labelStyle = 'text-center text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const props = defineProps({
    'targetLoan': {type: Object, default: {}},
    'books': Array,
    'readers': Array,
})

const emit = defineEmits(['fetchAgain'])

onMounted(async () => {
    utilsStore.InitializeSelect2()
    OnAppearAnimation('hide-up')

    var year = today.value.getFullYear()
    var month = today.value.getMonth() + 1
    if(month < 10) month = '0' + month
    var day = today.value.getDate()
    if(day < 10) day = '0' + day
    today.value = year + '-' + month + '-' + day

    const deliverDateInput = document.getElementById('deliver_date')
    deliverDateInput.max = today.value

    if(Object.keys(props.targetLoan).length !== 0){
        loanReader.value = props.targetLoan['reader_id']
        loanBook.value = props.targetLoan['book_id']
        loanObservation.value = props.targetLoan['observation']
        loanDeliverDate.value = props.targetLoan['deliver_date']
        console.log(props.targetLoan['return_date'])

        if(props.targetLoan['active'] === 1)
            loanActive.value = [1]
        else
            loanActive.value = []

        const deliverDate = new Date(props.targetLoan['deliver_date'])        
        var year = deliverDate.getFullYear()
        var month = deliverDate.getMonth() + 1
        if(month < 10) month = '0' + month
        var day = deliverDate.getDate() + 1
        if(day < 10) day = '0' + day
        
        deliverDateInput.value = year + '-' + month + '-' + day

        if(props.targetLoan['return_date'] !== null){
            const returnDateInput = document.getElementById('return_date')
            const returnDate = new Date(props.targetLoan['deliver_date'])        
            var year = returnDate.getFullYear()
            var month = returnDate.getMonth() + 1
            if(month < 10) month = '0' + month
            var day = returnDate.getDate() + 1
            if(day < 10) day = '0' + day
            
            returnDateInput.value = year + '-' + month + '-' + day
            document.getElementById('observation').disabled = true
        }

        $('#readers').val(loanReader.value)
        $('#readers').trigger('change')
        $('#readers').prop('disabled', true)

        $('#books').val(loanBook.value);
        $('#books').trigger('change')
        $('#books').prop('disabled', true)
    }

    // Vue.js presenta algunas dificultades para trabajar con Select2, en este caso le indicamos que al cambiar cualquiera de sus valores
    // Se refleje en su respectiva referencia ref()
    $('#readers').on('select2:select', function (e) { 
        loanReader.value = e.target.value;
        document.getElementById('select2-readers-container').classList.remove('border-red') 

    });
    $('#books').on('select2:select', function (e) { 
        loanBook.value = e.target.value;
        document.getElementById('select2-books-container').classList.remove('border-red') 

    });
    
    mounted.value = true    
})

async function ValidateForm() {
    const validator = new FormValidator()
    formErrors.value = [] 
    const validationStructure = {
        'deliver_date':{
            'min': 8, 
            'max': 10, 
            'required': true, 
            'value': loanDeliverDate.value 
        },
        'select2-books-container':{
            'min': 0, 
            'max': 0, 
            'required': true, 
            'value': loanBook.value 
        },
        'select2-readers-container':{
            'min': 0, 
            'max': 0, 
            'required': true, 
            'value': loanReader.value 
        },
        'observation':{
            'min': 0, 
            'max': 1000, 
            'required': false, 
            'value': loanObservation.value 
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

    if(Object.keys(props.targetLoan).length !== 0){
        if(loanActive.value.length === 0)
            loanActive.value = ['0']
        else
            loanActive.value = ['1']
    
        if(!['0', '1'].includes(loanActive.value[0]))
            formErrors.value.push('El campo "activo" debe ser 1 o 0')
    }


    if(formErrors.value.length === 0){        
        if(Object.keys(props.targetLoan).length === 0){
            const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar nuevo préstamo?', 'question')
            if(confirmAction === false)
                return

            // Creating the loan
            const cleanLoanData = {
                'deliver_date': validationStructure['deliver_date']['value'],
                'book': validationStructure['select2-books-container']['value'],
                'reader': validationStructure['select2-readers-container']['value'],
                'observation':validationStructure['observation']['value'],
            }

            const created = await loanStore.CreateLoan(cleanLoanData)            
            if(created.success){
                utilsStore.ShowModal('Success', created.message, 'success')
                loanDeliverDate.value = ''
                loanBook.value = ''
                loanReader.value = ''
                loanObservation.value = ''

                $('#readers').val(''); $('#readers').trigger('change');
                $('#books').val(''); $('#books').trigger('change');
            }
            else
                utilsStore.ShowModal('Error', created.message, 'error')
        }
        else{    
            // Updating the loan's observation
            const confirmAction = await utilsStore.ConfirmModal('¿Desea editar la observación del préstamo?', 'question')
            if(confirmAction === false)
                return

            let cleanLoanData = {}
            if(props.targetLoan['observation'] !== loanObservation.value) cleanLoanData['observation'] = loanObservation.value
            
            if(Object.keys(cleanLoanData).length === 0)
                utilsStore.ShowModal('Info', 'No se realizaron cambios', 'info')
            else{
                const updated = await loanStore.UpdateLoanObservation(props.targetLoan['loan_id'], cleanLoanData)
                
                if (updated.success)
                    utilsStore.ShowModal('Success', updated.message, 'success')
                else
                    utilsStore.ShowModal('Error', updated.message, 'error')            
            }
        }          
    }    
}

const DisplayReaderForm = (() => {
    $('#ReaderModal').modal('show')
})

const DeactivateLoan = (async () => {
    const confirmAction = await utilsStore.ConfirmModal('¿Desea desactivar el préstamo?', 'question')

    if(confirmAction === true){
        const finishResult = await loanStore.DeactivateLoan(props.targetLoan.loan_id)
        if (finishResult.success === true){
            utilsStore.ShowModal('Éxito', finishResult.message, 'success')
            router.push({name: 'dashboard'})
        }
        else{
            utilsStore.ShowModal('Error', finishResult.message, 'error')
        }
    }
})

const FinishLoan = (async () => {
    const confirmAction = await utilsStore.ConfirmModal('¿El préstamo ha sido devuelto?', 'question')
    
    if(confirmAction === true){
        const finishResult = await loanStore.FinishLoan(props.targetLoan.loan_id)
        if (finishResult.success === true){
            utilsStore.ShowModal('Éxito', finishResult.message, 'success')
            router.push({name: 'dashboard'})
        }
        else{
            utilsStore.ShowModal('Error', finishResult.message, 'error')
        }
    }
})

const FetchAgain = (() => {
    emit('fetchAgain')
})

</script>

<template>
    <form class="row m-0 p-0 justify-content-around align-items-start" @submit.prevent="ValidateForm">
        <template v-if="mounted.value === false">
            <LoadingGadget/>
        </template>
        <template v-else>
            <div class="col-12 row p-4 pt-5 fs-4 justify-content-around hide-up animated-1">
                <div class="col-12 col-lg-9 row myForm shadowed-l rounded lb-bg-terciary-ul justify-content-center">
                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="deliver_date"><strong>Fecha del préstamo</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-4 m-0 p-0">
                                    <input class="col-12 myInput" type="date" id="deliver_date" name="deliver_date" value="" v-model="loanDeliverDate" :disabled="Object.keys(props.targetLoan).length !== 0">
                                </div>
                            </div>
                        </div>
                    </div>

                    <template v-if="Object.keys(props.targetLoan).length !== 0">
                        <div :class="formRowStyle" v-if="props.targetLoan['return_date'] !== null">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="return_date">Fecha de devolución</label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
                                    <div class="row col-12 col-lg-4 m-0 p-0">
                                        <input class="col-12 myInput" type="date" id="return_date" name="return_date" disabled>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template>

                    <div :class="formRowStyle" v-if="Object.keys(props.targetLoan).length !== 0">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="deliver_date">Fecha de creación</label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12">
                                <div class="row col-12 col-lg-4 m-0 p-0">
                                    <input class="col-12 myInput" type="date" id="deliver_date" name="deliver_date" :value="props.targetLoan.created_at" :disabled="Object.keys(props.targetLoan).length !== 0">
                                </div>
                            </div>
                        </div>
                    </div>
        
                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="readers"><strong>Lector</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-10 col-lg-8">
                                <select class="myInput select2" id="readers" :v-model="loanReader">
                                    <option value="">&nbsp;</option>
                                    <template
                                    v-for="reader in props.readers"
                                    :key="reader.id">
                                        <option class="fw-normal" :value="reader.id" :selected="loanReader == reader.id">
                                            ({{ reader.cedula }}) {{ reader.names }} {{  reader.surnames }}
                                        </option>                                    
                                    </template>
                                </select>
                            </div>
                            <div v-if="Object.keys(props.targetLoan).length === 0" class="col-1 align-middle cursor-pointer" title="Agregar nuevo lector" @click="DisplayReaderForm()">
                                <i class="fa fa-plus my-auto align-middle text-success bg-white border-black p-1 rounded"></i>
                            </div>
                        </div>
                    </div>
    
                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="books"><strong>Libro</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-10 col-lg-8">
                                <select class="myInput select2" id="books" :v-model="loanBook">
                                    <option value="">&nbsp;</option>
                                    <template
                                    v-for="book in props.books"
                                    :key="book.id">
                                        <option class="fw-normal" :value="book.id" :selected="loanBook == book.id">
                                            {{ book.title }} ({{ book.call_number }})
                                        </option>                                    
                                    </template>
                                </select>
                            </div>
                        </div>
                    </div>
        
                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="observation">Observación</label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-10">
                                <textarea id="observation" cols="30" rows="4" maxlength="1000" class="myInput" v-model="loanObservation"></textarea>
                            </div>
                        </div>
                    </div>
                    
                    <template v-if="props.targetLoan['return_date'] === null || Object.keys(props.targetLoan).length === 0">
                        <div class="row m-0 p-0 justify-content-center my-3">
                            <div class="row m-0 p-0 col-4 justify-content-center">
                                <button class="col-8 myBtn shadowed-l h3 bg-danger border-white rounded-pill border-1 text-white" type="button" @click="DeactivateLoan">
                                    Desactivar préstamo
                                </button>
                            </div>
    
                            <div class="row m-0 p-0 col-4 justify-content-center">
                                <button class="col-8 myBtn shadowed-l h3 lb-bg-primary rounded-pill border-1 text-white" type="button" @click="FinishLoan">
                                    Préstamo devuelto
                                </button>
                            </div>
                        </div>
                        <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                            <div class="row m-0 p-0 col-12 justify-content-center">
                                <button class="col-6 col-lg-3 myBtn terciary-btn shadowed-l h3">
                                    {{ Object.keys(props.targetLoan).length === 0 ? 'Registrar ' : 'Modificar ' }}
                                </button>
                            </div>
                        </div>
                    </template>
        
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

    <template v-if="Object.keys(props.targetLoan).length === 0">
        <LargeModalGadget
        :componentToShow="ReaderForm"
        :title="'Agregar nuevo lector'"
        :modalName="'ReaderModal'"
        @firstEmit="FetchAgain"
        />
    </template>

</template>

<style scoped>
textarea{
    padding:5px;
}

.categories-section div{
    border: 1px black solid;
}
</style>