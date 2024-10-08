import { defineStore } from 'pinia'
import ApiConfig from '@/stores/config.js'

import useUtilsStore from './utils'
import useSessionStore from '@/stores/session.js'

const apiConfig = new ApiConfig()

const useTournamentStore = defineStore('tournaments', {
    state: () => {
        return {
            tournaments: undefined,
            results: undefined
        }
    },
    actions:{
        async CreateTournament(tournamentData){
            const sessionStore = useSessionStore()
            let result = {}
            try{
                let url = apiConfig.base_url + '/tournaments'
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'POST',
                    headers: fetchHeaders,
                    body: JSON.stringify(tournamentData)
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                result = await json                
            }
            catch(error){
                result = {success: false, message: 'Ocurrió un error inesperado al crear el torneo: ' + error.message}
            }

            return result
        },

        async GetTournamentById(id){
            var targetTournament = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/' + id
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
                    targetTournament = result.tournament                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar el torneo solicitado: ' + error.message, 'error')
            }

            return targetTournament
        },

        async GetLastTournament(){
            var targetTournament = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/last'
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
                    targetTournament = result.tournament                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar el último torneo: ' + error.message, 'error')
            }

            return targetTournament
        },

        async FetchCurrentTournaments(){
            this.tournaments = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments'
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'GET',
                    headers: fetchHeaders,
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                let result = await json
                if(result.success){
                    this.tournaments = result.tournaments
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los torneos: ' + error.message, 'error')
            }
        },

        async FetchActiveTournaments(){
            this.tournaments = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/active'
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'GET',
                    headers: fetchHeaders,
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                let result = await json
                if(result.success){
                    this.tournaments = result.tournaments
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los torneos activos: ' + error.message, 'error')
            }
        },

        async FetchInactiveTournaments(){
            this.tournaments = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/inactive'
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'GET',
                    headers: fetchHeaders,
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                let result = await json
                if(result.success){
                    this.tournaments = result.tournaments
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los torneos inactivos: ' + error.message, 'error')
            }
        },

        async FetchInactiveTournamentsOfSeason(season){
            this.tournaments = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/inactive/' + season
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'GET',
                    headers: fetchHeaders,
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                let result = await json
                if(result.success){
                    this.tournaments = result.tournaments
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los torneos inactivos: ' + error.message, 'error')
            }
        },

        async FetchAllTournaments(){
            this.tournaments = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/all'
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'GET',
                    headers: fetchHeaders,
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                let result = await json
                if(result.success){
                    this.tournaments = result.tournaments
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar todos los torneos: ' + error.message, 'error')
            }
        },

        async FetchAllTournamentsOfSeason(season){
            this.tournaments = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/all/' + season
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'GET',
                    headers: fetchHeaders,
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                let result = await json
                if(result.success){
                    this.tournaments = result.tournaments
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar todos los torneos: ' + error.message, 'error')
            }
        },

        async FetchTournamentsOfSeason(season){
            this.tournaments = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/season/' + season
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'GET',
                    headers: fetchHeaders,
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                let result = await json
                if(result.success){
                    this.tournaments = result.tournaments
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los torneos de la temporada: ' + error.message, 'error')
            }
        },

        async FetchTournamentsOfPlayer(playerId, seasonId = null){
            this.tournaments = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/player/' + playerId
                if (seasonId !== null) url += '/' + seasonId
                
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
                    this.tournaments = result.tournaments                   
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los torneos del jugador solicitado: ' + error.message, 'error')
            }
        },

        async FetchTournamentsResultsOfPlayer(playerId, seasonId){
            this.results = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/results/player/' + playerId
                if (seasonId !== null) url += '/' + seasonId
                
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
                    this.results = result.results                   
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los resultados de torneos del jugador solicitado: ' + error.message, 'error')
            }
        },

        async FetchTournamentsResultsOfDeck(deckId, seasonId){
            this.results = undefined
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/results/deck/' + deckId
                if (seasonId !== null) url += '/' + seasonId
                
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
                    this.results = result.results                   
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar los resultados de torneos del deck solicitado: ' + error.message, 'error')
            }
        },

        async GetTournamentCount(seasonId, formatName){
            var tournamentsCount = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/count'
                if (seasonId !== null) url += '/' + seasonId

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
                    tournamentsCount = result.count                   
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar las estadísticas de torneos de la temporada: ' + error.message, 'error')
            }

            return tournamentsCount
        },

        async GetTournamentsRankingOfSeasonAndFormat(season, gameFormat){
            var ranking = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/ranking/' + season + '/' + gameFormat
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
                    ranking = result.ranking                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar el ranking de la temporada: ' + error.message, 'error')
            }

            return ranking
        },

        async GetSeasonStatistics(season){
            var statistics = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/statistics/' + season
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
                    statistics = result.statistics                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar las estadísticas de la temporada: ' + error.message, 'error')
            }

            return statistics
        },

        async GetSeasonPot(season, format){
            var pot = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/pot/' + season + '/' + format
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
                    pot = result.pot                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al calcular el pote de la temporada: ' + error.message, 'error')
            }

            return pot
        },

        async GetIndividualPlayersOfSeason(season){
            var playerCount = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/individual_players/' + season
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
                    playerCount = result.count                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar el contador de jugadores individuales de la temporada: ' + error.message, 'error')
            }

            return playerCount
        },

        async FetchTournamentsCountsOfSeason(season){
            var tournamentsCount = false
            const sessionStore = useSessionStore()
            const utilsStore = useUtilsStore()
            try{
                let url = apiConfig.base_url + '/tournaments/count/' + season
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
                    tournamentsCount = result.counts                    
                }
                else
                    utilsStore.ShowModal('Error', result.message, 'error')
            }
            catch(error){
                utilsStore.ShowModal('Error', 'Ocurrió un error inesperado al cargar las estadísticas de torneos de la temporada: ' + error.message, 'error')
            }

            return tournamentsCount
        },

        async DeactivateTournament(tournamentId){
            var result = null;
            const sessionStore = useSessionStore()
            try{
                let url = apiConfig.base_url + '/tournaments/' + tournamentId
                var fetchHeaders = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                }

                if (sessionStore.authenticated === true)
                    fetchHeaders['Authorization'] = 'Bearer ' + sessionStore.token

                let fetchConfig = {
                    method: 'DELETE',
                    headers: fetchHeaders
                }

                let response = await fetch(url, fetchConfig)
                let json = await response.json()
                result = await json                
            }
            catch(error){
                result = {success: false, message: 'Ocurrió un error inesperado al desativar el torneo: ' + error.message}
            }

            return result
        },
    }
})

export default useTournamentStore