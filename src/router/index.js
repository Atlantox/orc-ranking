import { createRouter, createWebHistory } from 'vue-router'

import useSessionStore from '@/stores/session.js'

import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/DashboardView.vue'

import LoginFormView from '../views/forms/LoginFormView.vue'
import BookFormView from '../views/forms/BookFormView.vue'
import BooksByExcelView from '../views/forms/BooksByExcelView.vue'
import LoanFormView from '../views/forms/LoanFormView.vue'
import ReaderFormView from '../views/forms/ReaderFormView.vue'
import CategoryFormView from '@/views/forms/CategoryFormView.vue'
import EditorialFormView from '../views/forms/EditorialFormView.vue'
import AuthorFormView from '@/views/forms/AuthorFormView.vue'
import UserFormView from '@/views/forms/UserFormView.vue'
import MyAccountFormView from '@/views/forms/MyAccountFormView.vue'

import SearchBooksView from '../views/tables/SearchBooksView.vue'
import SearchLoanView from '../views/tables/SearchLoanView.vue'
import SearchReadersView from '../views/tables/SearchReadersView.vue'
import SearchCategoryView from '@/views/tables/SearchCategoryView.vue'
import SearchAuthorsView from '@/views/tables/SearchAuthorsView.vue'
import SearchEditorialsView from '@/views/tables/SearchEditorialsView.vue'
import SearchUsersView from '@/views/tables/SearchUsersView.vue'
import SearchBinnacleView from '@/views/tables/SearchBinnacleView.vue'

import WatchBookView from '../views/watchers/WatchBookView.vue'
import WatchStatisticsView from '../views/watchers/WatchStatisticsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/admin_login',
      name: 'admin_login',
      component: LoginFormView,
      meta:{ requireNotAuth: true }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta:{ requireAuth: true }
    },

    // BOOKS
    {
      path: '/add_book/:id?',
      name: 'add_book',
      component: BookFormView,
      meta:{ requireAuth: true, bookPermisson: true }
    },
    {
      path: '/add_book_excel',
      name: 'add_book_excel',
      component: BooksByExcelView,
      meta:{ requireAuth: true, bookPermisson: true }
    },
    {
      path: '/search_books',
      name: 'books',
      component: SearchBooksView
    },
    {
      path: '/books/:id',
      name: 'see_book',
      component: WatchBookView
    },

    // EDITORIALS
    {
      path: '/add_editorial/:id?',
      name: 'add_editorial',
      component: EditorialFormView,
      meta:{ requireAuth: true, editorialPermisson: true }
    },
    {
      path: '/search_editorials',
      name: 'editorials',
      component: SearchEditorialsView,
      meta:{ requireAuth: true, editorialPermisson: true }
    },

    // AUTHORS
    {
      path: '/add_author/:id?',
      name: 'add_author',
      component: AuthorFormView,
      meta:{ requireAuth: true, authorPermisson: true }
    },
    {
      path: '/search_authors',
      name: 'authors',
      component: SearchAuthorsView,
      meta:{ requireAuth: true, authorPermisson: true }
    },

    // CATEGORIES
    {
      path: '/add_category/:id?',
      name: 'add_category',
      component: CategoryFormView,
      meta:{ requireAuth: true, categoryPermisson: true }
    },
    {
      path: '/search_categories',
      name: 'categories',
      component: SearchCategoryView,
      meta:{ requireAuth: true, categoryPermisson: true }
    },
    
    // LOANS
    {
      path: '/add_loan/:id?',
      name: 'add_loan',
      component: LoanFormView,
      meta:{ requireAuth: true, loanPermisson: true }
    },
    {
      path: '/search_loans/:filter?',
      name: 'loans',
      component: SearchLoanView,
      meta:{ requireAuth: true, loanPermisson: true }
    },

    // READERS
    {
      path: '/add_reader/:id?',
      name: 'add_reader',
      component: ReaderFormView,
      meta:{ requireAuth: true, readerPermisson: true }
    },
    {
      path: '/search_readers',
      name: 'readers',
      component: SearchReadersView,
      meta:{ requireAuth: true, readerPermisson: true }
    },

    // USERS
    {
      path: '/add_user/:id?',
      name: 'add_user',
      component: UserFormView,
      meta:{ requireAuth: true, editorPermisson: true }
    },
    {
      path: '/search_users',
      name: 'users',
      component: SearchUsersView,
      meta:{ requireAuth: true, editorPermisson: true }
    },
    {
      path: '/account',
      name: 'account',
      component: MyAccountFormView,
      meta:{ requireAuth: true }
    },

    // STATISTICS
    {
      path: '/see_statistics',
      name: 'statistics',
      component: WatchStatisticsView,
      meta:{ requireAuth: true, statisticsPermisson: true }
    },

    // BINNACLE
    {
      path: '/binnacle',
      name: 'binnacle',
      component: SearchBinnacleView,
      meta:{ requireAuth: true, binnaclePermisson: true }
    },
  ]
})

router.beforeEach(async (to, from, next) => {
  
  const sessionStore = useSessionStore()
  var routeOk = true

  if(sessionStore.authenticated){
    // Si está autenticado, validamos que el usuario esté activo, sino le cerramos la sesión
    var userIsActive = await sessionStore.MyUserIsActive()
    if(userIsActive === false){
      sessionStore.DestroySession()
      routeOk = false
    }

    if(sessionStore.lastLoginDate === null){
      // No tiene fecha de último logeo
      sessionStore.DestroySession()
      routeOk = false
    }
    else{
      var today = new Date()
      var diffHours = Math.abs(sessionStore.lastLoginDate - today) / 36e5;
      if(diffHours >= 24){
        // si el usuario tiene 24 horas o más estando autenticado, le cerramos la sesión
        sessionStore.DestroySession()
        routeOk = false
      }
    }
  }

  if(to.meta.requireAuth){
    if(!sessionStore.authenticated)
      routeOk = false
    else{
      

      if(to.meta.bookPermisson && !(sessionStore.userData.permissons.includes('Libros'))){
        routeOk = false
      }

      if(to.meta.loanPermisson && !(sessionStore.userData.permissons.includes('Préstamos'))){
        routeOk = false
      }

      if(to.meta.readerPermisson && !(sessionStore.userData.permissons.includes('Lectores'))){
        routeOk = false
      }

      if(to.meta.editorialPermisson && !(sessionStore.userData.permissons.includes('Editoriales'))){
        routeOk = false
      }

      if(to.meta.authorPermisson && !(sessionStore.userData.permissons.includes('Autores'))){
        routeOk = false
      }

      if(to.meta.categoryPermisson && !(sessionStore.userData.permissons.includes('Categorías'))){
        routeOk = false
      }

      if(to.meta.editorPermisson && !(sessionStore.userData.permissons.includes('Editor'))){
        routeOk = false
      }

      if(to.meta.statisticsPermisson && !(sessionStore.userData.permissons.includes('Estadísticas'))){
        routeOk = false
      }

      if(to.meta.binnaclePermisson && !(sessionStore.userData.permissons.includes('Bitácora'))){
        routeOk = false
      }
    }
  }
  else{
    if(sessionStore.authenticated){
      if(to.meta.requireNotAuth)
        routeOk = false
    }
  }

  if(routeOk === true)
    next()
  else
    next('/')

})

export default router
