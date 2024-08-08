import { defineStore } from 'pinia'
import ApiConfig from '@/stores/config.js'

import useUtilsStore from './utils'
import useSessionStore from '@/stores/session.js'

const apiConfig = new ApiConfig()

const useDeckStore = defineStore('decks', {
    state: () => {
        return {
            decks: undefined,
            colors: undefined
        }
    },
    actions:{
        async CreateDeck(deckData){
            const sessionStore = useSessionStore()
            let result = {}
            try{
                let url = apiConfig.base_url + '/decks'
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'POST',
                    headers: fetchHeaders,
                    body: JSON.stringify(deckData)
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                result = await json                
            }
            catch(error){
                result = {success: false, message: 'Ocurrió un error inesperado al crear el deck: ' + error.message}
            }

            return result
        },

        async FetchDeckById(id){
            var targetDeck = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/decks/' + id
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
                    targetDeck = result.deck                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar el deck solicitado: ' + error.message, 'error')
            }

            return targetDeck
        },

        async FetchDecks(){
            this.decks = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/decks'
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
                    this.decks = result.decks
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los decks: ' + error.message, 'error')
            }
        },

        async FetchColors(){
            this.colors = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/colors'
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
                    this.colors = result.colors
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los colores: ' + error.message, 'error')
            }
        },

        async GetDeckCount(){
            var deckCount = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/decks/count'
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
                    deckCount = result.count                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar el número de decks: ' + error.message, 'error')
            }

            return deckCount
        },

        async UpdateDeck(deckId, deckData){
            const sessionStore = useSessionStore()
            let result = {}
            try{
                let url = apiConfig.base_url + '/decks/' + deckId
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'PUT',
                    headers: fetchHeaders,
                    body: JSON.stringify(deckData)
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                result = await json                
            }
            catch(error){
                result = {success: false, message: 'Ocurrió un error inesperado al intentar actualizar el deck: ' + error.message}
            }

            return result
        },
    }
})

export default useDeckStore