<script setup>
import { ref, onMounted } from 'vue'

import FormValidator from '@/utils/FormValidator'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useDeckStore from '@/stores/decks'


const utilsStore = useUtilsStore()
const deckStore = useDeckStore()

const mounted = ref(false)
const formErrors = ref([])

const deckName = ref('')
const deckColors = ref([]);

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-3'
const labelStyle = 'text-center text-green text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const emits = defineEmits(['formOk'])
const props = defineProps({
    'targetDeck': {
        type: Object,
        default: {}
    },
    'colors': {
        type: Array,
        default: []
    }
})

onMounted(async () => {
    OnAppearAnimation('hide-up')    

    if(Object.keys(props.targetDeck).length !== 0){
        deckName.value = props.targetDeck['name']       
        deckColors.value = props.targetDeck['colors']  
    }
    else{
        deckColors.value = []
    }
    
    mounted.value = true    
})

async function ValidateForm() {
    const validator = new FormValidator()
    formErrors.value = [] 
    const validationStructure = {
        'name':{ 
            'min': 2, 
            'max': 100, 
            'required': true, 
            'value': deckName.value 
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

    if(deckColors.value.length === 0)
        formErrors.value.push('Seleccione al menos un color')

    if(formErrors.value.length === 0){        
        if(Object.keys(props.targetDeck).length === 0){
            // Creating the deck
            const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar este nuevo deck?', 'question')
            if(confirmAction === false)
                return
            
            const cleanData = {
                'name': validationStructure['name']['value'],
                'colors': deckColors.value
            }

            const created = await deckStore.CreateDeck(cleanData)            
            if(created.success){
                utilsStore.ShowModal('Success', created.message, 'success')
                deckName.value = ''
                deckColors.value = []
                emits('formOk')
            }
            else
                utilsStore.ShowModal('Error', created.message, 'error')
        }
        else{
            // Updating the deck
            const confirmAction = await utilsStore.ConfirmModal('¿Desea modificar este deck?', 'question')
            if(confirmAction === false)
                return

            let cleanData = {}

            if(props.targetDeck['name'] !== deckName.value) cleanData['name'] = deckName.value
            if(props.targetDeck['colors'] !== deckColors.value) cleanData['colors'] = deckColors.value

            if(Object.keys(cleanData).length === 0)
                utilsStore.ShowModal('Info', 'No se realizaron cambios', 'info')
            else{
                const updated = await deckStore.UpdateDeck(props.targetDeck['id'], cleanData)
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
                            <div class="row col-12 col-lg-8">
                                <input type="text" class="myInput" maxlength="100" id="name" autofocus v-model="deckName">
                            </div>
                        </div>
                    </div>                  

                    
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle"><strong>Colores</strong></label>
                            </div>
                            
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
                                    <div 
                                    class="row col-12 col-lg-5 m-0 p-0 my-1"
                                    v-for="color in props.colors"
                                    :key="color">
                                        <label :class="'col-4 text-' + color " :for="color">{{ color }}</label>
                                        <input 
                                        :id="color" 
                                        :value="color"
                                        type="checkbox" 
                                        v-model="deckColors"
                                        class="col-1 mx-auto mx-lg-0"/>
                                    </div>
                                </div>
                            </div>
                        </div>  
                   
        
                    <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                        <div class="row m-0 p-0 col-12 justify-content-center">
                            <button class="col-6 col-lg-3 myBtn green-btn shadowed-l h3">
                                {{ Object.keys(props.targetDeck).length === 0 ? 'Registrar ' : 'Modificar ' }}
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