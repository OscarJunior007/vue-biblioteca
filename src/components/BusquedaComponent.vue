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
              variant="outlined"
              label="Estados"
              :items="['Disponibles', 'Prestados', 'Deshabilitados']"
              hide-details
            ></v-select>
          </v-col>
        </v-row>
      </v-card>
    </v-container>
  </template>
  

<script>
export default {
    name:'BusquedaComponent'
}
</script>

<style>

</style>