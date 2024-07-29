<script setup>
import { ref, onMounted } from 'vue'

import FrequentQuestions from '@/components/FrequentQuestions.vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';

const services = [
  'Préstamos de libros para uso interno',
  'Áreas de estudio, investigación, lectura, etc.',
  'Área audiovisual para talleres y conferencias',
  'Internet para fines investigativos',
  'Juegos de mesa como Scrabble y Ajedrez',
]


onMounted(() => {
  OnAppearAnimation('hide-up')
})
</script>

<template>
  <main class="row m-0 p-0 justify-content-center bg-black">
    <section class="row col-12 m-0 p-0">
      <figure class="m-0 p-0 my-hero d-flex align-items-center justify-content-center animated-2 shadowed-h" id="my-hero">
        <img class="w-100 text-center my-hero" src="@/assets/images/progenitus.jpg" alt="">
        <h1 class="h1 fw-bold text-center outline-black position-absolute text-orange">
          The Orc's Ranking
          <br>
          <span class="h2 text-orange outline-none m-0">
            Season 1
          </span>
        </h1>
      </figure>
    </section>

    <section class="row col-12 m-0 p-0 justify-content-around align-items-center flex-column-reverse flex-lg-row bg-dark-grey text-orange">
      <div class="col-12 m-0 p-0 d-flex justify-content-center fs-5">
        <div class="col-12 col-md-3 text-center py-4 side-border-orange">
          <h3 class="w-100 text-center text-orange">
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

        <div class="col-12 col-md-3 text-center py-4 side-border-orange ">
          <h3 class="w-100 text-center text-orange">
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

        <div class="col-12 col-md-3 text-center py-4 side-border-orange">
          <h3 class="w-100 text-center text-orange">
            Colores
          </h3>
          <article class="row m-0 p-0 my-1">
            <span class="col-4 text-end">Azul</span>
            <span class="col-8 text-start">
              <div class="percent" style="width:75.06%;">
                75%
              </div>
            </span>
          </article>
          <article class="row m-0 p-0 my-1">
            <span class="col-4 text-end">Rojo</span>
            <span class="col-8 text-start">
              <div class="percent" style="width:55%;">
                55%
              </div>
            </span>
          </article>
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
        </div>
      </div>
    </section>


    <section class="row col-12 m-0 p-0 mt-5 justify-content-center align-items-center flex-column flex-lg-row lb-bg-terciary shadowed-n services-section bg-dark-grey">
      <div class="row col-12 col-lg-7 m-0 p-0 d-flex justify-content-center text-white py-4">
        <div class="row m-0 p-0 col-6 justify-content-center">
          <p class="h3 col-12 text-orange text-center">
            Torneos totales
          </p>
          <figure class="col-5 text-center">
            <img class="col-6" src="@/assets/icons/sitemap.png" alt="bitemap">
          </figure>
          <p class="col-12 h1 text-orange text-center">4</p>
        </div>
        <div class="row m-0 p-0 col-6 justify-content-center">
          <p class="h3 col-12 text-orange text-center">
            Participantes
          </p>
          <figure class="col-5 text-center">
            <img class="col-6" src="@/assets/icons/user.png" alt="bitemap">
          </figure>
          <p class="col-12 h1 text-orange text-center">12</p>
        </div>
      </div>
    </section>

    <section class="row col-12 m-0 p-0 justify-content-around align-items-center flex-column flex-lg-row my-5">
      <div class="col-12 text-center">
        <h2 class="h1 fw-bold text-black">¿De qué te sirve leer?</h2>  
      </div>
      <div class="col-12 col-lg-3 text-center">
        <figure class="col-12">
          <img class="w-100 hide-up shadowed-l rounded animated-1" alt="escritores">
        </figure>
      </div>
      <div class="col-12 col-lg-5 text-center">
        <p class="fs-5">
          Leer regularmente no solo amplía
          tus conocimientos y mejora las habilidades de comunicación, sino que también estimula la mente, fomenta la 
          <strong>creatividad</strong>
          y reduce el estrés. A través de la lectura, puedes viajar a mundos imaginarios, aprender de diferentes culturas y perspectivas, 
          y desarrollar una comprensión más profunda de nosotros mismos y del mundo que nos rodea.
          <br><br>
          La lectura enriquece el vocabulario, mejora la concentración y la memoria, y puede incluso retrasar el deterioro cognitivo a medida que envejeces.
        </p>
      </div>
      <div class="col-12 col-lg-3 text-center">
        <figure class="col-12 ">
          <img class="w-100 hide-up shadowed-l rounded animated-1" alt="mangakas">
        </figure>
      </div>
    </section>

    <section class="row col-12 m-0 p-0 mt-5 justify-content-center align-items-center flex-column flex-lg-row lb-bg-terciary shadowed-n pb-4">
      <div class="col-12 text-center">
        <h2 class="h1 fw-bold text-white services-title text-shadow">Preguntas frecuentes</h2>  
      </div>
      <FrequentQuestions/>
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
