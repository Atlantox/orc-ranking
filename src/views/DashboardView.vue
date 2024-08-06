<script setup>
import { onMounted } from 'vue'
import PageTitle from '@/components/PageTitle.vue';

import useSessionStore from '@/stores/session';
import useLoanStore from '@/stores/loans';

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue';
import OnAppearAnimation from '@/utils/ElegantDisplayer';

const articleStyle = 'col-12 my-4 rounded bg-dark-grey shadowed-l'
const articleWrappedStyle = 'row col-12 m-0 p-0 justify-content-start shadowed p-2 px-4'
const h4Style = 'h4 col-12 border-bottom fw-bold text-green'
const linkContainersStyle = 'd-flex col-12 flex-wrap mt-2'
const linkElementStyle = 'col-12 col-lg-4 my-1'
const routerLinkStyle = 'w-100 justify-content-start align-items-center p-1'
const iconStyle = 'text-white col-1 panel-icon fs-5'
const linkTextStyle = 'text-white col-10 fs-5 w-auto hover-bold hover-spacing'

const sessionStore = useSessionStore()
const loanStore = useLoanStore()

onMounted( async () => {
  // fetchings
  await new Promise(r => setTimeout(r, 50));
  OnAppearAnimation('hide-up')
})
</script>

<template>
  <span class="w-100 mt-5"></span>
  <PageTitle
  :title="'Panel de administrador'"
  />
    <section class="row m-0 p-0 my-3 align-items-center align-items-lg-start justify-content-around flex-column-reverse flex-lg-row text-green">
      <div class="row col-12 justify-content-center col-lg-8 p-3">
        <div class="col-12 rounded text-green">

          <template v-if="sessionStore.userData.permissons.includes('Torneos')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Torneos
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="iconStyle + ' fa fa-plus text-green '" ></i>
                      <span :class="linkTextStyle">
                        Nuevo torneo
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home', params:{filter: 'pending'}}">
                      <i :class="'fa fa-sitemap ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver torneos actuales
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home', params:{filter: 'returned'}}">
                      <i :class="'fa fa-close ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver torneos borrados
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home', params:{filter: 'active'}}">
                      <i :class="'fa fa-list ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver todos los torneos
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Jugadores')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Jugadores
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="iconStyle + ' fa fa-plus text-green '" ></i>
                      <span :class="linkTextStyle">
                        Nuevo jugador
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="iconStyle + ' fa fa-users '" ></i>
                      <span :class="linkTextStyle">
                        Ver jugadores
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Mazos')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Decks
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="iconStyle + ' fa fa-plus text-green '" ></i>
                      <span :class="linkTextStyle">
                        Nuevo deck
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="'fa fa-diamond ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver decks
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Formatos')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Formatos
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="iconStyle + ' fa fa-plus text-green '" ></i>
                      <span :class="linkTextStyle">
                        Nuevo formato
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="'fa fa-tag ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver formatos
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Temporadas')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Temporadas
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="iconStyle + ' fa fa-plus text-green '" ></i>
                      <span :class="linkTextStyle">
                        Nueva temporada
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'home'}">
                      <i :class="iconStyle + ' fa fa-map'" ></i>
                      <span :class="linkTextStyle">
                        Ver temporadas
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Editor') || sessionStore.userData.permissons.includes('Admin')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Usuarios
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'add_user'}">
                      <i :class="iconStyle + ' fa fa-plus text-green '" ></i>
                      <span :class="linkTextStyle">
                        Nuevo usuario
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'users'}">
                      <i :class="'fa fa-user ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver usuarios
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Bitácora')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Bitácora
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'binnacle'}">
                      <i :class="'fa fa-list ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver bitácora
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

        </div>
      </div>


      <div class="row col-12 justify-content-center col-lg-4 p-3">
        <div class="row w-100 m-0 p-0 justify-content-around h-100 py-3 shadowed-l rounded bg-grey my-3 ">
          <h3 class="col-12 text-center text-green">Registros actuales</h3>
          <template v-if="false">
            <LoadingGadget/>
          </template>
          <template v-else>
            <div class="row col-12 m-0 p-0 justify-content-center hide-up animated-1">
              <article class="col-12 col-lg-6 row m-0 p-0 align-middle p-3 px-lg-2 my-1">
                  <div class="col-12 d-flex align-items-center bg-dark-grey rounded shadowed-l">
                      <h4 class="h4 m-0 text-center w-100 p-2 text-green">
                        Jugadores: {{ 17 }}
                      </h4>
                  </div>
              </article>
    
              <article class="col-12 col-lg-6 row m-0 p-0 align-middle p-3 px-lg-2 my-1">
                  <div class="col-12 d-flex align-items-center bg-dark-grey rounded shadowed-l">
                      <h4 class="h4 m-0 text-center w-100 p-2 text-green">
                        Decks: {{ 8 }}
                      </h4>
                  </div>
              </article>

              <article class="col-12 col-lg-6 row m-0 p-0 align-middle p-3 px-lg-2 my-1">
                  <div class="col-12 d-flex align-items-center bg-dark-grey rounded shadowed-l">
                      <h4 class="h4 m-0 text-center w-100 p-2 text-green">
                        Torneos: {{ 2 }}
                      </h4>
                  </div>
              </article>

              <article class="col-12 col-lg-6 row m-0 p-0 align-middle p-3 px-lg-2 my-1">
                  <div class="col-12 d-flex align-items-center bg-dark-grey rounded shadowed-l">
                      <h4 class="h4 m-0 text-center w-100 p-2 text-green">
                        Temporadas: {{ 2 }}
                      </h4>
                  </div>
              </article>
            </div>

            <div class="row col-12 m-0 p-0 justify-content-center hide-up animated-1">
              <h2 class="w-100 text-center">
                <router-link :to="{name: 'home'}">
                  Ver torneo más reciente
                </router-link>
              </h2>
            </div>
          </template>
        </div>
      </div>
  </section>
</template>

<style scoped>
  td{
    padding-top:10px;
  }

  thead tr{
    border-color:black !important;
  }
</style>