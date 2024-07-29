<script setup>

const emits = defineEmits(['firstEmit'])

const FirstEmit = (() => {
    emits('firstEmit')
})

const props = defineProps({
    componentToShow: Object,
    modalName: String,
    title: String
})
</script>

<template>
    <div class="modal fade bd-example-modal-xl" tabindex="-1" role="dialog" :id="props.modalName" :aria-labelledby="props.modalName" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
            <div class="modal-content">
                <div class="modal-header border-none">
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <h3 class="text-center">
                        {{ props.title }}
                    </h3>
                    <component :is="props.componentToShow" @formOk="FirstEmit" />
                </div>
            </div>
        </div>
    </div>

</template>

<style scoped>
.icon-container{
    width:60px;
    height:60px;
}
</style>