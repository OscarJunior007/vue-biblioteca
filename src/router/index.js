import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    { path: '/', component: LoginView },
    { path: '/home', component: HomeView },
    { path: '/register', component: RegisterView },
];


const router = createRouter({
    history: createWebHistory(),
    routes
  });
  

  export default router;