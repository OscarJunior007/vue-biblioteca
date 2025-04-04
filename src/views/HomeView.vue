<template>
  <v-container>
    <div></div>
    <MenuComponent ></MenuComponent>
    <BusquedaComponent :profile_user="profile_user" @response="handleResponse"></BusquedaComponent>
    <TableComponent :profile_user="profile_user" :libros="libros"></TableComponent>
    <AppFooter></AppFooter>
  </v-container>

  
</template>

<script>
import AppFooter from "@/components/AppFooter.vue";
import BusquedaComponent from "@/components/BusquedaComponent.vue";

import MenuComponent from "@/components/MenuComponent.vue";
import TableComponent from "@/components/TableComponent.vue";
import { onMounted, ref,reactive,toRaw } from "vue";
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
    let childMsg = ref('')
    const profile_user = localStorage.getItem("profile_user");
    const libros = ref([])
    const dialogLibro = ref(true);
    const BASE_URL = "http://127.0.0.1:8000";
    const handleResponse = async (libroData) => {
      try{
        const response = await axios.post(`${BASE_URL}/api/register-libro`,
        toRaw(libroData),
        { headers: { "Content-Type": "application/json" } })
        console.log("CODIGO DE ESTAOD: ",response.status)
        if(response.status==200) libros.value.unshift(response.data.libro); 
        console.log("Libro guardado con exito", response.data);  
        
      }catch(error){
        console.error("Error al crear el libro:", error);
      }
    }

    const getLibros = async()=>{
      try{
           const response =  await axios.get(`${BASE_URL}/api/listar-libros`)
           if(response.status !=200){
            console.log("No se pudo extraer ningun libro")
            return;
           }
           console.log(response.data)
           libros.value = response.data.libro;  
      }catch (error){
        console.error("Error al crear el libro:", error);
      }
    }
    
    onMounted(() => {
      console.log(profile_user)
      if(profile_user ==1) getLibros()
 
    });
    return { libros, profile_user, dialogLibro,childMsg,handleResponse,getLibros };
  },
};
</script>

<style>
</style>