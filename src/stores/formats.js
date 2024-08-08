import { defineStore } from 'pinia'
import ApiConfig from '@/stores/config.js'

import useUtilsStore from './utils'
import useSessionStore from '@/stores/session.js'

const apiConfig = new ApiConfig()

const useFormatStore = defineStore('formats', {
    state: () => {
        return {
            formats: undefined,
        }
    },
    actions:{
        async CreateFormat(formatData){
            const sessionStore = useSessionStore()
            let result = {}
            try{
                let url = apiConfig.base_url + '/formats'
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'POST',
                    headers: fetchHeaders,
                    body: JSON.stringify(formatData)
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                result = await json                
            }
            catch(error){
                result = {success: false, message: 'Ocurrió un error inesperado al crear el formato: ' + error.message}
            }

            return result
        },

        async FetchFormatById(id){
            var targetFormat = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/formats/' + id
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
                    targetFormat = result.format                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar el formato solicitado: ' + error.message, 'error')
            }

            return targetFormat
        },

        async FetchFormats(){
            this.formats = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/formats'
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
                    this.formats = result.formats
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los formatos: ' + error.message, 'error')
            }
        },

        async UpdateFormat(formatId, formatData){
            const sessionStore = useSessionStore()
            let result = {}
            try{
                let url = apiConfig.base_url + '/formats/' + formatId
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'PUT',
                    headers: fetchHeaders,
                    body: JSON.stringify(formatData)
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                result = await json                
            }
            catch(error){
                result = {success: false, message: 'Ocurrió un error inesperado al intentar actualizar el formato: ' + error.message}
            }

            return result
        },
    }
})

export default useFormatStore