<script setup>
import { ref } from 'vue'

let currentAnswer = null
const questions = ref([
    {
        question: 
            '¿Qué debo hacer para pedir un libro prestado?',
        answer: 
            `Acércate a la biblioteca. Pregunta por el libro que estás buscando. Te pediremos tus datos para registrarte en el sistema,
            luego de ello se te explicarán las <strong>condiciones</strong> del préstamo para que puedas utilizar el libro`,
    },
    {
        question: 
            '¿Existe un tiempo límite para tener un libro?',
        answer: 
            `Dependerá del libro y de la disponibilidad de este, si se tiene más de un ejemplar, el tiempo máximo de préstamo será de <strong>una semana<strong>`,
    },
    {
        question: 
            '¿Puedo llevarme el libro prestado a mi casa?',
        answer: 
            `Si se trata de un libro <strong>recreativo o enciclopedia</strong>, sí, puedes llevártelo a tu hogar.`,
    },
    {
        question: 
            '¿Qué pasa si pierdo un libro?',
        answer: 
            `En caso de un libro extraviado, el lector debe <strong>pagar</strong> el costo total del libro para poder reponerlo nuevamente en la biblioteca`,
    },
    {
        question: 
            '¿Quiénes pueden utilizar los servicios de la biblioteca?',
        answer: 
            `<strong>Solamente</strong> estudiantes regulares, docentes y coordinadores`,
    },
    {
        question: 
            '¿Puedo planificar una conferencia o actividad?',
        answer: 
            `Por supuesto, para ello debes contactar con el/la encargado(a) de la biblioteca y plantearle tu propuesta con <strong>anticipación</strong>`,
    },
])

const ToggleAnswer = ((questionIdx)=>{
    if(currentAnswer !== null){
        const lastAnswer = document.getElementById('answer' + currentAnswer)
        lastAnswer.classList.add('answer-hidden')
    }

    if(questionIdx === currentAnswer){
        const targetAnswer = document.getElementById('answer' + questionIdx)
        targetAnswer.classList.add('answer-hidden')
        currentAnswer = null
    }
    else{
        const targetAnswer = document.getElementById('answer' + questionIdx)
        targetAnswer.classList.remove('answer-hidden')
        currentAnswer = questionIdx

    }
})
</script>

<template>
    <div class="row w-100 m-0 p-0 justify-content-center">
        <div class="col-12 d-flex justify-content-center flex-wrap">
            <article
            class="col-12 col-md-6 col-lg-4 p-3 fs-3 text-white my-3"
            v-for="question, index in questions"
            :key="index">
                <div class="w-100 lb-bg-primary text-center rounded-pill p-2 shadowed-l lb-border-primary-l question-card" :id="'question' + index" @click="ToggleAnswer(index)">
                    {{ question.question }}
                </div>
                <div class="w-100 content text-center fs-5 px-5 answer-card answer-hidden m-0" :id="'answer' + index">
                    <div class="w-100 content text-center lb-bg-primary rounded-bottom shadowed-n p-2" v-html="question.answer">
                    </div>
                </div>
            </article>
        </div>
    </div>
</template>

<style scoped>
.question-card{
    cursor:pointer;
    position:sticky;
    z-index:5;
}

.answer-card{
    transition:0.3s;
    position:sticky;
    z-index:0;
}

.answer-hidden{
    height:0px;
    font-size:0 !important;
}

*{
    color:rgb(63, 63, 63);
}
</style>