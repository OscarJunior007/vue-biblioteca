<template>
  <v-container>
    <v-card class="pa-5">
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
            density="comfortable"
            variant="outlined"
            label="Buscar por titulo autor o categoria"
            prepend-inner-icon="mdi-magnify"
            hide-details
          ></v-text-field>
        </v-col>

        <v-col cols="12" md="3">
          <v-select
            density="comfortable"
            variant="outlined"
            label="Categoria"
            :items="['Novela', 'Historia', 'Ficcion']"
            hide-details
          ></v-select>
        </v-col>

        <v-col cols="12" md="3">
          <v-select
            density="comfortable"
            v-model ="filtroEstado"
            @update:model-value="filterEstados"
            variant="outlined"
            label="Estados"
            :items="['Disponible', 'Prestado', 'Deshabilitado']"
            hide-details
          ></v-select>
        </v-col>

        <v-col v-if="profile_user == 'ADMIN'" class="d-flex justify-end " >
          <v-btn color="yellow" @click="refrezh()" variant="elevated"> eliminar filtros </v-btn>
          <v-btn color="green" @click="dialogLibro = true" variant="elevated" class="ml-2"> agregar libro </v-btn>
        </v-col>

        
        <v-col v-else class="d-flex justify-end " >
          <v-btn style="display: none;" color="green" @click="dialogLibro = true" variant="elevated"> agregar libro </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-container>

  <v-container>
  <v-dialog v-model="dialogLibro">
    <v-card class="pa-5 mx-auto" max-width="600">
      <v-card-title class="text-h5">Registro de Libro</v-card-title>

      <v-form @submit.prevent="submitForm">
        <v-row>
          <v-col cols="12">
            <v-text-field
              prepend-inner-icon="mdi-book"
              v-model="form_create_libro.titulo"
              label="Título del Libro"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-text-field
              prepend-inner-icon="mdi-book-account"
              v-model="form_create_libro.author"
              label="Autor"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-select
              v-model="form_create_libro.categoria"
              :items="['Novela', 'Historia', 'Ficcion']"

              label="Categoría"
              required
            ></v-select>
          </v-col>

          <v-col cols="12">
            <v-text-field
              v-model="form_create_libro.fecha_publicacion"
              label="Fecha de Publicación"
              type="date"
              required
            ></v-text-field>
          </v-col>

          <v-col  cols="12" class="text-center">
            <v-btn type="submit" color="primary">Registrar Libro</v-btn>
          </v-col>    
        </v-row>
      </v-form>
    </v-card>
  </v-dialog>
</v-container>
</template>

<script>
import { reactive,ref } from 'vue'
import { useRouter } from 'vue-router';

export default {
  name: "BusquedaComponent",

  props: {
    dialogLibro: Boolean,
    categorias: Array,
    profile_user:Number
  },

  emits: ['response','filterEstado'], 

  setup(props, { emit }) {
    const router = useRouter()
    const dialogLibro =ref(false) 
    const filtroEstado =  ref("")
    const form_create_libro = reactive({
      titulo: "",
      author: "",
      categoria: "",
      estado: "Disponible",
      fecha_publicacion: "",
    })
    const refrezh = () =>{
        window.location.reload();
    }
    const submitForm = () => {
      emit('response', form_create_libro)
    }

    const filterEstados = () =>{
      emit('filterEstado',filtroEstado.value)
    }
    return {
      form_create_libro,
      submitForm,
      dialogLibro,
      filtroEstado,
      filterEstados,
      refrezh
    }
  }
};
</script>
<style>
</style>