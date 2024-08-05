<script setup>
import { ref, onMounted } from 'vue'

import OnAppearAnimation from '@/utils/ElegantDisplayer';
import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue';
import useTournamentStore from '@/stores/tournaments';
import useSeasonStore from '@/stores/seasons';

const tournamentStore = useTournamentStore()
const seasonStore = useSeasonStore()

const fetchReady = ref(false)
const currentSeason = ref(undefined)
const lastTournament = ref(undefined)
const tournamentsCounts = ref(undefined)
const tournamentsRanking = ref(undefined)

onMounted( async () => {
  currentSeason.value = await seasonStore.GetCurrentSeason()
  await tournamentStore.FetchTournamentsOfSeason(currentSeason.value['id'])
  await seasonStore.FetchSeasons()
  tournamentsCounts.value = await tournamentStore.FetchTournamentsCountsOfSeason(currentSeason.value['id'])
  lastTournament.value = await tournamentStore.GetLastTournament()
  fetchReady.value = true
  OnAppearAnimation('hide-up')
})
</script>

<template>
  <main class="row m-0 p-0 justify-content-center bg-black">
    <section class="row col-12 m-0 p-0">
      <figure class="m-0 p-0 my-hero d-flex align-items-center justify-content-center animated-2 shadowed-h" id="my-hero">
        <img class="w-100 text-center my-hero" src="@/assets/images/progenitus.jpg" alt="">
        <h1 class="h1 fw-bold text-center outline-black position-absolute text-green">
          The Orc's Ranking
        </h1>
      </figure>
    </section>

    <section class="row col-12 m-0 p-0 justify-content-around align-items-center flex-wrap bg-dark-grey text-green">
      <template v-if="tournamentsRanking === undefined">
        <LoadingGadget />
      </template>
      <template v-else>
        <div class="col-12 m-0 p-0 d-flex justify-content-center fs-5 flex-wrap">
          <div class="col-12 text-center py-4 fs-3">
            <select class="myInput px-4" id="season-select">
              <option 
              v-for="season in seasonStore.seasons"
              :key="season.id">
                Season {{ season.id }}
              </option>
            </select>
          </div>
          <div class="col-12 col-md-3 text-center py-4 side-border-green">
            <h3 class="w-100 text-center text-green">
              Jugadores
            </h3>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Jugador1</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:75.06%;">
                  75%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Jugador2</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:55%;">
                  55%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Jugador3</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:12%;">
                  12%
                </div>
              </span>
            </article>
          </div>
  
          <div class="col-12 col-md-3 text-center py-4 side-border-green ">
            <h3 class="w-100 text-center text-green">
              Decks
            </h3>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Deck1</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:75.06%;">
                  75%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Deck2</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:55%;">
                  55%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Deck3</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:12%;">
                  12%
                </div>
              </span>
            </article>
          </div>
  
          <div class="col-12 col-md-3 text-center py-4 side-border-green">
            <h3 class="w-100 text-center text-green">
              Colores
            </h3>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Verde</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:12%;">
                  12%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Negro</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:12%;">
                  12%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Blanco</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:12%;">
                  12%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Incoloro</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:12%;">
                  12%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Azul</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:0;">
                  0%
                </div>
              </span>
            </article>
            <article class="row m-0 p-0 my-1">
              <span class="col-4 text-end">Rojo</span>
              <span class="col-8 text-start">
                <div class="percent" style="width:0%;">
                  0%
                </div>
              </span>
            </article>
          </div>
        </div>
      </template>
    </section>


    <section class="row col-12 m-0 p-0 mt-5 justify-content-center align-items-center flex-column flex-lg-row shadowed-n services-section">
      <template v-if="tournamentsCounts === undefined">
        <LoadingGadget />
      </template>
      <template v-else>
        <div class="row col-12 col-lg-7 m-0 p-0 d-flex justify-content-center text-white py-4">
          <div class="row m-0 p-0 col-6 justify-content-center">
            <p class="h3 col-12 text-green text-center">
              Torneos totales
            </p>
            <figure class="col-5 text-center">
              <img class="col-6" src="@/assets/icons/sitemap.png" alt="bitemap">
            </figure>
            <p class="col-12 h1 text-green text-center">{{ tournamentsCounts.tournaments }}</p>
          </div>
          <div class="row m-0 p-0 col-6 justify-content-center">
            <p class="h3 col-12 text-green text-center">
              Participantes
            </p>
            <figure class="col-5 text-center">
              <img class="col-6" src="@/assets/icons/user.png" alt="bitemap">
            </figure>
            <p class="col-12 h1 text-green text-center">{{ tournamentsCounts.participants }}</p>
          </div>
        </div>
      </template>
    </section>

    <section class="row col-12 m-0 p-0 py-4 justify-content-center align-items-start my-5 bg-dark-grey text-green">
      <div class="col-12 text-center my-3">
        <h2 class="h1 text-green">Último torneo</h2>  
      </div>

      <template v-if="lastTournament === undefined">
        <LoadingGadget />
      </template>
      <template v-else>
        <div class="row m-0 p-0 col-12 text-center justify-content-center align-items-start px-4">
          <div class="row m-0 p-0 col-12 col-lg-5 text-center justify-content-center px-4">
            <table class="col-10 text-white fs-4">
              <tr>
                <td class="p-1 border-green">Fecha</td>
                <td class="p-1 border-green">{{ lastTournament.data.date }}</td>
              </tr>
              <tr>
                <td class="p-1 border-green">Formato</td>
                <td class="p-1 border-green">{{ lastTournament.data.format }}</td>
              </tr>
              <tr>
                <td class="p-1 border-green">Participantes</td>
                <td class="p-1 border-green">{{ lastTournament.results.length }}</td>
              </tr>
              <tr>
                <td class="p-1 border-green">Ganador</td>
                <td class="p-1 border-green">{{ lastTournament.data.winner }}</td>
              </tr>
              <tr>
                <td class="p-1 border-green">Presencia de colores</td>
                <td class="p-1 border-green">
                  <ul class="w-100 list-unstyled m-0 p-0">
                    <li 
                    v-for="color in lastTournament.colors"
                    :key="color.name"
                    >
                      <i :class="'fa fa-circle text-' + color.color"></i>&nbsp;{{ color.quantity }}
                    </li>
                  </ul>
                </td>
              </tr>
            </table>
          </div>
    
          <div class="row col-12 m-0 p-0 col-lg-7 text-center justify-content-center">
            <table class="col-10">
              <thead class="fs-4 text-white">
                <tr>
                  <th class="border-green p-1 fw-normal">Posición</th>
                  <th class="border-green p-1 fw-normal">Jugador</th>
                  <th class="border-green p-1 fw-normal">Deck</th>
                  <th class="border-green p-1 fw-normal">Puntos/Victorias</th>
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

      </template>
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
