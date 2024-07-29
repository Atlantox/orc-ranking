<script setup>
import { ref, onMounted } from 'vue'
import OnAppearAnimation from '@/utils/ElegantDisplayer';
import LoadingGadget from '../myGadgets/LoadingGadget.vue';

import useLoanStore from '@/stores/loans';

const loanStore = useLoanStore()

const props = defineProps({
    'initialDate': String,
    'finalDate': String,
})

const loansByGender = ref({})
const loansByTeacher = ref({})
const loansByCategories = ref({})
const totalLoans = ref({})
const mounted = ref(false)


onMounted(async () => {
    loansByGender.value = await loanStore.GetLoansCountByGenderBetweenDates(props.initialDate, props.finalDate)
    loansByTeacher.value = await loanStore.GetLoansCountByTeacherBetweenDates(props.initialDate, props.finalDate)
    loansByCategories.value = await loanStore.GetLoansCountByCategoriesrBetweenDates(props.initialDate, props.finalDate)
    totalLoans.value = await loanStore.GetDeliveredAndReturnedLoansCountBetweenDates(props.initialDate, props.finalDate)
    mounted.value = true
    await new Promise(r => setTimeout(r, 50));
    OnAppearAnimation('hide-up')

    Highcharts.chart('loansByGender', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Préstamos por género'
        },
        plotOptions: {
            series: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: [{
                    enabled: true,
                    distance: 20
                }, {
                    enabled: true,
                    distance: -40,
                    format: '{point.y}',
                    style: {
                        fontSize: '1.2em',
                        textOutline: 'none',
                        opacity: 0.7
                    },
                    
                }]
            }
        },
        series: [
            {
                name: 'Cantidad',
                colorByPoint: true,
                data: loansByGender.value
            }
        ]
    });

    Highcharts.chart('loansByTeacher', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Préstamos por docencia'
        },
        plotOptions: {
            series: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: [{
                    enabled: true,
                    distance: 20
                }, {
                    enabled: true,
                    distance: -40,
                    format: '{point.y}',
                    style: {
                        fontSize: '1.2em',
                        textOutline: 'none',
                        opacity: 0.7
                    },
                    
                }]
            }
        },
        series: [
            {
                name: 'Cantidad',
                colorByPoint: true,
                data: loansByTeacher.value
            }
        ]
    });

    Highcharts.chart('loansByCategories', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Préstamos por categorías'
        },
        plotOptions: {
            series: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: [{
                    enabled: true,
                    distance: 20
                }, {
                    enabled: true,
                    distance: -40,
                    format: '{point.y}',
                    style: {
                        fontSize: '1.2em',
                        textOutline: 'none',
                        opacity: 0.7
                    },
                    
                }]
            }
        },
        series: [
            {
                name: 'Cantidad',
                colorByPoint: true,
                data: loansByCategories.value
            }
        ]
    });
})

</script>

<template>
    <LoadingGadget v-if="mounted === false" />
    <div v-else class="hide-up animated-1 row w-100 m-0 p-0 justify-content-center align-items-start p-1 p-lg-4">
        <div class="row m-0 p-0 col-12 col-lg-8 justify-content-around p-3">
            <div class="row col-12 p-2 text-center shadowed-l rounded lb-bg-terciary-ul">
                <div class="col-12 col-lg-6 p-2">
                    <figure id="loansByGender">
                    </figure>
                </div>
                <div class="col-12 col-lg-6 p-2">
                    <figure id="loansByTeacher">
                    </figure>
                </div>
                <div class="col-12 col-lg-6 p-2">
                    <figure id="loansByCategories">
                    </figure>
                </div>           
            </div>
        </div>
        <div class="row m-0 p-0 col-12 col-lg-4 justify-content-around p-3">
            <div class="row col-12 p-2 text-center shadowed-l rounded lb-bg-terciary-ul">
                <h2 class="col-12 m-0">Préstamos realizados: <strong>{{ totalLoans['delivered'] }}</strong></h2>
                <h2 class="col-12 m-0">Préstamos devueltos: <strong>{{ totalLoans['returned'] }}</strong></h2>
            </div>
        </div>
    </div>
</template>