<script setup>
import { useRouter } from 'vue-router'

import useUtilsStore from '@/stores/utils';
import useWarningStore from '@/stores/warnings';

const warningStore = useWarningStore()
const utilsStore = useUtilsStore()
const router = useRouter()

const props = defineProps({
  'targetWarning': {type: Object, default: {}}
})

const DeleteWarning = (async () => {
  const confirmAction = await utilsStore.ConfirmModal('¿Borrar este warning?', 'question')
  if(confirmAction === false)
      return

  warningStore.DeleteWarning(props.targetWarning.id)
  utilsStore.ShowModal('Success', 'Warning borrado exitosamente', 'success')
  router.push({name: 'dashboard'})
})
</script>

<template>
  <div class="row w-100 m-0 p-0 justify-content-center align-items-start p-1 p-lg-4">
    <div class="row m-0 p-0 col-11 col-lg-8 shadowed-l rounded bg-dark-grey justify-content-around my-4"> 
      <article class="row col-12 col-lg-6 m-0 p-2">
        <table class="col-12 table border-green text-white fs-4">
            <tr>
              <td class="odd p-1 border-green text-end orc-font p-2">Jugador</td>
              <td class="odd p-1 border-green p-2">{{ props.targetWarning.player_name }}</td>
            </tr>
            <tr>
              <td class="even p-1 border-green text-end orc-font p-2">Fecha</td>
              <td class="even p-1 border-green p-2">{{ props.targetWarning.date }}</td>
            </tr>
            <tr>
              <td class="odd p-1 border-green text-end orc-font p-2">Temporada</td>
              <td class="odd p-1 border-green p-2">
                {{ props.targetWarning.season_name }}
              </td>
            </tr>
            <tr>
              <td class="even p-1 border-green text-end orc-font p-2">Motivo</td>
              <td class="even p-1 border-green p-2">
                {{ props.targetWarning.reason }}
              </td>
            </tr>
        </table>
      </article>

      <div class="row m-0 p-0 justify-content-center my-2 mt-5">
          <div class="row m-0 p-0 col-12 justify-content-center">
              <button class="col-6 col-lg-3 myBtn green-btn shadowed-l h3 border-danger" @click.prevent="DeleteWarning()" style="color:red!important">
                  Borrar warning
              </button>
          </div>
      </div>    

    </div>  
  </div>
</template>

<style scoped>

</style>