<script setup>

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

import PageTitle from '@/components/PageTitle.vue'
import Statistics from '@/components/detailers/Statistics.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'

import OnAppearAnimation from '@/utils/ElegantDisplayer'

const formRowStyle = 'row m-0 col-6 p-0 justify-content-center my-2'
const labelContainerStyle = 'row m-0 p-0 col-12 col-md-5'
const labelStyle = 'text-center text-md-end'
const inputContainerStyle = 'row m-0 p-0 col-12 col-md-7 justify-content-center justify-content-md-start'

const initialDate = ref('')
const finalDate = ref('')
const displayStatistics = ref(false)

onMounted( async () => {
    OnAppearAnimation('hide-up')
})

const CheckStatistics = (async () => {
    displayStatistics.value = false
    if(initialDate.value !== '' && finalDate.value !== '')
        displayStatistics.value = await true
})

</script>

<template>
    <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
        <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
            <BackButtonGadget :back_to="'dashboard'"/>
        </div>
    </div>

    <PageTitle
        :title="'Estadísticas'"
    />

    <div class="hide-up animated-1 row w-100 m-0 p-0 justify-content-center align-items-start p-3">
        <div class="row m-0 p-0 col-11 col-lg-8 shadowed-l rounded lb-bg-terciary-ul justify-content-around my-4 fs-4 p-3">
            <div :class="formRowStyle">
                <div :class="labelContainerStyle">
                    <label :class="labelStyle" for="initial_date"><strong>Fecha inicial</strong></label>
                </div>
                <div :class="inputContainerStyle">
                    <div class="row col-12">
                        <div class="row col-12 m-0 p-0">
                            <input class="col-12 myInput" type="date" id="initial_date" name="initial_date" v-model="initialDate" @change="CheckStatistics">
                        </div>
                    </div>
                </div>
            </div>

            <div :class="formRowStyle">
                <div :class="labelContainerStyle">
                    <label :class="labelStyle" for="final_date"><strong>Fecha final</strong></label>
                </div>
                <div :class="inputContainerStyle">
                    <div class="row col-12">
                        <div class="row col-12 m-0 p-0">
                            <input class="col-12 myInput" type="date" id="final_date" name="final_date" v-model="finalDate" @change="CheckStatistics">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <template v-if="displayStatistics === true">    
        <Statistics
        :initialDate = initialDate
        :finalDate = finalDate
        />
    </template>
</template>

<style scoped>

</style>
