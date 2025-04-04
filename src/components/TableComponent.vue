<template>
  <v-container>
    <div v-if="profile_user == 2 && libros.length == 0">
      <H1 class="text-center">Aun no tienes libros prestados</H1>
    </div>
    <v-card class="pa-5">
      <v-table class="mt-4">
        <thead>
          <tr>
            <th>Titulo</th>
            <th>Autor</th>
            <th>Categoria</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="libro in libros" :key="libro.id">
            <td>{{ libro.titulo }}</td>
            <td>{{ libro.author }}</td>
            <td>{{ libro.categoria }}</td>
            
            <td v-if="libro.estado = 'disponible' ">
             <v-chip color="green" variant="tonal">
              {{ libro.estado }}
             </v-chip> 
            </td>

            <td v-else-if="libro.estado = 'prestado' ">
             <v-chip color="blue" variant="tonal">
              {{ libro.estado }}
             </v-chip> 
            </td>

            <td class="d-flex justify-start">
              <v-btn variant="text" icon color="blue" density="compact"
                ><v-icon>mdi-pencil</v-icon></v-btn
              >
              <v-btn variant="text" icon color="green" density="compact"
                ><v-icon>mdi-exit-to-app</v-icon></v-btn
              >
              <v-btn variant="text" icon color="red" density="compact"
                ><v-icon>mdi-delete</v-icon></v-btn
              >
            </td>
          </tr>
        </tbody>
      </v-table>
    </v-card>
  </v-container>
</template>

<script>
import { ref, reactive, onMounted } from "vue";

export default {
  name: "TableComponent",
  props: {
    libros: Array,
    profile_user: Number,
  },

  setup(){
    const form_edit_libro = reactive({
      titulo: "",
      author: "",
      categoria: "",
      estado: "disponible",
      fecha_publicacion: "",
    })

    return{form_edit_libro}
  }
};
</script>

<style>
</style>