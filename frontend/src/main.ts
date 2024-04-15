import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import { OhVueIcon, addIcons } from 'oh-vue-icons'
import {
  FaGithub,
  BiArrowDownCircle,
  BiArrowUpCircle,
  FaMoon,
  FaSun,
  HiSolidMail,
  BiTelephoneFill,
  BiFileEarmarkPdfFill
} from 'oh-vue-icons/icons'

addIcons(
  FaGithub,
  BiArrowDownCircle,
  BiArrowUpCircle,
  FaMoon,
  FaSun,
  HiSolidMail,
  BiTelephoneFill,
  BiFileEarmarkPdfFill
)

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.component('v-icon', OhVueIcon)
app.mount('#app')
