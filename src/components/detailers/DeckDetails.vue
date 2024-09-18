<script setup>
import { ref } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';
import { onMounted } from 'vue';

import LoadingGadget from '../myGadgets/LoadingGadget.vue';

import TournamentResultTable from '../tables/TournamentResultTable.vue';

import useSeasonStore from '@/stores/seasons';
import useDeckStore from '@/stores/decks';
import usetournamentStore from '@/stores/tournaments';

const formRowStyle = 'row m-0 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-7'
const labelStyle = 'text-center text-green text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-5 justify-content-center justify-content-md-start'
const statisticNumberStyle = 'col-12 m-0 p-0 my-1 text-center text-lg-start'

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
      <div class="row m-0 p-0 col-12 p-3 text-white">
        <template v-if="deckStatistics === undefined">
          <LoadingGadget/>
        </template>
        <div v-else class="row m-0 p-0 col-12 h3 text-white">
          <div class="col-12 col-lg-7">

            <div :class="formRowStyle">
              <div :class="labelContainerStyle">
                  <label :class="labelStyle">Torneos participados</label>
              </div>
              <div :class="inputContainerStyle">
                <div class="row col-12">
                  <div :class="statisticNumberStyle">
                    {{ deckStatistics.tournaments }}
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
                  <div :class="statisticNumberStyle">
                    {{ deckStatistics.wins == null ? 0 : deckStatistics.wins }}
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
                  <div :class="statisticNumberStyle">
                    {{ (deckStatistics.wins === '0' || deckStatistics.wins === null) ? 0 : (deckStatistics.wins * 100) / deckStatistics.tournaments }}%
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
                  <div :class="statisticNumberStyle">
                    {{ (deckStatistics.points === null ? 0 : deckStatistics.points) + ' (' + (deckStatistics.points_percent === null ? 0 : deckStatistics.points_percent) + '%)' }}
                  </div>
                </div>
              </div>
            </div>

          </div> 

          <div class="col-12 col-lg-5">
            <h3 class="text-center w-100 text-green">Colores</h3>
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