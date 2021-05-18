import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/base'
import './plugins/chartist'
import './plugins/vee-validate'
import './plugins/vue-mavon-editor'
import vuetify from './plugins/vuetify'
import i18n from './i18n'

import 'leaflet/dist/leaflet.css';

Vue.config.productionTip = false
Vue.prototype.$config = {
  fastApiUrl: process.env.VUE_APP_FAST_API_URL,
  node_env: process.env.NODE_ENV,
  markdownOption: {
    bold: true,
    italic: true,
    header: true,
    underline: true,
    strikethrough: true,
    mark: true,
    superscript: true,
    subscript: true,
    quote: true,
    ol: true,
    ul: true,
    link: true,
    imagelink: true,
    code: true,
    table: true,
    help: true,
    alignleft: true,
    aligncenter: true,
    alignright: true,
    subfield: true,
    preview: true,
    undo: true,
    redo: true,
    // false
    fullscreen: false,
    readmodel: false,
    htmlcode: false,
    trash: false,
    save: false,
    navigation: false,
  }
}

new Vue({
  router,
  vuetify,
  i18n,
  render: h => h(App)
}).$mount('#app')
