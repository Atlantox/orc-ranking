<script setup>
import { ref, onMounted } from 'vue'

import FormValidator from '@/utils/FormValidator'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useBookStore from '@/stores/books'


const utilsStore = useUtilsStore()
const bookStore = useBookStore()

const mounted = ref(false)
const formErrors = ref([])

const authorName = ref('')

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-3'
const labelStyle = 'text-center text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const emits = defineEmits(['formOk'])
const props = defineProps({
    'targetAuthor': {
        type: Object,
        default: {}
    }
})

onMounted(async () => {
    OnAppearAnimation('hide-up')

    if(props.targetAuthor !== undefined){
        authorName.value = props.targetAuthor['name']         
    }
    
    mounted.value = true    
})

async function ValidateForm() {
    const validator = new FormValidator()
    formErrors.value = [] 
    const validationStructure = {
        'name':{ 
            'min': 5, 
            'max': 30, 
            'required': true, 
            'value': authorName.value 
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
        if(Object.keys(props.targetAuthor).length === 0){
            // Creating the author
            const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar este nuevo autor?', 'question')
            if(confirmAction === false)
                return
            
            const cleanAuthorData = {
                'name': validationStructure['name']['value'],
            }

            const created = await bookStore.CreateAuthor(cleanAuthorData)            
            if(created.success){
                utilsStore.ShowModal('Success', created.message, 'success')
                authorName.value = ''
                emits('formOk')
            }
            else
                utilsStore.ShowModal('Error', created.message, 'error')
        }
        else{
            // Updating the author
            const confirmAction = await utilsStore.ConfirmModal('¿Desea editar este libro?', 'question')
            if(confirmAction === false)
                return

            let cleanAuthorData = {}

            if(props.targetAuthor['name'] !== authorName.value) cleanAuthorData['name'] = authorName.value

            if(Object.keys(cleanAuthorData).length === 0)
                utilsStore.ShowModal('Info', 'No se realizaron cambios', 'info')
            else{
                const updated = await bookStore.UpdateAuthor(props.targetAuthor['id'], cleanAuthorData)
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
                <div class="col-12 col-lg-10 p-2 row myForm shadowed-l rounded lb-bg-terciary-ul justify-content-center">
                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="name"><strong>Nombre</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12 col-lg-8">
                                <input type="text" class="myInput" maxlength="150" id="name" autofocus v-model="authorName">
                            </div>
                        </div>
                    </div>
        
                    <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                        <div class="row m-0 p-0 col-12 justify-content-center">
                            <button class="col-6 col-lg-3 myBtn terciary-btn shadowed-l h3">
                                {{ Object.keys(props.targetAuthor).length === 0 ? 'Registrar ' : 'Modificar ' }}
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

.categories-section div{
    border: 1px black solid;
}
</style>