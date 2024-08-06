<script setup>
import { onMounted } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';

onMounted(() => {
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
          Cabe destacar que, todos los jugadores registrados (actualmente 17) en esta página forman parte de la comunidad local y 
          están unidos por la férrea pasión del Magic.
          <br><br>
          Puedes descubrir más sobre la comunidad en el canal de Youtube <a href="https://www.youtube.com/@ComandMancos" target="_blank">ComandMancos</a> y en [Inserte más redes sociales]
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
        <div class="col-12 col-lg-6">
          Coliseo es un formato netamente local nacido en el año XXXX, basado en la regla 0, mucho texto acerca del formato
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
          <li class="my-1"><a href="" target="_blank">Baneos de coliseo en todas sus formas</a> </li>
          <li class="my-1"><a href="" target="_blank">Duel (1vs1) como comandante</a></li>
          <li class="my-1"><a href="" target="_blank">Duel (1vs1) entre las 99</a></li>
          <li class="my-1"><a href="" target="_blank">Multi (vs4) como comandante</a></li>
          <li class="my-1"><a href="" target="_blank">Multi (vs4) como entre las 99</a></li>
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
