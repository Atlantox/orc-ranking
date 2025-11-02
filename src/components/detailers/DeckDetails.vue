<script setup>
import { ref } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';
import { onMounted } from 'vue';

import LoadingGadget from '../myGadgets/LoadingGadget.vue';

import TournamentResultTable from '../tables/TournamentResultTable.vue';

import useSeasonStore from '@/stores/seasons';
import useDeckStore from '@/stores/decks';
import usetournamentStore from '@/stores/tournaments';

const seasonStore = useSeasonStore()
const deckStore = useDeckStore()
const tournamentStore = usetournamentStore()

const deckStatistics = ref(undefined)
const selectedSeason = ref('')

const props = defineProps({
  'targetDeck': {type: Object, default: {}}
})

onMounted(async () => {
  deckStatistics.value = undefined
  await seasonStore.FetchSeasons()
  const currentSeason = seasonStore.seasons[seasonStore.seasons.length - 1].id
  selectedSeason.value = currentSeason
  await tournamentStore.FetchTournamentsResultsOfDeck(props.targetDeck.id, currentSeason)
  deckStatistics.value = await deckStore.GetDeckStatistics(props.targetDeck.id, currentSeason)
  OnAppearAnimation('hide-up')
})

const FetchTournamentsOfDeckOfSeason = (async () => {
  deckStatistics.value = undefined
  const seasonValue = selectedSeason.value === '' ? null : selectedSeason.value
  await tournamentStore.FetchTournamentsResultsOfDeck(props.targetDeck.id, seasonValue)
  deckStatistics.value = await deckStore.GetDeckStatistics(props.targetDeck.id, seasonValue)
})

</script>

<template>
  <div class="hide-up animated-1 row w-100 m-0 p-0 justify-content-center align-items-start p-1 p-lg-4">
    <div class="row m-0 p-0 col-11 col-lg-8 shadowed-l rounded bg-dark-grey justify-content-around my-4"> 
      
      <div class="col-12">
        <div class="row justify-content-center fs-1 text-center">
          <article 
          v-for="color in props.targetDeck['colors']"
          :key="color"
          class="col-3 p-2"
          >
            <i :class="'fa fa-circle text-' + color"></i>
          </article>
        </div>
      </div>

      <div class="row m-0 p-0 col-12 p-3 text-white">
        <template v-if="deckStatistics === undefined">
          <LoadingGadget/>
        </template>
        <div v-else class="row m-0 p-0 col-12 h3 text-white justify-content-around flex-wrap">
          

          <template v-if="deckStatistics.length > 0">
            <template v-for="statistic in deckStatistics">
              <article class="row col-12 col-lg-6 m-0 p-2">
                <table class="col-12 table border-green text-white">
                  <thead class="text-center bg-black ">
                    <tr>
                      <th class="border-green" colspan="2">{{ statistic.format }}</th>
                    </tr>
                  </thead>
                    <tr>
                      <td class="odd p-1 border-green text-end orc-font p-2">Participaciones</td>
                      <td class="odd p-1 border-green p-2">{{ statistic.tournaments }}</td>
                    </tr>
                    <tr>
                      <td class="even p-1 border-green text-end orc-font p-2">Victorias</td>
                      <td class="even p-1 border-green p-2">{{ statistic.wins }}</td>
                    </tr>
                    <tr>
                      <td class="odd p-1 border-green text-end orc-font p-2">Winrate</td>
                      <td class="odd p-1 border-green p-2">
                        {{ (statistic.wins === '0' || statistic.wins === null) ? 0 : (statistic.wins * 100) / statistic.tournaments }}%
                      </td>
                    </tr>
                    <tr>
                      <td class="even p-1 border-green text-end orc-font p-2">Promedio de puntos</td>
                      <td class="even p-1 border-green p-2">
                        {{ parseFloat(statistic.avg_points).toFixed(2) }}
                      </td>
                    </tr>
                    <tr>
                      <td class="odd p-1 border-green text-end orc-font p-2">Puntos totales</td>
                      <td class="odd p-1 border-green p-2">
                        {{ (statistic.points === null ? 0 : statistic.points) + ' (' + (statistic.points_percent === null ? 0 : parseFloat(statistic.points_percent).toFixed(2)) + '%)' }}
                      </td>
                    </tr>                    
                </table>
              </article>
            </template>          
          </template>
          <template v-else>
              <h2 class="text-danger text-center">Sin participaciones en la temporada {{ selectedSeason }}</h2>
          </template>
        </div>
      </div>
    </div>
  </div>

  <div class="row m-0 p-0 col-12 justify-content-center">
    <div class="col-11 bg-grey shadowed-l pt-4">
      <h2 class="w-100 text-center text-green fs-1 m-0">
        Torneos de {{ targetDeck.name }}
      </h2>
      <template v-if="seasonStore.seasons === undefined">
        <LoadingGadget/>
      </template>
      <div v-else class="row col-100 m-0 p-0 fs-5 p-3 justify-content-center justify-content-lg-start">
        <h3 class="col-100 text-white text-center text-lg-start">
          Filtrar por temporada
        </h3>
        <div class="col-6 col-lg-2 fs-6 px-1 px-lg-5">
          <select class="myInput px-2 w-100 fs-4 text-center" id="season-select" @change="FetchTournamentsOfDeckOfSeason" v-model="selectedSeason">
            <option 
            v-for="season in seasonStore.seasons"
            :key="season.id"
            :value="season.id"
            :selected="parseInt(season.id) === parseInt(selectedSeason)"
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