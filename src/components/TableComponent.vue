<template>
  <v-container>
    <div v-if="profile_user == 'DEFAULT' && libros.length == 0">
      <h1 class="text-center">Aun no tienes libros prestados</h1>
    </div>

    <v-card class="pa-5">
      <v-table class="mt-4">
        <thead>
          <tr>
            <th>Título</th>
            <th v-if="profile_user == 'DEFAULT'">Fecha Publicación</th>
            <th v-if="profile_user == 'DEFAULT'">Fecha Préstamo</th>
            <th v-if="profile_user == 'DEFAULT'">Fecha Devolución</th>

            <th v-if="profile_user == 'ADMIN'">Autor</th>
            <th v-if="profile_user == 'ADMIN'">Categoría</th>
            <th v-if="profile_user == 'ADMIN'">Fecha Publicación</th>
            <th v-if="profile_user == 'ADMIN'">Estado</th>
            <th v-if="profile_user == 'ADMIN'">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="libro in libros" :key="libro.id">
            <td>{{ libro.titulo }}</td>

     
            <td v-if="profile_user == 'DEFAULT'">
              {{ libro.fecha_publicacion }}
            </td>
            <td v-if="profile_user == 'DEFAULT'">{{ libro.fecha_prestamo }}</td>
            <td v-if="profile_user == 'DEFAULT'">
              {{
                libro.fecha_devolucion
                  ? libro.fecha_devolucion
                  : "Aún no lo devuelve"
              }}
            </td>

    
            <td v-if="profile_user == 'ADMIN'">{{ libro.author }}</td>
            <td v-if="profile_user == 'ADMIN'">{{ libro.categoria }}</td>
            <td v-if="profile_user == 'ADMIN'">
              {{ libro.fecha_publicacion }}
            </td>

            <td v-if="profile_user == 'ADMIN'">
              <v-chip
                :color="libro.estado === 'Disponible' ? 'green' : 'blue'"
                variant="tonal"
              >
                {{ libro.estado }}
              </v-chip>
            </td>

            <td v-if="profile_user == 'ADMIN'" class="d-flex justify-start">
              <v-btn
                @click="editarLibro(libro)"
                variant="text"
                icon
                color="blue"
                density="compact"
              >
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-btn @click="PrestarLibro(libro)" variant="text" icon color="green" density="compact">
                <v-icon>mdi-exit-to-app</v-icon>
              </v-btn>
              <v-btn variant="text" icon color="red" density="compact">
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </td>
          </tr>
        </tbody>
      </v-table>
    </v-card>

    <!-- Modal de edición -->
    <v-container>
      <v-dialog v-model="dialogEdit">
        <v-card class="pa-5 mx-auto" max-width="600">
          <v-card-title class="text-h5">Editar Libro</v-card-title>
          <v-form @submit.prevent="submitFormEdit">
            <v-row>
              <v-col cols="12">
                <v-text-field
                  prepend-inner-icon="mdi-book"
                  v-model="form_edit_libro.titulo"
                  label="Título del Libro"
                  required
                />
              </v-col>

              <v-col cols="12">
                <v-text-field
                  prepend-inner-icon="mdi-book-account"
                  v-model="form_edit_libro.author"
                  label="Autor"
                  required
                />
              </v-col>

              <v-col cols="12">
                <v-select
                  v-model="form_edit_libro.categoria"
                  :items="['Novela', 'Historia', 'Ficción']"
                  label="Categoría"
                  required
                />
              </v-col>

              <v-col cols="12">
                <v-text-field
                  v-model="form_edit_libro.fecha_publicacion"
                  label="Fecha de Publicación"
                  type="date"
                  required
                />
              </v-col>

              <v-col cols="12" class="text-center">
                <v-btn type="submit" color="primary">Registrar Libro</v-btn>
                <h1>{{ form_edit_libro.id }}</h1>
              </v-col>
            </v-row>
          </v-form>
        </v-card>
      </v-dialog>
    </v-container>

    <v-container>
      <v-dialog v-model="dialogPrestamo">
        <v-card class="pa-5 mx-auto" max-width="600">
          <v-card-title class="text-h5">Registro de Libro</v-card-title>
          <v-form @submit.prevent="submitFormPrestamo">
            <v-row>
              <v-col cols="12">
                <v-text-field
                  prepend-inner-icon="mdi-book"
                  v-model="form_prestamo_libro.doc_user"
                  label="Documento del usuario"
                  required
                />
              </v-col>
              <v-col cols="12" class="text-center">
                <v-btn type="submit" color="primary">prestar Libro</v-btn>
                <h1>{{ form_prestamo_libro.id_libro }}</h1>
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

  emits: ["editResponse","prestamoResponse"], // Declara los eventos que emites

  setup(props, { emit }) {
    const dialogEdit = ref(false);
    const dialogPrestamo = ref(false);

    const form_edit_libro = reactive({
      id: "",
      titulo: "",
      author: "",
      categoria: "",
      estado: "disponible",
      fecha_publicacion: "",
    });

    const form_prestamo_libro = reactive({
      id_libro: "" ,
      doc_user:""
    });

    const submitFormEdit = () => {
      emit("editResponse", form_edit_libro);
    };
    const submitFormPrestamo = () => {
      emit("prestamoResponse", form_prestamo_libro);
    };
    const editarLibro = (libro) => {
      Object.assign(form_edit_libro, libro);
      dialogEdit.value = true;
    };

    const PrestarLibro = (libro) => {
      form_prestamo_libro.id_libro = libro.id;
      dialogPrestamo.value = true;
    };

    return { form_edit_libro, dialogEdit, editarLibro, submitFormEdit,dialogPrestamo,form_prestamo_libro,submitFormPrestamo,PrestarLibro};
  },
};
</script>

<style>
</style>