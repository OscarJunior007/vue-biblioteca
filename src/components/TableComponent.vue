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
            
            <td v-if="libro.estado ==  'disponible' ">
             <v-chip color="green" variant="tonal">
              {{ libro.estado }}
             </v-chip> 
            </td>

            <td v-else-if="libro.estado ==  'prestado' ">
             <v-chip color="blue" variant="tonal">
              {{ libro.estado }}
             </v-chip> 
            </td>

            <td class="d-flex justify-start">
              <v-btn @click="editarLibro(libro)" variant="text" icon color="blue" density="compact"
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

    <v-container>
  <v-dialog v-model="dialogEdit" >
    <v-card class="pa-5 mx-auto" max-width="600">
      <v-card-title class="text-h5">Registro de Libro</v-card-title>

      <v-form @submit.prevent="submitFormEdit">
        <v-row>
          <v-col cols="12">
            <v-text-field
              prepend-inner-icon="mdi-book"
              v-model="form_edit_libro.titulo"
              label="Título del Libro"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-text-field
              prepend-inner-icon="mdi-book-account"
              v-model="form_edit_libro.author"
              label="Autor"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-select
              v-model="form_edit_libro.categoria"
              :items="['Novela', 'Historia', 'Ficcion']"

              label="Categoría"
              required
            ></v-select>
          </v-col>

          <v-col cols="12">
            <v-text-field
              v-model="form_edit_libro.fecha_publicacion"
              label="Fecha de Publicación"
              type="date"
              required
            ></v-text-field>
          </v-col>

          <v-col  cols="12" class="text-center">
            <v-btn type="submit" color="primary">Registrar Libro</v-btn>
            <h1>{{ form_edit_libro.id }}</h1>
          </v-col>
        </v-row>
      </v-form>
    </v-card>
  </v-dialog>
</v-container>
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

  emits: ['editResponse'], // Declara los eventos que emites

  setup(props,{emit}){
    const dialogEdit = ref(false)
    const form_edit_libro = reactive({
      id:"",
      titulo: "",
      author: "",
      categoria: "",
      estado: "disponible",
      fecha_publicacion: "",
    })

    const submitFormEdit = () => {
      emit('editResponse', form_edit_libro)
    }
    const editarLibro = (libro) =>{
      Object.assign(form_edit_libro, libro);
      dialogEdit.value = true
    }

    return{form_edit_libro,dialogEdit,editarLibro,submitFormEdit}
  }
};
</script>

<style>
</style>