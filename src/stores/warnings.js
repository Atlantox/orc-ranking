import { defineStore } from 'pinia'

import ApiConfig from '@/stores/config.js'

import useUtilsStore from './utils'
import useSessionStore from '@/stores/session.js'

const apiConfig = new ApiConfig()
const useWarningStore = defineStore('warnings', {
    state: () => {
        return {
            warnings: undefined
        }
    },
    actions:{
        async CreateWarning(warningData){
            const sessionStore = useSessionStore()
            let result = {}
            try{
                let url = apiConfig.base_url + '/warnings'
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'POST',
                    headers: fetchHeaders,
                    body: JSON.stringify(warningData)
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                result = await json                
            }
            catch(error){
                result = {success: false, message: 'Ocurrió un error inesperado al crear el warning: ' + error.message}
            }

            return result
        },

        async FetchWarnings(){
            this.warnings = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/warnings'
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
                    this.warnings = result.warnings
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los warnings: ' + error.message, 'error')
            }
        },

        async FetchCurrentWarnings(){
            this.warnings = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/warnings/current'
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
                    this.warnings = result.warnings
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los warnings: ' + error.message, 'error')
            }
        },

        async FetchWarningsBySeason(seasonId){
            this.warnings = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/warnings/season/' + seasonId
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
                    this.warnings = result.warnings
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los warnings: ' + error.message, 'error')
            }
        },

        async FetchWarningById(id){
            var targetWaning = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()

            try{
                let url = apiConfig.base_url + '/warnings/' + id
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
                if(result.success){
                    targetWaning = result.data                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar el warning solicitado: ' + error.message, 'error')
            }

            
            return targetWaning
        },

        async DeleteWarning(warningId){
            const sessionStore = useSessionStore()
            let result = {}
            try{
                let url = apiConfig.base_url + '/warnings/' + warningId
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'DELETE',
                    headers: fetchHeaders,
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                result = await json                
            }
            catch(error){
                result = {success: false, message: 'Ocurrió un error inesperado al intentar borrar el warning: ' + error.message}
            }

            return result
        },
    }
})

export default useWarningStore