<template>
  <v-container>
    <v-card class="pa-5">
      <v-card-title class="text-center"> Login </v-card-title>

      <v-card-text>
        <v-form ref="form">
          <v-text-field
            v-model="forDataLogin.email"
            type="email"
            label="email"
            variante="outlined"
            density="comfortable"
            prepend-inner-icon="mdi-email"
            :rules="[(v) => !!v || 'Este campo no puede ir vacio']"
          >
          </v-text-field>

          <v-text-field
            v-model="forDataLogin.password"
            type="password"
            label="password"
            variante="outlined"
            density="comfortable"
            prepend-inner-icon="mdi-lock"
            :rules="[(v) => !!v || 'Este campo no puede ir vacio']"
          >
          </v-text-field>

          <v-btn @click="login_user()"> ingresar </v-btn>
          <router-link to="/register"
            ><v-btn> Crear cuenta </v-btn></router-link
          >
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { ref, reactive, toRaw } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
export default {
  name: "LoginView",

  setup() {
    const router = useRouter();
    const forDataLogin = reactive({
      email: "",
      password: "",
    });
    const BASE_URL = "http://127.0.0.1:8000";

    const login_user = async () => {
      try {
        const response = await axios.post(
          `${BASE_URL}/api/login`,
          toRaw(forDataLogin),
          { headers: { "Content-Type": "application/json" } }
        );
        if (response.status != 200) {
          console.log("no se pudo tener nada");
          return;
        }

        localStorage.setItem("id_user", response.data.id);
        localStorage.setItem("doc_user", response.data.documento_user);
        localStorage.setItem("profile_user", response.data.profile);

        router.push("/home");
      } catch (error) {
        console.error("Error al crear usuario:", error);
      }
    };
    return { forDataLogin, login_user };
  },
};
</script>

<style>
</style>