<script setup>
import PageTitle from '@/components/PageTitle.vue'

import BackButtonGadget from '@/components/myGadgets/BackButtonGadget.vue'
import BooksByExcelForm from '@/components/forms/BooksByExcelForm.vue'

</script>

<template>
    <div class="row m-0 p-0 justify-content-center justify-content-lg-start">
        <div class="col-4 col-lg-2 col-xl-1 ps-0 ps-lg-5">
            <BackButtonGadget :back_to="'dashboard'"/>
        </div>
    </div>

    <PageTitle :title="'Agregar libros por excel'"/>

    <BooksByExcelForm />
</template>
