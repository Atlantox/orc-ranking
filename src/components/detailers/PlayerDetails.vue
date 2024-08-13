<script setup>
import { ref } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';
import { onMounted } from 'vue';

import LoadingGadget from '../myGadgets/LoadingGadget.vue';

import TournamentTable from '../tables/TournamentTable.vue';

import useSeasonStore from '@/stores/seasons';
import usePlayerStore from '@/stores/players';
import usetournamentStore from '@/stores/tournaments';

const labelStyle = 'fw-bold text-end p-2 w-50 w-lg-auto text-green'

const seasonStore = useSeasonStore()
const playerStore = usePlayerStore()
const tournamentStore = usetournamentStore()

const playerStatistics = ref({})
const selectedSeason = ref('')

const props = defineProps({
  'targetPlayer': {type: Object, default: {}}
})

onMounted(async () => {
  await seasonStore.FetchSeasons()
  const currentSeason = seasonStore.seasons[seasonStore.seasons.length - 1].id
  await tournamentStore.FetchTournamentsOfPlayer(props.targetPlayer.id)
  playerStatistics.value = await playerStore.GetPlayerStatistics(props.targetPlayer.id, currentSeason)
  OnAppearAnimation('hide-up')
})

const FetchTournamentsOfPlayerOfSeason = (async () => {
  playerStatistics.value = undefined
  const seasonValue = selectedSeason.value === '' ? null : selectedSeason.value
  await tournamentStore.FetchTournamentsOfPlayer(props.targetPlayer.id, seasonValue)
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
          <table >
            <tr>
              <td :class="labelStyle">Torneos participados:</td>
              <td>{{ playerStatistics.tournaments }}</td>
            </tr>
            <tr>
              <td :class="labelStyle">Victorias:</td>
              <td>{{ playerStatistics.wins }}</td>
            </tr>
            <tr>
              <td :class="labelStyle">Winrate:</td>
              <td>{{ playerStatistics.wins === '0' ? 0 : playerStatistics.tournaments / playerStatistics.wins }}%</td>
            </tr>
            <tr>
              <td :class="labelStyle">Puntos:</td>
              <td>{{ playerStatistics.points }} ({{ playerStatistics.points_percent }}%)</td>
            </tr>
          </table>
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
      v-if="tournamentStore.tournaments === undefined">
        <LoadingGadget/>
      </template>
      <template v-else>        
        <div class="row col-12 m-0 p-3 px-5 table-container text-green">
          <TournamentTable
            :tournaments="tournamentStore.tournaments"
            />
        </div>
      </template>
    </div>
  </div>

</template>

<style scoped>

</style>