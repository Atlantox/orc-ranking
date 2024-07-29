<script setup>
import { ref, onMounted } from 'vue'

import FormValidator from '@/utils/FormValidator'

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer'

import BinnacleTable from '../tables/BinnacleTable.vue'

import useUtilsStore from '@/stores/utils'
import useSessionStore from '@/stores/session'
import useUserStore from '@/stores/users'
import useBinnacleStore from '@/stores/binnacle'


const utilsStore = useUtilsStore()
const userStore = useUserStore()
const sessionStore = useSessionStore()
const binnacleStore = useBinnacleStore()

const mounted = ref(false)
const binnacleFetched = ref(false)
const formErrors = ref([])
const selfUser = ref(false)

const userNickname = ref('')
const userLevel = ref('')
const userUsername = ref('')
const userPassword = ref('')
const userPasswordConfirm = ref('')
const userActive = ref([1])

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-3'
const labelStyle = 'text-center text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const props = defineProps({
    'targetUser': Object
})

const emits = defineEmits(['formOk'])

onMounted(async () => {
    OnAppearAnimation('hide-up')
    if(Object.keys(props.targetUser).length !== 0){
        await binnacleStore.FetchBinnacleOfUser(props.targetUser.id)
        selfUser.value = props.targetUser.id === sessionStore.userData.id
        userNickname.value = props.targetUser.nickname
        userLevel.value = props.targetUser.level
        if(props.targetUser.active === 1)
            userActive.value = [1]
        else
            userActive.value = []
    }
    mounted.value = true
    binnacleFetched.value = true
})


const ValidateForm = (async (e) => {
    const validator = new FormValidator()

    formErrors.value = [] 
    const validationStructure = {
        'nickname':{ 
            'min': 4,
            'max': 50, 
            'required': true, 
            'value': userNickname.value 
        },
        'username':{
            'min': 6, 
            'max': 50, 
            'required': Object.keys(props.targetUser).length === 0, 
            'value': userUsername.value 
        },
        'password':{
            'min': 8, 
            'max': 50, 
            'required': Object.keys(props.targetUser).length === 0, 
            'value': userPassword.value 
        },
        'passwordConfirm':{
            'min': 8, 
            'max': 50, 
            'required': Object.keys(props.targetUser).length === 0, 
            'value': userPasswordConfirm.value 
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


    if(userLevel.value === ''){
        formErrors.value.push('Debe elegir un tipo de usuario')
    }
    else{
        if(!sessionStore.userData.permissons.includes(userLevel.value) && selfUser.value === false){
            formErrors.value.push('Usted carece de permisos para crear usuarios de tipo ' + userLevel.value)
        }
    }

    if(userActive.value.length === 0)
        userActive.value = ['0']
    else
        userActive.value = ['1']

    if(!['0', '1'].includes(userActive.value[0]))
        formErrors.value.push('El campo "activo" debe ser 1 o 0')
    
    if(!['Editor', 'Admin', 'Super'].includes(userLevel.value))
        formErrors.value.push('Tipo de usuario inválido')

    if(userPassword.value !== userPasswordConfirm.value){
        formErrors.value.push('Las contraseñas no coinciden')
    }


    if(formErrors.value.length === 0){        
        if(Object.keys(props.targetUser).length === 0){
            // Creating the user
            const confirmAction = await utilsStore.ConfirmModal('¿Desea registrar este nuevo usuario?', 'question')
            if(confirmAction === false)
                return

            const cleanUserData = {
                'nickname': validationStructure['nickname']['value'],
                'username': validationStructure['username']['value'],
                'password': validationStructure['password']['value'],
                'level': userLevel.value,
                'active': userActive.value[0],
            }

            const created = await userStore.CreateUser(cleanUserData)            
            if(created.success){
                emits('formOk')
                utilsStore.ShowModal('Success', created.message, 'success')
                userNickname.value = ''
                userPassword.value = ''
                userUsername.value = ''
                userLevel.value = ''
                userActive.value = [1]
            }
            else
                utilsStore.ShowModal('Error', created.message, 'error')
        }
        else{
            // Updating the user
            const confirmAction = await utilsStore.ConfirmModal('¿Desea editar este nuevo usuario?', 'question')
            if(confirmAction === false)
                return

            let cleanUserData = {}

            if(props.targetUser['nickname'] !== userNickname.value) cleanUserData['nickname'] = userNickname.value
            if(props.targetUser['level'] !== userLevel.value) cleanUserData['level'] = userLevel.value
            if(props.targetUser['active'] !== parseInt(userActive.value[0])) cleanUserData['active'] = userActive.value[0]

            if(userUsername.value !== ''){
                cleanUserData['username'] = userUsername.value
            }

            if(userPassword.value !== ''){
                cleanUserData['password'] = userPassword.value
            }

            if(Object.keys(cleanUserData).length === 0)
                utilsStore.ShowModal('Info', 'No se realizaron cambios', 'info')
            else{
                const updated = await userStore.UpdateUser(props.targetUser['id'], cleanUserData)
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

const ChangeDate = (async (data) => {
    binnacleFetched.value = false
    await binnacleStore.FetchBinnacleOfUserBetweenDates(props.targetUser.id, data['initial_date'], data['final_date'])
    binnacleFetched.value = true    
})

const ResetBinnacle = (async () => {
    binnacleFetched.value = false
    await binnacleStore.FetchBinnacleOfUser(props.targetUser.id)
    binnacleFetched.value = true
})

</script>

<template>
    <form class="row m-0 p-0 justify-content-around align-items-start" @submit.prevent="ValidateForm">
        <template v-if="mounted.value === false">
            <LoadingGadget/>
        </template>
        <template v-else>
            <div class="col-12 row p-4 pt-5 fs-4 justify-content-around hide-up animated-1">
                <div class="col-12 col-lg-8 p-2 row myForm shadowed-l rounded lb-bg-terciary-ul justify-content-center">   
                    
                    <template v-if="Object.keys(props.targetUser).length !== 0">
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="created_at"><strong>Fecha de creación</strong></label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12 col-lg-8">
                                    <input type="date" class="myInput" minlength="4" id="created_at" :value="props.targetUser.created_at" disabled>
                                </div>
                            </div>
                        </div>
                    </template>

                    <template v-if="selfUser === false">
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="nickname"><strong>Nickname</strong></label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12 col-lg-8">
                                    <input type="text" class="myInput" maxlength="50" minlength="4" id="nickname" v-model="userNickname">
                                </div>
                            </div>
                        </div>
                    </template>
                    <template v-else>
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="nickname"><strong>Nickname</strong></label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12 col-lg-8">
                                    {{ props.targetUser.nickname }}
                                </div>
                            </div>
                        </div>
                    </template>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="username"><strong>Usuario</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12 col-lg-8">
                                <input type="text" class="myInput" maxlength="50" minlength="6" id="username" v-model="userUsername">
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="password"><strong>Contraseña</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12 col-lg-8">
                                <input type="password" class="myInput" maxlength="50" minlength="8" id="password" v-model="userPassword">
                            </div>
                        </div>
                    </div>

                    <div :class="formRowStyle">
                        <div :class="labelContainerStyle">
                            <label :class="labelStyle" for="passwordConfirm"><strong>Repetir contraseña</strong></label>
                        </div>
                        <div :class="inputContainerStyle">
                            <div class="row col-12 col-lg-8">
                                <input type="password" class="myInput" maxlength="50" minlength="8" id="passwordConfirm" v-model="userPasswordConfirm">
                            </div>
                        </div>
                    </div>

                    <template v-if="selfUser === false">
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="gender"><strong>Tipo</strong></label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
    
                                    <div 
                                    v-if="sessionStore.userData.permissons.includes('Editor')"
                                    class="row col-12 col-lg-5 m-0 p-0 my-1"
                                    >
                                        <label class="col-6 text-end text-lg-center" for="level-editor">Editor</label>
                                        <input class="col-1 my-auto" type="radio" id="level-editor" name="gender" value="Editor" v-model="userLevel">
                                    </div>
                                    <div 
                                    v-if="sessionStore.userData.permissons.includes('Admin')"
                                    class="row col-12 col-lg-5 m-0 p-0 my-1"
                                    >
                                        <label class="col-8 text-end text-lg-center" for="level-admin">Administrador</label>
                                        <input class="col-1" type="radio" id="level-admin" name="gender" value="Admin" v-model="userLevel">
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="active"><strong>Activo</strong></label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
                                    <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                                        <input class="col-1 mx-auto mx-lg-0" type="checkbox" id="active" name="active" value="1" v-model="userActive">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template>
                    <template v-else>
                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="active"><strong>Tipo</strong></label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
                                    <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                                        {{ props.targetUser.level }}
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div :class="formRowStyle">
                            <div :class="labelContainerStyle">
                                <label :class="labelStyle" for="active"><strong>Activo</strong></label>
                            </div>
                            <div :class="inputContainerStyle">
                                <div class="row col-12">
                                    <div class="row col-12 col-lg-5 m-0 p-0 my-1">
                                        {{ props.targetUser.active === 1 ? 'Sí' : 'No' }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template>

                           

                    <div class="row m-0 p-0 justify-content-center my-2 mt-5">
                        <div class="row m-0 p-0 col-12 justify-content-center">
                            <button class="col-6 col-lg-3 myBtn terciary-btn shadowed-l h3">
                                {{ Object.keys(props.targetUser).length === 0 ? 'Registrar ' : 'Modificar ' }}
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

                <template v-if="Object.keys(props.targetUser).length !== 0">
                    <template v-if="sessionStore.userData.permissons.includes('Bitácora')">
                        <div class="col-10 mt-5 p-2 row myForm shadowed-l rounded lb-bg-terciary-ul justify-content-center">
    
                            <h2 class="w-100 text-center h1 my-3 fw-bold">
                                Historial de acciones de {{ props.targetUser.nickname }}
                            </h2>
                            <template v-if="binnacleFetched === false">
                                <LoadingGadget/>
                            </template>
                            <template v-else>
                                <div class="w-100 p-2 fs-6">
                                    <BinnacleTable
                                    :binnacle="binnacleStore.binnacle"
                                    @ChangeDate="ChangeDate"
                                    @ResetBinnacle="ResetBinnacle"
                                    />
                                </div>
                            </template>
                        </div>            
                    </template>
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