import { ref } from 'vue'
import { defineStore } from 'pinia'
import Apiconfig from '@/stores/config.js'
import useUtilsStore from './utils'

const apiConfig = new Apiconfig()


const useSessionStore = defineStore('session', {
  state: () => {
    return {
      authenticated: false,
      lastLoginDate: null,
      token: '',
      userData: {},
      loginResult: ref({})
    }
  },
  actions:{
    async TryLogin(username, password){
      const sessionStore = useSessionStore()
      try{
          let url = apiConfig.base_url + '/login'
          var fetchHeaders = {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
          }

          if (sessionStore.authenticated === true)
              fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

          let fetchConfig = {
              method: 'POST',
              headers: fetchHeaders,
              body:JSON.stringify({
                'username': username,
                'password': password
              })
          }

          let response = await fetch(url, fetchConfig)
          let json = await response.json()
          let result = await json
          this.loginResult.value = result
      }
      catch(error){
          this.loginResult.value = 'Error: ' + error.message
      }
    },

    async MyUserIsActive(){
      const sessionStore = useSessionStore()
      var userIsActive = false
      try{
          let url = apiConfig.base_url + '/my_user'
          var fetchHeaders = {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
          }

          if (sessionStore.authenticated === true)
              fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

          let fetchConfig = {
              method: 'GET',
              headers: fetchHeaders
          }

          let response = await fetch(url, fetchConfig)
          let json = await response.json()
          let result = await json
          if(result.success)
            userIsActive = result.data.active === 1
            
      }
      catch(error){
          return false
      }

      return userIsActive
    },

    DestroySession(){
      const utilsStore = useUtilsStore()
      this.token = ''
      this.authenticated = false
      this.userData = {}
      utilsStore.ShowModal('Success', 'Sesión cerrada', 'success')
    },
  },
  
  persist: true,
})

export default useSessionStore