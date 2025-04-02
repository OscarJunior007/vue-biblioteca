/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import router from './router';

import { registerPlugins } from '@/plugins'
import axios from 'axios'
import VueAxios from 'vue-axios'
// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

const app = createApp(App)
app.use(router);
registerPlugins(app)
app.use(VueAxios,axios);
app.mount('#app')
