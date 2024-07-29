<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue'

import useUserStore from '@/stores/users'
import useSessionStore from '@/stores/session'

import UserForm from '@/components/forms/UserForm.vue'

const userStore = useUserStore()
const sessionStore = useSessionStore()

const fetchReady = ref(false)
const targetUser = ref({})

onMounted( async () => {
    fetchReady.value = false
    targetUser.value = await userStore.FetchUserById(sessionStore.userData.id)
    fetchReady.value = true
})

</script>

<template>
  <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
    <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
      <BackButtonGadget :back_to="'dashboard'"/>
    </div>
  </div>
  <PageTitle
    :title="'Mi cuenta'"
  />
  <template v-if="fetchReady === false">
    <LoadingGadget />
  </template>
  <template v-else>    
    <UserForm
    :targetUser = "targetUser"
    />
  </template>
</template>