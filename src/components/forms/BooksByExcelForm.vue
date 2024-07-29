<script setup>
import { ref, onMounted } from 'vue'

import EditorialForm from './EditorialForm.vue'
import AuthorForm from './AuthorForm.vue'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import useUtilsStore from '@/stores/utils'
import useBookStore from '@/stores/books'

const utilsStore = useUtilsStore()
const bookStore = useBookStore()

const excelData = ref(null)
const excelName = ref('')
const formErrors = ref([])

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-6'
const labelStyle = 'text-center text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-6 justify-content-center justify-content-md-start align-items-center'

onMounted(async () => {
    OnAppearAnimation('hide-up')   
})

async function ValidateForm() {
    formErrors.value = []
    const validationStructure = {
        'Título':{ 
            'min': 1, 
            'max': 150, 
            'required': true, 
        },
        'Autor':{
            'min': 0, 
            'max': 30, 
            'required': false, 
        },
        'Cota':{
            'min': 1, 
            'max': 8, 
            'required': true, 
        },
        'Editorial':{
            'min': 0, 
            'max': 30, 
            'required': false, 
        },
        'Estante':{
            'min': 1, 
            'max': 10,
            'required': true, 
        },
        'Descripción':{
            'min': 0, 
            'max': 1000, 
            'required': false, 
        },       
    }
    
    if(excelData.value === null){
        formErrors.value.push('Se requiere de subir un archivo Excel')
        return
    }

    var bookCounter = 2
    var call_numbers = []

    excelData.value.forEach((tentativeBook) => {
        var errorInBook = false

        // Verificamos que los campos estalbecidos arriba son correctos
        for(let key in validationStructure){
            if(key in tentativeBook === false && validationStructure[key]['required'] === true){
                formErrors.value.push('El libro de la fila ' + bookCounter + ' no tiene el campo ' + key)
                errorInBook = true
            }else{
                var fieldStringValue = String(tentativeBook[key])
                if(fieldStringValue.trim() === ''){
                    formErrors.value.push('El campo ' + key + ' del libro de la fila ' + bookCounter + ' está vacío')
                    errorInBook = true
                }
                else{
                    if(fieldStringValue.length > validationStructure[key]['max']){
                        formErrors.value.push('El campo ' + key + ' del libro de la fila ' + bookCounter + ' supera el máximo de caracteres permitido (' + validationStructure[key]['max']  +')')
                        errorInBook = true
                    }

                    if(fieldStringValue.length < validationStructure[key]['min']){
                        formErrors.value.push('El campo ' + key + ' del libro de la fila ' + bookCounter + ' no alcanza el mínimo de caracteres permitido (' + validationStructure[key]['min']  +')')
                        errorInBook = true
                    }
                }

                
            }
        }

        // Faltan por validar los campos categoría y páginas que tendrán validaciones más concretas
        if('Categorías' in tentativeBook === false){
            formErrors.value.push('El campo Categorías del libro de la fila ' + bookCounter + ' no existe')
            errorInBook = true
        }
        else{
            // El campo categorías existe
            if(tentativeBook['Categorías'].trim() === ''){
                formErrors.value.push('El campo Categorías del libro de la fila ' + bookCounter + ' está vacío')
                errorInBook = true
            }
            else{
                // El campo categorías contiene algo, validamos el tamaño de cada posible categoría que pueda tener
                var categories = tentativeBook['Categorías'].split(',')
                categories.forEach((category) => {
                    var trimmedCategory = category.trim()
                    if(trimmedCategory.length > 50){
                        formErrors.value.push('La categoría' + trimmedCategory + ' del libro de la fila ' + bookCounter + ' supera el máximo de caracteres permitido (50)')
                        errorInBook = true
                    }

                    if(trimmedCategory.length <= 2){
                        formErrors.value.push('La categoría' + trimmedCategory + ' del libro de la fila ' + bookCounter + ' no alcanza el mínimo de caracteres permitido (3)')
                        errorInBook = true
                    }
                })
            }
        }

        // Validamos el número de páginas
        if('Páginas' in tentativeBook === false){
            formErrors.value.push('El campo Páginas del libro de la fila ' + bookCounter + ' no existe')
            errorInBook = true
        }
        else{
            // El campo páginas existe
            var stringPages = String(tentativeBook['Páginas'])
            if(stringPages.trim() === ''){
                formErrors.value.push('El campo Páginas del libro de la fila ' + bookCounter + ' está vacío')
                errorInBook = true
            }
            else{
                // El campo páginas contiene algo
                if(isNaN(stringPages)){
                    formErrors.value.push('El campo Páginas del libro de la fila ' + bookCounter + ' no es un número')
                    errorInBook = true
                }
                else{
                    if(tentativeBook['Páginas'] > 99999){
                        formErrors.value.push('El campo Páginas del libro de la fila ' + bookCounter + ' no puede ser mayor a 99999')
                    errorInBook = true
                    }
                }
            }
        }

        if(errorInBook === false){
            if(call_numbers.includes(tentativeBook['Cota']))
                formErrors.value.push('Cota "' + tentativeBook['Cota'] + '" repetida en el libro de la fila ' + bookCounter)
            else
                call_numbers.push(tentativeBook['Cota'])
        }

        bookCounter++
    })   
    
    if(formErrors.value.length === 0){
        /*
        const confirmAction = await utilsStore.ConfirmModal('Se añadirán ' + (bookCounter - 2) + ' libros', 'info')
        if(confirmAction === false)
            return
        */

        const created = await bookStore.CreateBooks(excelData.value)
        if(created.success){
            utilsStore.ShowModal('Success', created.message, 'success')
            ResetExcel()            
        }
        else
            utilsStore.ShowModal('Error', created.message, 'error')

    }

}

const UploadFile = ((event) => {
    const file = event.target.files[0];
    if(file !== undefined){
        excelName.value = file.name
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const data = new Uint8Array(e.target.result);
                const workbook = XLSX.read(data, { type: 'array' });
    
                const sheetName = workbook.SheetNames[0];
                const worksheet = workbook.Sheets[sheetName];
    
                const json = XLSX.utils.sheet_to_json(worksheet);
                excelData.value = json;
            };
            reader.readAsArrayBuffer(file);
        }
    }
})

const ResetExcel = (() => {
    excelData.value = null
    document.getElementById('file').value = ''
    excelName.value = ''
    const spinIcon = document.getElementById('spin-icon')
    if (spinIcon !== null){
        spinIcon.classList.remove('spin-on')
        void spinIcon.offsetWidth
        spinIcon.classList.add('spin-on')
    }
})


</script>

<template>
    <form class="row m-0 p-0 justify-content-around align-items-start" @submit.prevent="ValidateForm">
        <div class="col-12 row p-4 pt-5 fs-4 justify-content-around hide-up animated-1">
            
            <div class="col-12 p-2 row myForm shadowed-l rounded lb-bg-terciary-ul justify-content-center">
                <div class="col-12 row m-0 p-0 justify-content-center p-3">
                    <h2 class="text-center fw-bold">Consideraciones</h2>
                    <ul class="col-12 col-lg-8">
                        <li>Las cabeceras de la tabla deben tener <strong>exactamente</strong> el nombre indicado respetando tildes y mayúsculas</li>
                        <li>Las categorías, autores y editoriales no existentes en la base de datos, serán <strong>agregadas</strong> automáticamente</li>
                        <li>Los únicos campos que pueden estar <strong>vacíos</strong> son: autor, editorial y descripción</li>
                        <li><strong>NINGUNA</strong> de las cotas debe repetirse</li>
                        <li>Los libros deben estar en la <strong>primera hoja</strong> del excel</li>
                        <li>Debe subir un archivo excel que tenga el siguiente <strong>formato:</strong></li>
                    </ul>
                    <figure class="col-12 shadowed-l p-0 my-3">
                        <img class="w-100" alt="">
                    </figure>
                </div>
    
                <div :class="formRowStyle">
                    <div :class="labelContainerStyle">
                        <label :class="labelStyle" for="file"><strong>Archivo excel</strong></label>
                    </div>
                    <div :class="inputContainerStyle">
                        <div class="row col-12">
                            <label for="file" class="w-auto">
                                <span class="fileinput-label text-white w-auto">
                                    <template
                                    v-if="excelName === ''">
                                        Subir archivo                                
                                    </template>
                                    <template
                                    v-else>
                                        {{ excelName }}                        
                                    </template>
                                </span>
                            </label>
                            <i id="spin-icon" class="spin-on animated-1 fa fa-rotate-left ms-3 w-auto text-info cursor-pointer hover-bigger fs-3" title="Limpiar excel" @click="ResetExcel()"></i>
                            <input id="file" class="myInput m-0 p-0" type="file" @change="UploadFile" accept=".xlsx">
                        </div>
                    </div>
                </div>
    
                <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                    <div class="row m-0 p-0 col-12 justify-content-center">
                        <button class="col-6 col-lg-3 myBtn terciary-btn shadowed-l h3">
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