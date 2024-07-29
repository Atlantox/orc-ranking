<script setup>
import { ref, onMounted } from 'vue'
import Select2Initializer from '@/utils/Select2Initializer'
import FormValidator from '@/utils/FormValidator'
const formErrors = ref([])

const myText = ref('UwU')
const myNumber = ref(5055)
const myTextarea = ref('Whatojell')
const myRadio = ref('4')
const myCheckbox = ref(['1', '4'])
const myFile = ref('')
const mySelect = ref('1')
const myDate = ref('2024-04-16')

onMounted(() => {
    const s2Initializer = new Select2Initializer()
})

const UploadFile = (event) => {
    const file = event.target.files[0];
    //const reader = new FileReader();
    myFile.value = file
}

const ValidateForm = ((e) => {
    const myForm = e.srcElement
    const validator = new FormValidator()

    
    
})
</script>

<template>
    <div class="row m-0 p-0">
        <form action="" class="col-12 row m-0 p-2 fs-4 myForm shadowed-l rounded lb-bg-terciary-ul" @submit.prevent="ValidateForm">
            <div class="row m-0 p-0 justify-content-center my-2">
                <div class="row m-0 p-0 col-3">
                    <label class="text-end" for="text">Text input</label>
                </div>
                <div class="row m-0 p-0 col-6">
                    <div class="row col-8">
                        <input type="text" class="myInput" id="text" autofocus v-model="myText">
                    </div>
                </div>
            </div>

            <div class="row m-0 p-0 justify-content-center my-2">
                <div class="row m-0 p-0 col-3">
                    <label class="text-end" for="number">Number input</label>
                </div>
                <div class="row m-0 p-0 col-6">
                    <div class="row col-4">
                        <input type="number" class="myInput" id="number" v-model="myNumber">
                    </div>
                </div>
            </div>

            <div class="row m-0 p-0 justify-content-center my-2">
                <div class="row m-0 p-0 col-3">
                    <label class="text-end" for="textarea">Textarea</label>
                </div>
                <div class="row m-0 p-0 col-6">
                    <div class="row col-12">
                        <textarea name="" id="textarea" cols="30" rows="4" class="myInput" v-model="myTextarea"></textarea>
                    </div>
                </div>
            </div>

            <div class="row m-0 p-0 justify-content-center my-3">
                <div class="row m-0 p-0 col-3">
                    <label class="text-end">Radio input</label>
                </div>
                <div class="row m-0 p-0 col-6 fs-5 justify-content-center">
                    <div class="row col-12">
                        <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                            <label class="col-6 text-end" for="radio1">Opción 1</label>
                            <input class="col-1" type="radio" id="radio1" name="radio" value="1" v-model="myRadio">
                        </div>
                        <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                            <label class="col-6 text-end" for="radio2">Opción 2</label>
                            <input class="col-1" type="radio" id="radio2" name="radio" value="2" v-model="myRadio">
                        </div>
                        <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                            <label class="col-6 text-end" for="radio3">Opción 3</label>
                            <input class="col-1" type="radio" id="radio3" name="radio" value="3" v-model="myRadio">
                        </div>
                        <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                            <label class="col-6 text-end" for="radio4">Opción 4</label>
                            <input class="col-1" type="radio" id="radio4" name="radio" value="4" v-model="myRadio">
                        </div>
                    </div>
                </div>
            </div>

            <div class="row m-0 p-0 justify-content-center my-3">
                <div class="row m-0 p-0 col-3">
                    <label class="text-end">Checkbox input</label>
                </div>
                <div class="row m-0 p-0 col-6 fs-5 justify-content-center">
                    <div class="row col-12">
                        <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                            <label class="col-6 text-end" for="checkbox1">Opción 1</label>
                            <input class="col-1" type="checkbox" id="checkbox1" name="checkbox" value="1" v-model="myCheckbox">
                        </div>
                        <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                            <label class="col-6 text-end" for="checkbox2">Opción 2</label>
                            <input class="col-1" type="checkbox" id="checkbox2" name="checkbox" value="2" v-model="myCheckbox">
                        </div>
                        <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                            <label class="col-6 text-end" for="checkbox3">Opción 3</label>
                            <input class="col-1" type="checkbox" id="checkbox3" name="checkbox" value="3" v-model="myCheckbox">
                        </div>
                        <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                            <label class="col-6 text-end" for="checkbox4">Opción 4</label>
                            <input class="col-1" type="checkbox" id="checkbox4" name="checkbox" value="4" v-model="myCheckbox">
                        </div>
                    </div>
                </div>
            </div>


            <div class="row m-0 p-0 justify-content-center my-2">
                <div class="row m-0 p-0 col-3">
                    <label class="text-end">File</label>
                </div>
                <div class="row m-0 p-0 col-6">
                    <div class="row col-12">
                        <label for="file">
                            <span class="fileinput-label">
                                <template
                                v-if="myFile === ''">
                                    Subir archivo                                
                                </template>
                                <template
                                v-else>
                                    {{ myFile.name }}                        
                                </template>
                            </span>
                        </label>
                        <input name="" id="file" class="myInput" type="file" @change="UploadFile">
                    </div>
                </div>
            </div>

            <div class="row m-0 p-0 justify-content-center my-2">
                <div class="row m-0 p-0 col-3">
                    <label class="text-end" for="select2">Select</label>
                </div>
                <div class="row m-0 p-0 col-6">
                    <div class="row col-7">
                        <select class="myInput select2" id="select2" v-model="mySelect">
                            <option class="" value=""></option>
                            <option class="fw-normal" value="1">Category 1</option>
                            <option class="" value="2">Category 2</option>
                            <option class="" value="3">Category 3</option>
                            <option class="" value="4">Category 4</option>
                            <option class="" value="5">Category 5</option>
                            <option class="" value="6">Category 6</option>
                        </select>
                    </div>
                </div>
            </div>

            <div class="row m-0 p-0 justify-content-center my-2">
                <div class="row m-0 p-0 col-3">
                    <label class="text-end" for="date">Date</label>
                </div>
                <div class="row m-0 p-0 col-6">
                    <div class="row col-4">
                        <input name="" id="date" class="myInput" type="date" v-model="myDate">
                    </div>
                </div>
            </div>

            <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                <div class="row m-0 p-0 col-12 justify-content-center">
                    <button class="col-2 terciary-btn shadowed-l h3">
                        {{ edit ? 'Modificar ' : 'Registrar ' }}
                    </button>
                </div>
            </div>

            <div v-if="formErrors.length > 0" class="row m-0 p-0 justify-content-center my-2 mt-5">
                <ul class="row m-0 p-0 col-12 justify-content-center list-unstyled text-center text-danger">
                    <li 
                    v-for="error, index in formErrors"
                    :key="index"
                    >
                        {{ error.message }}
                    </li>  
                </ul>
            </div>
        
        </form>
    </div>
</template>

<style scoped>
textarea{
    padding:5px;
}
</style>