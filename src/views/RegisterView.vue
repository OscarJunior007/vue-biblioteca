<template>
  <v-container>
    <v-card class="pa-5">
      <v-card-title class="text-center"> Registrarse </v-card-title>

      <v-card-text>
        <v-form ref="form">
          <v-text-field
            v-model="formData.name"
            type="text"
            label="Nombre"
            variante="outlined"
            density="comfortable"
            prepend-inner-icon="mdi-account"
            :rules="[(v) => !!v || 'Este campo no puede ir vacio']"
          >
          </v-text-field>

          <v-text-field
            v-model="formData.email"
            type="email"
            label="email"
            variante="outlined"
            density="comfortable"
            prepend-inner-icon="mdi-email"
            :rules="[(v) => !!v || 'Este campo no puede ir vacio']"
          >
          </v-text-field>

          <v-text-field
            v-model="formData.password"
            type="password"
            label="password"
            variante="outlined"
            density="comfortable"
            prepend-inner-icon="mdi-lock"
            :rules="[(v) => !!v || 'Este campo no puede ir vacio']"
          >
          </v-text-field>

          <v-text-field
            type="password"
            label="confirm password"
            variante="outlined"
            density="comfortable"
            prepend-inner-icon="mdi-lock"
            :rules="[
              (v) => v === formData.password || 'Las contraseñas no coinciden',
            ]"
          >
          </v-text-field>

          <v-btn @click="crear_user()"> Registrarse </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { ref, reactive, toRaw } from "vue";
import axios from "axios";

export default {
  name: "RegisterView",

  setup() {
    const formData = reactive({
      name: "",
      email: "",
      password: "",
    });
    const BASE_URL = "http://127.0.0.1:8000";
    

    const crear_user = async () => {
      try {
            const response = await axios.post(
            `${BASE_URL}/api/register-user`,
            toRaw(formData), // Convierte el objeto reactivo a uno plano
            { headers: { "Content-Type": "application/json" } }
            );
        console.log("Usuario creado:", response.data);

      } catch (error) {
        console.error("Error al crear usuario:", error);
      }
    };
    return { formData, BASE_URL, crear_user,limpiar_data };
  },
};
</script>

<style>
</style>