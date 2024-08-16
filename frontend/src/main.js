import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import store from './store/store';
import router  from './router/router';
import axios from 'axios'
import VueAxios from 'vue-axios'
// Vuetify
import 'vuetify/styles'

import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import colors from 'vuetify/lib/util/colors'
import '@mdi/font/css/materialdesignicons.css';
const vuetify = createVuetify({
  components,
  directives,
  theme: {
    themes: {
      light: {
        dark: false,
        colors: {
         primary:"#009688",
         Secondary:"#FFFFFF",
         ternaire:"#df6662"
       } },
    },
  },
})

createApp(App).use(VueAxios, axios).use(vuetify).use(router).use(store).mount('#app')