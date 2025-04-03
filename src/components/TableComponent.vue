<template>
  <v-container>
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
            <td>{{ libro.autor }}</td>
            <td>{{ libro.categoria }}</td>
            <td>{{ libro.estado }}</td>

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
  },
};
</script>

<style>
</style>