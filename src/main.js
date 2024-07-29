import { createApp } from 'vue'
import { createPinia } from 'pinia'

import "@/assets/common.scss"

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';


import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'

const app = createApp(App)

const sweetalertOptions = {
    confirmButtonColor: '#71E580',
    cancelButtonColor: '#ff7674',
    background: 'black'
}
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)
app.use(VueSweetalert2, sweetalertOptions)


app.mount('#app')

