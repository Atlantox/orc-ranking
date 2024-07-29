<script setup>
import { onMounted } from 'vue'
import PageTitle from '@/components/PageTitle.vue';

import useSessionStore from '@/stores/session';
import useLoanStore from '@/stores/loans';

import LoadingGadget from '@/components/myGadgets/LoadingGadget.vue';
import OnAppearAnimation from '@/utils/ElegantDisplayer';

const articleStyle = 'col-12 my-4 rounded bg-white shadowed-l'
const articleWrappedStyle = 'row col-12 m-0 p-0 justify-content-start shadowed p-2 px-4'
const h4Style = 'h4 col-12 border-bottom fw-bold'
const linkContainersStyle = 'd-flex col-12 flex-wrap mt-2'
const linkElementStyle = 'col-12 col-lg-4 my-1'
const routerLinkStyle = 'w-100 justify-content-start align-items-center p-1'
const iconStyle = 'text-black col-1 panel-icon fs-5'
const linkTextStyle = 'text-grey col-10 fs-5 w-auto hover-bold hover-spacing'

const sessionStore = useSessionStore()
const loanStore = useLoanStore()

onMounted( async () => {
  await loanStore.FetchLatestLoans()
  await loanStore.FetchLoansRecentCount()
  await new Promise(r => setTimeout(r, 50));
  OnAppearAnimation('hide-up')
})
</script>

<template>
  <PageTitle
  :title="'Panel de administrador'"
  />
    <section class="row m-0 p-0 my-3 align-items-center align-items-lg-start justify-content-around flex-column-reverse flex-lg-row">
      <div class="row col-12 justify-content-center col-lg-8 p-3">
        <div class="col-12 shadowed-l rounded lb-bg-terciary-ul">

          <template v-if="sessionStore.userData.permissons.includes('Préstamos')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Préstamos
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'add_loan'}">
                      <i :class="'fa fa-plus text-success ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Nuevo préstamo
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'loans', params:{filter: 'pending'}}">
                      <i :class="'fa fa-file ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver préstamos pendientes
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'loans', params:{filter: 'returned'}}">
                      <i :class="'fa fa-rotate-right ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver préstamos devueltos
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'loans', params:{filter: 'active'}}">
                      <i :class="'fa fa-check ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver préstamos activos
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'loans', params:{filter: 'inactive'}}">
                      <i :class="'fa fa-close ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver préstamos inactivos
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Libros')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Libros
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'add_book'}">
                      <i :class="'fa fa-plus text-success ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Nuevo libro
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'books'}">
                      <i :class="'fa fa-book ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver libros
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'add_book_excel'}">
                      <i :class="'fa fa-table ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Añadir libros por Excel
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Categorías')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Categorías
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'add_category'}">
                      <i :class="'fa fa-plus text-success ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Nueva categoría
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'categories'}">
                      <i :class="'fa fa-tag ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver categorías
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Autores')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Autores
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'add_author'}">
                      <i :class="'fa fa-plus text-success ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Nuevo autor
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'authors'}">
                      <i :class="'fa fa-pencil ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver autores
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Editoriales')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Editoriales
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'add_editorial'}">
                      <i :class="'fa fa-plus text-success ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Nueva editorial
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'editorials'}">
                      <i :class="'fa fa-building ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver editoriales
                      </span>
                    </router-link>
                  </div>
                </div>
              </div>
            </article>
          </template>

          <template v-if="sessionStore.userData.permissons.includes('Lectores')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                  Ver lectores
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'add_reader'}">
                      <i :class="'fa fa-plus text-success ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Nuevo lector
                      </span>
                    </router-link>
                  </div>
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'readers'}">
                      <i :class="'fa fa-eye ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver lectores
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
                      <i :class="'fa fa-plus text-success ' + iconStyle" ></i>
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

          <template v-if="sessionStore.userData.permissons.includes('Estadísticas')">
            <article :class="articleStyle">
              <div :class="articleWrappedStyle">
                <h4 :class="h4Style">
                    Estadísticas
                </h4>
                <div :class="linkContainersStyle">
                  <div :class="linkElementStyle">
                    <router-link :class="routerLinkStyle" :to="{name: 'statistics'}">
                      <i :class="'fa fa-star ' + iconStyle" ></i>
                      <span :class="linkTextStyle">
                        Ver estadísticas
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
        <div class="row w-100 m-0 p-0 justify-content-around h-100 py-3 shadowed-l rounded lb-bg-terciary-ul my-3">
          <h3 class="fw-bold col-12 text-center">Los últimos 30 días se realizaron...</h3>
          <template v-if="loanStore.counts === undefined">
            <LoadingGadget/>
          </template>
          <template v-else>
            <div class="row col-12 m-0 p-0 justify-content-center hide-up animated-1">
              <article class="col-12 col-lg-6 row m-0 p-0 align-middle p-3 px-lg-2 my-1">
                  <div class="col-12 d-flex align-items-center bg-white rounded shadowed-l">
                      <h4 class="h4 m-0 text-center w-100 p-2">
                        <strong>{{ loanStore.counts['delivered'] }}</strong>
                        Préstamo{{ loanStore.counts['delivered'] > 1 ? 's' : '' }}
                      </h4>
                  </div>
              </article>
    
              <article class="col-12 col-lg-6 row m-0 p-0 align-middle p-3 px-lg-2 my-1">
                  <div class="col-12 d-flex align-items-center bg-white rounded shadowed-l">
                      <h4 class="h4 m-0 text-center w-100 p-2">
                        <strong>{{ loanStore.counts['returned'] }}</strong>
                          {{ loanStore.counts['returned'] > 1 ? 'Devoluciones' : 'Devolución' }}
                      </h4>
                  </div>
              </article>
            </div>
          </template>
        </div>

        <div class="row w-100 m-0 p-0 justify-content-around h-100 py-3 shadowed-l rounded lb-bg-terciary-ul my-3">
          <h3 class="fw-bold col-12 text-center">Préstamos recientes</h3>
          <template v-if="loanStore.loans === undefined">
            <LoadingGadget/>
          </template>
          <template v-else>
            <table class="col-10 text-center hide-up animated-1">
              <thead>
                <tr class="border-bottom">
                  <th>Lector</th>
                  <th>Libro</th>
                  <th>Fecha</th>
                </tr>
              </thead>
              <tbody>
                <tr 
                v-for="loan in loanStore.loans"
                :key="loan.id"
                >
                  <td>
                    <router-link class="text-black" :to="{name:'add_reader', params: {id: loan.reader_id}}">
                      {{ loan.fullname }}
                    </router-link>
                  </td>
                  <td>
                    <router-link class="text-black" :to="{name:'see_book', params: {id: loan.book_id}}">
                      {{ loan.title }}
                    </router-link>
                  </td>
                  <td>
                    <router-link class="text-black" :to="{name:'add_loan', params: {id: loan.loan_id}}">
                      {{ new Date(loan.full_deliver_date).toLocaleDateString('es-VE', { hour: '2-digit', minute: '2-digit', timeZone: 'America/Caracas'}) }}
                    </router-link>
                  </td>
                </tr>
              </tbody>
            </table>
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