import { defineStore } from 'pinia'
import Swal from 'sweetalert2/dist/sweetalert2.all.js'


const useUtilsStore = defineStore('utils', {
  state: () => {
    return {
      
    }
  },
  actions:{
    ShowModal(title, content, type){
      Swal.fire({
        title: title,
        html: content,
        icon: type,
        confirmButtonColor: '#71E580',
        cancelButtonColor: '#71E580'
      })
    },

    async ConfirmModal(content, type){
      let confirmed = false
      await Swal.fire({
        title: 'Confirmar',
        text: content,
        icon: type,
        showCancelButton: true,
        confirmButtonText: 'Sí',
        cancelButtonText: 'No',
      }).then((result) => { confirmed = result.isConfirmed; })

      return confirmed
    },

    InitializeSelect2(){
      const select2Ids = [
        'books',
        'select2',
        'readers',
        'state',
        'categories',
        'editorial',
        'author'
      ]

      select2Ids.forEach((id) => { 
          $('#' + id).select2() 
      })
    },

    InitializeDatatables(){
      var even = true
        $('#normal-dt').DataTable( {
            scrollX: true,
            order: false,
            "language": {
                paginate: {
                  previous: '<i class="bi bi-caret-left-fill text-white datatable-navigation"></i>',
                  next:     '<i class="bi bi-caret-right-fill text-white datatable-navigation"></i>',
                  first: "Primero",
                  last: "Último",
                },
                aria: {
                  paginate: {
                      previous: '<i class="bi bi-caret-right-fill text-white datatable-navigation"></i>',
                      next:     '<i class="bi bi-caret-right-fill text-white datatable-navigation"></i>',
                      first: "Primero",
                      last: "Último",
                  }
                },
                search: '<i class="bi bi-search text-black me-2 datatable-search"></i>',    
                "lengthMenu": "Mostrar _MENU_ registros por página",
                "info": "Mostrando _START_ a _END_ de entre _TOTAL_ registros totales",
                "infoEmpty": "No se encontraron registos",
                "infoFiltered": "(filtrado de _MAX_ registros totales)",
                "emptyTable": "No se encontraron resultados",
                "zeroRecords": "No se encontraron coincidencias"
            },
            createdRow: (row, data, index) => {
                if(even === false)
                    row.classList.add('odd')
                else
                    row.classList.add('even')
                even = !even
            }
        });
    }
  },
  
  persist: true,
})

export default useUtilsStore