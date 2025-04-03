<template>
  <v-container>
    <div></div>
    <MenuComponent :profile="profile_user" ></MenuComponent>
    <BusquedaComponent></BusquedaComponent>
    <TableComponent :libros="libros"></TableComponent>
    <AppFooter></AppFooter>
  </v-container>
</template>

<script>
import AppFooter from "@/components/AppFooter.vue";
import BusquedaComponent from "@/components/BusquedaComponent.vue";

import MenuComponent from "@/components/MenuComponent.vue";
import TableComponent from "@/components/TableComponent.vue";
import {onMounted} from 'vue';

export default {
  name: "HomeView",
  components: {
    AppFooter,
    MenuComponent,
    BusquedaComponent,
    TableComponent,
  },

  setup() {
    const profile_user = localStorage.getItem("profile_user")
    const libros = [
      {
        id: 1,
        titulo: "El Principito",
        autor: "Antoine de Saint-Exupéry",
        categoria: "Ficción",
        estado: "Disponible",
      },
      {
        id: 2,
        titulo: "Cien años de soledad",
        autor: "Gabriel García Márquez",
        categoria: "Realismo mágico",
        estado: "Prestado",
      },
      {
        id: 3,
        titulo: "1984",
        autor: "George Orwell",
        categoria: "Distopía",
        estado: "Disponible",
      },
      {
        id: 4,
        titulo: "Don Quijote de la Mancha",
        autor: "Miguel de Cervantes",
        categoria: "Clásico",
        estado: "Disponible",
      },
      {
        id: 5,
        titulo: "Los miserables",
        autor: "Victor Hugo",
        categoria: "Drama",
        estado: "Prestado",
      },
    ];
    onMounted(() => {
      console.log(profile_user)
    });
    return { libros,profile_user };
  },
};
</script>

<style>
</style>