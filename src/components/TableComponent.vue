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
          <tr>
            <td>{{ titulo_libro }}</td>
            <td>{{ autor_libro }}</td>
            <td>{{ categoria_libro }}</td>
            <td>{{ estado_libro }}</td>

            <td class="d-flex justify-start">
              <v-btn variant="text" icon color="blue" density="compact"
                ><v-icon>mdi-pencil</v-icon></v-btn
              >
              <v-btn variant="text" icon color="red" density="compact"
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
  prop: {
    titulo_libro: String,
    autor_libro: String,
    categoria_libro: String,
    estado: String,
    acciones: String,
  },
};
</script>

<style>
</style>