<template>
  <v-container>
    <div></div>

    <MenuComponent></MenuComponent>
    <BusquedaComponent
      v-if="profile_user == 'ADMIN'"
      :profile_user="profile_user"
      @response="handleResponse"
      @filterEstado="filtroByEstado"
    ></BusquedaComponent>
    <TableComponent
      :profile_user="profile_user"
      :libros="libros"
      @editResponse="editLibro"
      @prestamoResponse="prestamoLibro"
      @disabledResponse="deshabilitarLibro"
      @devolverLibro="regresarLibro"
    ></TableComponent>
    <AppFooter></AppFooter>
  </v-container>
</template>

<script>
import AppFooter from "@/components/AppFooter.vue";
import BusquedaComponent from "@/components/BusquedaComponent.vue";

import MenuComponent from "@/components/MenuComponent.vue";
import TableComponent from "@/components/TableComponent.vue";
import { onMounted, ref, reactive, toRaw } from "vue";
import axios from "axios";

export default {
  name: "HomeView",
  components: {
    AppFooter,
    MenuComponent,
    BusquedaComponent,
    TableComponent,
  },

  setup() {
    let childMsg = ref("");
    const profile_user = localStorage.getItem("profile_user");
    let libros = reactive([]);
    const dialogLibro = ref(true);
    const BASE_URL = "http://127.0.0.1:8000";
    const id_user = ref("");

    const regresarLibro = async (id) => {
      const response = await axios.put(`${BASE_URL}/api/libro/devolver/${id}`);
      console.log("id del libro", id);
      if (response.status != 200) {
        console.log("ERROR NO SE PUDO REGREAR EL LIBRO");
        return;
      }

      console.log(response.data);
    };
    const filtroByEstado = async (estado) => {
      const response = await axios.get(`${BASE_URL}/api/libro/${estado}`);
      console.log("estado recibido", estado);
      if (response.status != 200) {
        console.log("Error");
        return;
      }
      // console.log(response.data.libros)

      libros.splice(0, libros.length, ...response.data.libros);

      console.log("array de libros actual", libros);
    };

    const deshabilitarLibro = async (id) => {
      try {
        console.log("Id recibido: ", id);
        const response = await axios.put(
          `${BASE_URL}/api/libro/disabled/${id}`
        );
        if (response.status != 200) {
          console.log("No se pudo deshabilitar nada");
        }
        console.log(response.status);
      } catch (error) {
        throw new Error("ocurrio un error: ", error);
      }
    };
    const handleResponse = async (libroData) => {
      try {
        const response = await axios.post(
          `${BASE_URL}/api/register-libro`,
          toRaw(libroData),
          { headers: { "Content-Type": "application/json" } }
        );
        console.log("CODIGO DE ESTAOD: ", response.data);
        if (response.status == 200) libros.unshift(response.data.libro);
        console.log("Libro guardado con exito", response.data);
      } catch (error) {
        console.error("Error al crear el libro:", error);
      }
    };

    const editLibro = async (libroData) => {
      try {
        const response = await axios.put(
          `${BASE_URL}/api/edit-libro`,
          toRaw(libroData),
          { headers: { "Content-Type": "application/json" } }
        );
        console.log(response.data.libros);
        if (response.status === 200 && response.data.libros) {
          const updatedLibro = response.data.libros;

          const index = libros.findIndex(
            (libro) => libro.id === updatedLibro.id
          );

          if (index !== -1) {
            libros[index] = updatedLibro;
          }

          console.log(" Libro editado con éxito", updatedLibro);
        } else {
          console.warn(" El libro no fue actualizado: ", response.data);
        }
      } catch (error) {
        console.error(" Error al editar el libro:", error);
      }
    };

    const prestamoLibro = async (libroData) => {
      try {
        const response = await axios.post(
          `${BASE_URL}/api/prestar-libro`,
          toRaw(libroData)
        );
        if (response.status != 200) {
          console.log("NO SE PUDO PRESTAR NADA");
          return;
        }

        const updatedLibro = response.data.libro;
        const index = libros.findIndex(
          (libro) => libro.id === updatedLibro.id_libro
        );
        if (index == -1) {
          return;
        }
        libros[index].estado = "Prestado";

        console.log("LIBRO PRESTADO ", response.data);
      } catch (error) {
        console.error("Error al prestar el libro:", error);
      }
    };
    const getLibros = async () => {
      try {
        const response = await axios.get(`${BASE_URL}/api/listar-libros`);
        if (response.status != 200) {
          console.log("No se pudo extraer ningun libro");
          return;
        }
        console.log(response.data);
        Object.assign(libros, response.data);
      } catch (error) {
        console.error("Error al crear el libro:", error);
      }
    };

    const getLibroById = async (id) => {
      try {
        const response = await axios.get(
          `${BASE_URL}/api/listar-libros-by-id-users/${id}`
        );

        if (response.status != 200) {
          console.log("No se pudo extraer ningun libro");
          return;
        }
        console.log(response.data);
        console.log("antes", libros);
        Object.assign(libros, response.data.libros);
        console.log("despues", libros);
      } catch (error) {
        console.error("Error al extraer el libro:", error);
      }
    };

    onMounted(() => {
      console.log(profile_user);
      id_user.value = localStorage.getItem("id_user");
      if (profile_user == "ADMIN") {
        getLibros();
      } else {
        getLibroById(id_user.value);
      }
    });
    return {
      libros,
      profile_user,
      dialogLibro,
      childMsg,
      handleResponse,
      getLibros,
      editLibro,
      getLibroById,
      id_user,
      prestamoLibro,
      filtroByEstado,
      deshabilitarLibro,
      regresarLibro,
    };
  },
};
</script>

<style>
</style>