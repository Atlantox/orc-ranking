<script setup>
import { ref, onMounted } from 'vue'

import OnAppearAnimation from '@/utils/ElegantDisplayer';
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue';

import useTournamentStore from '@/stores/tournaments';
import useSeasonStore from '@/stores/seasons';
import useFormatStore from '@/stores/formats';

const tournamentStore = useTournamentStore()
const seasonStore = useSeasonStore()
const formatStore = useFormatStore()

const fetchReady = ref(false)
const currentSeason = ref(undefined)
const lastTournament = ref(undefined)
const tournamentsRanking = ref(undefined)
const playedFormats = ref(undefined)
const seasonStatistics = ref(undefined)

onMounted( async () => {
  currentSeason.value = await seasonStore.GetCurrentSeason()
  await seasonStore.FetchSeasons()
  playedFormats.value = await formatStore.GetPlayedFormatsInSeason(currentSeason.value['id'])
  lastTournament.value = await tournamentStore.GetLastTournament()

  await FetchRanking()

  fetchReady.value = await true
})

const FetchRanking = ( async() => {
  tournamentsRanking.value = undefined
  let targetSeasonId = currentSeason.value['id']
  let targetGameFormat = null
  if(fetchReady.value === true){
    targetSeasonId = document.getElementById('season-select').value
    targetGameFormat = document.getElementById('format-select').value
  }
  else{
    // If the only played format is one, take that format
    if(playedFormats.value.length === 1)
      targetGameFormat = playedFormats.value[0]['id']
    else if(playedFormats.value.length > 1){
      // If are more than 1 played format, priorize Coliseo, otherwise take the first in the array
      for(let i = 0; i < playedFormats.value.length; i++){
        if(playedFormats.value[i]['name'] === 'Coliseo'){
          targetGameFormat = playedFormats.value[i]['id']
          break;
        }
      }

      if (targetGameFormat === null)
        targetGameFormat = playedFormats.value[0]['id']
    }
  }

  tournamentsRanking.value = await tournamentStore.GetTournamentsRankingOfSeasonAndFormat(targetSeasonId, targetGameFormat)
  seasonStatistics.value = await tournamentStore.GetSeasonStatistics(targetSeasonId)

  fetchReady.value = await true
  OnAppearAnimation('hide-up')
})

const FetchSeasonStatistics = ((seasonId) => {
  alert(seasonId.target)
})

</script>

<template>
  <main class="row m-0 p-0 justify-content-center bg-black">
    <section class="row col-12 m-0 p-0">
      <figure class="m-0 p-0 my-hero d-flex align-items-center justify-content-center animated-2 shadowed-h" id="my-hero">
        <img class="w-100 text-center my-hero" src="@/assets/images/progenitus.jpg" alt="">
        <h1 class="h1 fw-bold text-center outline-black position-absolute text-green hide-up animated-1">
          The Orc's Ranking
        </h1>
      </figure>
    </section>

    <section class="row col-12 m-0 p-0 justify-content-around align-items-center flex-wrap bg-dark-grey text-green">
      
        <div class="col-12 m-0 p-0 d-flex justify-content-center fs-5 flex-wrap">
          <template v-if="seasonStore.seasons === undefined">
            <LoadingGadget />
          </template>
          <template v-else>
            <div class="col-12 text-center py-4 fs-3 hide-up animated-1 d-flex justify-content-center">
              <select class="myInput px-4 mx-3" id="season-select" @change="FetchRanking(); FetchSeasonStatistics();">
                <option 
                v-for="season in seasonStore.seasons"
                :key="season.id"
                :value="season.id"
                :selected="season.active === 1"
                class="align-middle"
                >
                  Season {{ season.name }}
                </option>
              </select>

              <select class="myInput px-4 mx-3" id="format-select" @change="FetchRanking()">
                <option 
                v-for="format in playedFormats"
                :key="format.id"
                :value="format.id"
                :selected="format.name === 'Coliseo'"
                class="align-middle"
                >
                  {{ format.name }}
                </option>
              </select>
            </div>
          </template>

          <template v-if="tournamentsRanking === undefined">
            <LoadingGadget />
          </template>
          <template v-else>
            <div class="row col-12 m-0 p-0 justify-content-center hide-up animated-1">
              <div class="col-12 col-md-3 text-center py-4 side-border-green">
                <h3 class="w-100 text-center text-green">
                  Jugadores
                </h3>
                <article 
                class="row m-0 p-0 my-1"
                v-for="player, index in tournamentsRanking.players"
                :key="index"
                >
                  <span class="col-6 text-end">{{ player.name }}</span>
                  <span class="col-6 text-start my-auto">
                    <div class="percent" :style="'width:' + player.percent + '%'">
                      {{ player.percent }}%
                    </div>
                  </span>
                </article>
              </div>
      
              <div class="col-12 col-md-5 text-center py-4 side-border-green ">
                <h3 class="w-100 text-center text-green">
                  Decks
                </h3>
                <article 
                class="row m-0 p-0 my-1"
                v-for="deck, index in tournamentsRanking.decks"
                :key="index"
                >
                  <span class="col-6 text-end">{{ deck.name }}</span>
                  <span class="col-6 text-start my-auto">
                    <div class="percent" :style="'width:' + deck.percent + '%'">
                      {{ deck.percent }}%
                    </div>
                  </span>
                </article>
              </div>
      
              <div class="col-12 col-md-3 text-center py-4 side-border-green">
                <h3 class="w-100 text-center text-green">
                  Colores
                </h3>
                <article 
                class="row m-0 p-0 my-1"
                v-for="color, index in tournamentsRanking.colors"
                :key="index"
                >
                  <span class="col-4 text-end">{{ color.color }}</span>
                  <span class="col-8 text-start my-auto">
                    <div class="percent" :style="'width:' + color.percent + '%'">
                      {{ color.percent }}%
                    </div>
                  </span>
                </article>
              </div>
            </div>
          </template>
        </div>
    </section>


    <section class="row col-12 m-0 p-0 mt-5 justify-content-center align-items-center flex-column flex-lg-row shadowed-n services-section">
      <template v-if="seasonStatistics === undefined">
        <LoadingGadget />
      </template>
      <template v-else>
        <div class="row col-12 col-lg-7 m-0 p-0 d-flex justify-content-center text-white py-4  hide-up animated-1">
          <div class="row m-0 p-0 col-12 col-lg-4 justify-content-center my-3">
            <table class="col-10 text-white fs-4">
              <thead class="text-center bg-grey">
                <tr>
                  <th class="p-1 border-green fs-1 py-2" colspan="2">Torneos</th>
                </tr>
              </thead>
              <tbody>
                <tr
                v-for="tournament, index in seasonStatistics.tournaments"
                :key="index"
                class="text-center"
                >
                  <td class="p-1 border-green">{{ tournament['format'] }}</td>
                  <td class="p-1 border-green">{{ tournament['count'] }}</td>
                </tr>            
              </tbody>
            </table>
          </div>

          <div class="row m-0 p-0 col-12 col-lg-4 justify-content-center my-3">
            <table class="col-10 text-white fs-4">
              <thead class="text-center bg-grey">
                <tr>
                  <th class="p-1 border-green fs-1 py-2" colspan="2">Participantes</th>
                </tr>
              </thead>
              <tbody>
                <tr
                v-for="participant, index in seasonStatistics.participants"
                :key="index"
                class="text-center"
                >
                  <td class="p-1 border-green">{{ participant['format'] }}</td>
                  <td class="p-1 border-green">{{ participant['count'] }}</td>
                </tr>            
              </tbody>
            </table>
          </div>

          <div class="row m-0 p-0 col-12 col-lg-4 justify-content-center my-3">
            <table class="col-10 text-white fs-4">
              <thead class="text-center bg-grey">
                <tr>
                  <th class="p-1 border-green fs-1 py-2" colspan="2">Personas</th>
                </tr>
              </thead>
              <tbody>
                <tr
                v-for="person, index in seasonStatistics.persons"
                :key="index"
                class="text-center"
                >
                  <td class="p-1 border-green">{{ person['format'] }}</td>
                  <td class="p-1 border-green">{{ person['count'] }}</td>
                </tr>            
              </tbody>
            </table>
          </div>

        </div>
      </template>
    </section>

    <section class="row col-12 m-0 p-0 py-4 justify-content-center align-items-start my-5 bg-dark-grey text-green">
      <div class="col-12 text-center my-3 p-0">
        <h2 class="h1 text-green">Último torneo </h2>  
        
      </div>

      <template v-if="lastTournament === undefined">
        <LoadingGadget />
      </template>
      <div v-else class="row m-0 p-0 col-12 text-center justify-content-center align-items-start p-0 px-4 hide-up animated-1">
        <template v-if="Object.keys(lastTournament).length === 0">
            <h2 class="text-center w-100 text-green">
              No hay torneos registrados esta temporada (aún)
            </h2>
        </template>
        <div v-else  class="row col-12 m-0 p-0 justify-content-center">
          <div class="row m-0 p-0 col-12 col-lg-5 text-center justify-content-center px-4 my-2">
          <table class="col-10 text-white fs-4">
            <tr>
              <td class="p-1 border-green bg-grey orc-font py-2">Fecha</td>
              <td class="p-1 border-green">{{ lastTournament.data.date }}</td>
            </tr>
            <tr>
              <td class="p-1 border-green bg-grey orc-font py-2">Formato</td>
              <td class="p-1 border-green">{{ lastTournament.data.format }}</td>
            </tr>
            <tr>
              <td class="p-1 border-green bg-grey orc-font py-2">Participantes</td>
              <td class="p-1 border-green">{{ lastTournament.results.length }}</td>
            </tr>
            <tr>
              <td class="p-1 border-green bg-grey orc-font py-2">Ganador</td>
              <td class="p-1 border-green">{{ lastTournament.data.winner }}</td>
            </tr>
            <tr>
              <td class="p-1 border-green bg-grey orc-font py-2">Observación</td>
              <td class="p-1 border-green">{{ lastTournament.data.observation === undefined ? 'Ninguna' : lastTournament.data.observation }}</td>
            </tr>
            <tr>
              <td class="p-1 border-green bg-grey orc-font py-2">Presencia de colores</td>
              <td class="p-1 border-green">
                <ul class="w-100 list-unstyled m-0 p-0">
                  <li 
                  v-for="color in lastTournament.colors"
                  :key="color.name"
                  class=""
                  >
                    <i :class="'fa fa-circle text-' + color.color"></i>&nbsp;{{ color.percent }}% ({{ color.quantity }})
                  </li>
                </ul>
              </td>
            </tr>
          </table>
        </div>
  
        <div class="row col-12 m-0 p-0 col-lg-7 text-center justify-content-center my-2">
          <table class="col-10">
            <thead class="fs-4 text-white">
              <tr>
                <th class="border-green p-1 py-3 fw-normal bg-grey">Posición</th>
                <th class="border-green p-1 fw-normal bg-grey">Jugador</th>
                <th class="border-green p-1 fw-normal bg-grey">Deck</th>
                <th class="border-green p-1 fw-normal bg-grey">Puntos/Victorias</th>
              </tr>
            </thead>
            <tbody class="fs-5 text-white">
              <tr v-for="participant, index in lastTournament.results"
              :key="index"
              >
                <td class="border-green p-1 py-2">{{ index + 1 }}</td>
                <td class="border-green p-1">{{ participant.player }}</td>
                <td class="border-green p-1">{{ participant.deck }}</td>
                <td class="border-green p-1">{{ participant.wins }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        </div>      
      </div>
    </section>
  </main>
</template>

<style scoped lang="scss">
.my-hero{
  width:100vw;
  height:600px;  
}

h1{
  font-size:80px;
  transition:0.8s;
  color: rgb(87, 211, 97);
  letter-spacing: 2px;
}

@media (max-width: 720px) {
    .my-hero{
        height:260px;
    }

    h1{
        font-size:40px;
    }

    h2{
      font-size:40px !important;
    }
}

.services-section{
  background-position:center;
}

h2{
  font-size:70px;
}

.percent{
  background-color:rgba(255, 184, 92, 0.322);
}

</style>
