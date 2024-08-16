<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useUserStore from '@/stores/users'
import useSessionStore from '@/stores/session'

import UserForm from '@/components/forms/UserForm.vue'

const route = useRoute()
const router = useRouter()

const userStore = useUserStore()
const sessionStore = useSessionStore()

const targetUser = ref([])
const fetchReady = ref(false)

onMounted( async () => {
  fetchReady.value = false
  const recievedId = route.params.id
  
  if(recievedId !== undefined && recievedId !== ''){
    targetUser.value = await userStore.FetchUserById(recievedId)
    // TODO: problemas con el manejo de usuario propio
    if(targetUser.value.id !== sessionStore.userData.id){
      // If the user don't have permissons of the targetUser level, return it to dashboard
      if(!sessionStore.userData.permissons.includes(targetUser.level))
        router.push({name: 'dashboard'})
    }
  }
  
  fetchReady.value = true
})


</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start mt-5 pt-5">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="route.params.id === undefined || route.params.id === '' ? 'dashboard' : 'users'"/>
    </div>
  </div>

  <PageTitle
    :title="(route.params.id === undefined || route.params.id === '' ? 'Registrar nuevo ' : 'Modificar ') + 'usuario'"
  />

  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <UserForm
    :targetUser="targetUser"
    />
  </template>
</template>