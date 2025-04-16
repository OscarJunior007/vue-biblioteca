<template>
  <v-container>
    <v-app-bar :elevation="2">
      <v-app-bar-title>CBN BIBLIOTECA</v-app-bar-title>
    
      <v-btn @click="logOut" variant="elevated" color="red">
        cerrar sesion
      </v-btn>
    </v-app-bar>
  </v-container>
</template>

<script>
import { useRouter } from 'vue-router';


export default {
  name: "MenuComponent",
  setup(){
    const router = useRouter(); 
    const logOut = () =>{
      localStorage.clear()
      router.push("/")
    }
    return{logOut}
}
};


</script>

<style>
</style>