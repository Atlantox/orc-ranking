<script setup>
import { ref } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';
import { onMounted } from 'vue';

import LoadingGadget from '../myGadgets/LoadingGadget.vue';

import TournamentResultTable from '../tables/TournamentResultTable.vue';

import useSeasonStore from '@/stores/seasons';
import usePlayerStore from '@/stores/players';
import usetournamentStore from '@/stores/tournaments';

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-7'
const labelStyle = 'text-center text-green text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-5 justify-content-center justify-content-md-start'

const seasonStore = useSeasonStore()
const playerStore = usePlayerStore()
const tournamentStore = usetournamentStore()

const playerStatistics = ref(undefined)
const selectedSeason = ref('')

const props = defineProps({
  'targetPlayer': {type: Object, default: {}}
})

onMounted(async () => {
  playerStatistics.value = undefined
  await seasonStore.FetchSeasons()
  const currentSeason = seasonStore.seasons[seasonStore.seasons.length - 1].id
  await tournamentStore.FetchTournamentsResultsOfPlayer(props.targetPlayer.id, currentSeason)
  playerStatistics.value = await playerStore.GetPlayerStatistics(props.targetPlayer.id, currentSeason)
  OnAppearAnimation('hide-up')
})

const FetchTournamentsOfPlayerOfSeason = (async () => {
  playerStatistics.value = undefined
  const seasonValue = selectedSeason.value === '' ? null : selectedSeason.value
  await tournamentStore.FetchTournamentsResultsOfPlayer(props.targetPlayer.id, seasonValue)
  playerStatistics.value = await playerStore.GetPlayerStatistics(props.targetPlayer.id, seasonValue)
})

</script>

<template>
  <div class="hide-up animated-1 row w-100 m-0 p-0 justify-content-center align-items-start p-1 p-lg-4">
    <div class="row m-0 p-0 col-11 col-lg-8 shadowed-l rounded bg-dark-grey justify-content-around my-4">      
      <div class="row m-0 p-0 col-12 col-lg-6 p-3 text-white">
        <template v-if="playerStatistics === undefined">
          <LoadingGadget/>
        </template>
        <div v-else class="row m-0 p-0 col-12 h3 text-white">
          <div :class="formRowStyle">
              <div :class="labelContainerStyle">
                  <label :class="labelStyle">Torneos participados</label>
              </div>
              <div :class="inputContainerStyle">
                <div class="row col-12">
                  <div class="row col-12 m-0 p-0 my-1">
                    {{ playerStatistics.tournaments }}
                  </div>
                </div>
              </div>
            </div>

            <div :class="formRowStyle">
              <div :class="labelContainerStyle">
                  <label :class="labelStyle">Victorias</label>
              </div>
              <div :class="inputContainerStyle">
                <div class="row col-12">
                  <div class="row col-12 m-0 p-0 my-1">
                    {{ playerStatistics.wins == null ? 0 : playerStatistics.wins }}
                  </div>
                </div>
              </div>
            </div>

            <div :class="formRowStyle">
              <div :class="labelContainerStyle">
                  <label :class="labelStyle">Winrate</label>
              </div>
              <div :class="inputContainerStyle">
                <div class="row col-12">
                  <div class="row col-12 m-0 p-0 my-1">
                    {{ (playerStatistics.wins === '0' || playerStatistics.wins === null) ? 0 : (playerStatistics.wins * 100) / playerStatistics.tournaments }}%
                  </div>
                </div>
              </div>
            </div>

            <div :class="formRowStyle">
              <div :class="labelContainerStyle">
                  <label :class="labelStyle">Puntos totales</label>
              </div>
              <div :class="inputContainerStyle">
                <div class="row col-12">
                  <div class="row col-12 m-0 p-0 my-1">
                    {{ (playerStatistics.points === null ? 0 : playerStatistics.points) + ' (' + (playerStatistics.points_percent === null ? 0 : playerStatistics.points_percent) + '%)' }}
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </div>

  <div class="row m-0 p-0 col-12 justify-content-center">
    <div class="col-11 bg-grey shadowed-l pt-4">
      <h2 class="w-100 text-center text-green fs-1 m-0">
        Torneos de {{ targetPlayer.name }}
      </h2>
      <template v-if="seasonStore.seasons === undefined">
        <LoadingGadget/>
      </template>
      <div v-else class="row w-100 m-0 p-0 fs-5 p-3">
        <h3 class="w-100 text-white">
          Filtrar por temporada
        </h3>
        <div class="col-6 col-lg-2 fs-6 px-5">
          <select class="myInput px-2 w-100 fs-4 text-center" id="season-select" @change="FetchTournamentsOfPlayerOfSeason" v-model="selectedSeason">
            <option 
            v-for="season in seasonStore.seasons"
            :key="season.id"
            :value="season.id"
            class="align-middle text-center"
            >
              Season {{ season.name }}
            </option>
          </select>
        </div>
      </div>
    
      <template
      v-if="tournamentStore.results === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>        
        <div class="row col-12 m-0 p-3 px-5 table-container text-green">
          <TournamentResultTable
            :results="tournamentStore.results"
            />
        </div>
      </template>
    </div>
  </div>

</template>

<style scoped>

</style>