<template>
  <v-container>
    <v-app-bar :elevation="2">
      <v-app-bar-title>CBN BIBLIOTECA</v-app-bar-title>
      <div v-if="profile == 2">
        <v-btn style="display: none" color="green" variant="elevated">
          agregar libro
        </v-btn>
      </div>
      <div v-else>
        <v-btn color="green" variant="elevated">
          agregar libro
        </v-btn>
      </div>

      <v-btn variant="elevated" color="red">
        cerrar sesion
      </v-btn>
    </v-app-bar>
  </v-container>
</template>

<script>
export default {
  name: "MenuComponent",
  props: {
    profile: Number,
  },
};
</script>

<style>
</style>