/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'
import router from './router';
import axios from 'axios'
import VueAxios from 'vue-axios'
// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

const app = createApp(App)
registerPlugins(app)
app.use(VueAxios,axios);
app.use(router);
app.mount('#app')
