<script setup>
import { ref, onMounted } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';

import usePlayerStore from '@/stores/players';

const playerStore = usePlayerStore()
const playerCount = ref(0)
onMounted( async() => {
  playerCount.value = await playerStore.GetPlayerCount()
  OnAppearAnimation('hide-up')
})
</script>

<template>
  <main class="row m-0 p-0 justify-content-center bg-black fs-4 text-green">
    <section class="row col-12 m-0 p-0">
      <figure class="m-0 p-0 my-hero d-flex align-items-center justify-content-center animated-2 shadowed-h" id="my-hero">
        <img class="w-100 text-center my-hero" src="@/assets/images/open_book.jpg" alt="">
        <h1 class="h1 fw-bold text-center outline-black position-absolute text-green hide-up">
          Acerca de The Orc's Ranking
        </h1>
      </figure>
    </section>

    <section class="row col-12 m-0 p-0 justify-content-around align-items-center flex-wrap bg-dark-grey py-5">
      <div class="row col-12 m-0 p-0 justify-content-center mt-3">
        <p class="col-12 col-lg-10 text-center fw-lighter">
          The Orc's Ranking es un proyecto desarrollado por <a href="https://atlantox.pythonanywhere.com/" target="_blank">Atlantox</a>
          con el objetivo de poder crear un sitio web en el cual poder llevar un historial de torneos y eventos en la comunidad de Magic the Gathering en Venezuela estado Lara.
          Gracias a este proyecto, es posible crear y ver estadísticas certeras que ayuden a analizar el panorama competitivo local,
          y por supuesto, sana competición entre los jugadores.
          <br><br>
          Cabe destacar que, todos los jugadores registrados (actualmente {{ playerCount }}) en esta página forman parte de la comunidad local y 
          están unidos por la férrea pasión del Magic.
          <br><br>
          Puedes descubrir más sobre la comunidad en el canal de Youtube <a href="https://www.youtube.com/@ComandMancos" target="_blank">ComandMancos</a>
        </p>
      </div>
    </section>


    <section class="row col-12 m-0 p-0 mt-5 justify-content-center align-items-center flex-column flex-lg-row shadowed-n services-section">
     <div class="row col-12 m-0 p-0 justify-content-center">
      <h2 class="col-12 text-center text-green">
        Coliseo
      </h2>
      <div class="row col-12 justify-content-center m-0 p-0 mt-5">
        <figure class="col-12 col-lg-4">
          <img src="@/assets/images/grand_coliseum.jpg" alt="grand coliseum" class="w-100 hide-up animated-1 shadowed-l">
        </figure>
        <div class="col-12 col-lg-7">
          <p class="my-3">
            Coliseo es un formato de Commander Multi que nace en Barquisimeto - Venezuela a mediados del año 2020, surge de la 
            necesidad de integrar nuevos jugadores a la comunidad y de incluirlos de forma armoniosa a los torneos locales que se venían realizando.
          </p>
          <p class="my-3">
            Parte de los objetivos del formato son: 
          </p>
          <ol class="my-3">
            <li>Promover la realización de torneos en los que tanto los jugadores novatos como los experimentados tengan la oportunidad de competir en un ambiente de transparencia y equidad, donde la inversión económica no represente una ventaja abrumadora.</li>
            <li>Promover la viabilidad de la mayoría de arquetipos posibles en el juego con posibilidades reales de ganar.</li>
            <li>Velar por la integración de todos los jugadores de comander en la comunidad fomentando espacios seguros y respetuosos.</li>
          </ol>

          <p class="my-3">
            Coliseo cuenta con su propia lista de baneo estudiada y analizada minuciosamente por un comité electo por los mismos miembros 
            de la comunidad y toma como base la lista de baneo de EDH.
          </p>

          <p class="my-3">
            Otra particularidad del formato es que se rige por un sistema de puntos o "logros" que determinan al 
            ganador en torneos en mesas de 4 jugadores que funciona de la siguiente manera:
            <br>
            Eliminar a un jugador de la mesa +1 punto.
            <br>
            Ganar la mesa +2 puntos.
          </p>
        </div>
      </div>
     </div>
    </section>

    <section class="row col-12 m-0 p-0 py-4 justify-content-center align-items-start my-5 bg-dark-grey text-green">
      <div class="row col-12 justify-content-center m-0 p-05">
      <h2 class="col-12 text-center text-green fs-1">
        Lista de baneos
      </h2>

      <div class="row col-12 justify-content-center m-0 p-0 mt-3">
        <ul class="col-12 list-unstyled text-center">
          <li class="my-1"><a href="https://manabox.app/decks/rg-uh4KUSY6EwM4Pp-vwgw " target="_blank">Baneos de coliseo en todas sus formas</a> </li>
          <li class="my-1"><a href="https://manabox.app/decks/93ZwKsK8SaWY85X27xWeOQ" target="_blank">Baneados como comandante</a></li>
        </ul>
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
