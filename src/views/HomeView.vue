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
  await seasonStore.FetchSeasons()
  await FetchSeasonDependantData(currentSeason.value['id'])

  lastTournament.value = await tournamentStore.GetLastTournament()
  fetchReady.value = await true
  OnAppearAnimation('hide-up')

  const tournamentsNumber = document.getElementById('tournaments-number')
  const participantsNumber = document.getElementById('participants-number')

  const tournamentNumberObserver = new IntersectionObserver(entries => {
      entries.forEach(async entry => {
        // If the element is visible
        if (entry.isIntersecting) {
            // Change the number value
            if(tournamentsNumber.classList.contains('numbers-displayed'))
              return

            var realTournaments = tournamentsCounts.value.tournaments
            tournamentsCounts.value.tournaments = -1
            for(let i = 0; i <= realTournaments; i++){
              console.log(i)
              tournamentsCounts.value.tournaments = i
              await new Promise(r => setTimeout(r, 50 + (i * 50)));
            }
            tournamentsNumber.classList.add('numbers-displayed')
        }
      });
  })

  const participantNumberObserver = new IntersectionObserver(entries => {
      entries.forEach(async entry => {
        // If the element is visible
        if (entry.isIntersecting) {
          if(participantsNumber.classList.contains('numbers-displayed'))
            return

          // Change the number value
          var realParticipants = tournamentsCounts.value.participants
          tournamentsCounts.value.participants = -1
          for(let i = 0; i <= realParticipants; i++){
            tournamentsCounts.value.participants = i
            await new Promise(r => setTimeout(r, 50 + (i * 50)));
          }
          participantsNumber.classList.add('numbers-displayed')
        }
      });
  })

  tournamentNumberObserver.observe(tournamentsNumber);
  participantNumberObserver.observe(participantsNumber);
})

const FetchSeasonDependantData = ( async(seasonId) => {
  if(typeof seasonId !== 'number')
    var mySeasonId = seasonId.target.value
  else
    var mySeasonId = seasonId
    
  tournamentsCounts.value = await tournamentStore.GetTournamentCount(mySeasonId)
  tournamentsRanking.value = await tournamentStore.GetTournamentsRankingOfSeason(mySeasonId)
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
            <div class="col-12 text-center py-4 fs-3 hide-up animated-1">
              <select class="myInput px-4" id="season-select" @change="FetchSeasonDependantData">
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
                  <span class="col-6 text-start">
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
                  <span class="col-6 text-start">
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
                  <span class="col-8 text-start">
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
      <template v-if="tournamentsCounts === undefined">
        <LoadingGadget />
      </template>
      <template v-else>
        <div class="row col-12 col-lg-7 m-0 p-0 d-flex justify-content-center text-white py-4  hide-up animated-1">
          <div class="row m-0 p-0 col-6 justify-content-center">
            <p class="h3 col-12 text-green text-center">
              Torneos totales
            </p>
            <figure class="col-5 text-center">
              <img class="col-6" src="@/assets/icons/sitemap.png" alt="bitemap">
            </figure>
            <p class="col-12 h1 text-green text-center" id="tournaments-number">{{ tournamentsCounts.tournaments }}</p>
          </div>
          <div class="row m-0 p-0 col-6 justify-content-center">
            <p class="h3 col-12 text-green text-center">
              Participantes
            </p>
            <figure class="col-5 text-center">
              <img class="col-6" src="@/assets/icons/user.png" alt="bitemap">
            </figure>
            <p class="col-12 h1 text-green text-center" id="participants-number">{{ tournamentsCounts.participants }}</p>
          </div>
        </div>
      </template>
    </section>

    <section class="row col-12 m-0 p-0 py-4 justify-content-center align-items-start my-5 bg-dark-grey text-green">
      <div class="col-12 text-center my-3">
        <h2 class="h1 text-green">Último torneo </h2>  
        
      </div>

      <template v-if="lastTournament === undefined">
        <LoadingGadget />
      </template>
      <div v-else class="row m-0 p-0 col-12 text-center justify-content-center align-items-start px-4 hide-up animated-1">
        <template v-if="Object.keys(lastTournament).length === 0">
            <h2 class="text-center w-100 text-green">
              No hay torneos registrados esta temporada (aún)
            </h2>
        </template>
        <div v-else  class="row col-12 m-0 p-0 justify-content-center">
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
              <td class="p-1 border-green">Observación</td>
              <td class="p-1 border-green">{{ lastTournament.data.observation === undefined ? 'Ninguna' : lastTournament.data.observation }}</td>
            </tr>
            <tr>
              <td class="p-1 border-green">Presencia de colores</td>
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
