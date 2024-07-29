<script setup>
import { onMounted } from 'vue'

import useUtilsStore from '@/stores/utils';
import OnAppearAnimation from '@/utils/ElegantDisplayer';

const utilsStore = useUtilsStore()

const props = defineProps({
    users: {type: Array, default: []}
})

onMounted(() => {
  utilsStore.InitializeDatatables()
  OnAppearAnimation('hide-up')
})

</script>

<template>
    <div class="w-100 m-0 p-0 hide-up animated-1">
        <table class="w-100 h6 m-0" id="normal-dt">
            <thead>
                <tr class="text-white">
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Nickname</th>
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Tipo</th>
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Fecha de registro</th>
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Activo</th>
                    <th class="text-center lb-bg-terciary border-1 border-white fs-4">Acción</th>
                </tr>
            </thead>
            <tbody>
                <tr 
                v-for="user in props.users"
                :key="user.id"
                class="fs-5 text-center"
                >
                    <td class="border-1"> {{ user.nickname }} </td>
                    <td class="border-1">{{ user.level }}</td>
                    <td class="border-1 text-center">{{ user.created_at }}</td>
                    <td class="border-1">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-12 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <i :class="'text-black fs-5 bi bi-circle-fill text-' + (user.active === 0 ? 'danger' : 'success')"></i>
                                </div>
                            </div>
                        </div>
                    </td>
                    <td class="border-1">
                        <div class="row m-0 p-0 text-center justify-content-center">
                            <div class="row col-12 m-0 p-1 col-3 fs-2">
                                <div class="w-100 hover-bigger text-center m-0 p-0">
                                    <router-link :to="{name:'add_user', params: {id: user.id}}">
                                        <i class="text-black bi bi-eye text-center m-0 p-0"></i>
                                    </router-link>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>