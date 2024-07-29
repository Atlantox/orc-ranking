<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import LoadingGadget from '../myGadgets/LoadingGadget.vue';
import PageTitleView from '../PageTitle.vue'

import useUtilsStore from '@/stores/utils';
import useSessionStore from '@/stores/session.js'

const utilsStore = useUtilsStore()
const sessionStore = useSessionStore()
const router = useRouter()

const formErrors = ref([])
const waitingResponse = ref(false)

const username = ref('')
const password = ref('')

const ValidateForm = (async (e) => {
    if(username.value === '') formErrors.value.push('Usuario vacío')
    if(password.value === '') formErrors.value.push('Contraseña vacío')

    if(formErrors.value.length === 0){
        const loginResult = sessionStore.loginResult
        waitingResponse.value = true
        await sessionStore.TryLogin(username.value, password.value)
        waitingResponse.value = false
        if(loginResult.value.success === true){            
            sessionStore.authenticated = true
            sessionStore.token = loginResult.value.token
            sessionStore.userData = loginResult.value.userData
            sessionStore.lastLoginDate = new Date()
            router.push({name: 'dashboard'})
        }
        else{
            utilsStore.ShowModal('Error', loginResult.value.message, 'error')
        }
    }
})
</script>

<template>
    <div class="row m-0 p-0 justify-content-center">
        <form class="col-12 col-lg-9 row m-0 p-2 fs-4 myForm shadowed-n rounded lb-bg-terciary-ul" @submit.prevent="ValidateForm">
            <PageTitleView :title="'Login administrativo'"/>

            <template v-if="waitingResponse">
                <LoadingGadget/>
            </template>
            <template v-else>
                <div class="row m-0 p-0 justify-content-center my-2">
                    <div class="row m-0 p-0 col-10 col-lg-3">
                        <label class="text-center text-lg-end" for="username">Usuario</label>
                    </div>
                    <div class="row m-0 p-0 col-10 col-lg-7">
                        <div class="row col-12 col-lg-7">
                            <input type="password" class="myInput" maxlength="50" minlength="6" id="username" autofocus v-model="username">
                        </div>
                    </div>
                </div>
    
                <div class="row m-0 p-0 justify-content-center my-2">
                    <div class="row m-0 p-0 col-10 col-lg-3">
                        <label class="text-center text-lg-end" for="password">Contraseña</label>
                    </div>
                    <div class="row m-0 p-0 col-10 col-lg-7">
                        <div class="row col-12 col-lg-7">
                            <input type="password" class="myInput" maxlength="50" minlength="8" id="password" v-model="password">
                        </div>
                    </div>
                </div>
    
                <template v-if="formErrors.length > 0">
                    <div class="row m-0 p-0 justify-content-center my-2 mb-0">
                        <div class="row m-0 p-0 col-12 justify-content-center">
                            <ul class="row col-6 m-0 p-0 text-center list-unstyled error-displayer">
                                <li
                                v-for="error, index in formErrors"
                                :key="index">
                                    {{ error }}
                                </li>
                            </ul>
                        </div>
                    </div>                    
                </template>
            </template>

            <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                <div class="row m-0 p-0 col-12 justify-content-center">
                    <button class="col-2 myBtn terciary-btn shadowed-l h3">
                        Ingresar
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

h1{
  font-size:50px !important;
}
</style>
