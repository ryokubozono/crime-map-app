import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/base'
import './plugins/chartist'
import './plugins/vee-validate'
import './plugins/vue-mavon-editor'
import vuetify from './plugins/vuetify'
import i18n from './i18n'
import store from '@/store'
import firebase from 'firebase'
import 'leaflet/dist/leaflet.css';

Vue.config.productionTip = false
Vue.prototype.$config = {
  fastApiUrl: process.env.VUE_APP_FAST_API_URL,
  node_env: process.env.NODE_ENV,
  markdownPreviewOption: {
    navigation: true,
  },
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
  },
  externalLink: {
    // markdown_css: function() {
    //   return '/static/css/markdown/github-markdown.min.css'
    // },
    hljs_js: function() {
      return '/static/js/highlightjs/highlight.min.js'
    },
    // katex_css: function() {
    //   return '/static/css/katex/katex.min.css'
    // },
    katex_js: function() {
      return '/static/js/katex/katex.min.js'
    },
  },
}

var firebaseConfig = {
  apiKey: "AIzaSyDgjOpcwwsVC9tV7MdAX7HtIVPBvPSFIL4",
  authDomain: "blog-betme.firebaseapp.com",
  projectId: "blog-betme",
  storageBucket: "blog-betme.appspot.com",
  messagingSenderId: "1070379729965",
  appId: "1:1070379729965:web:295e39e1321bed09d4a4a4",
  measurementId: "G-4QP6KYRVQ7"
};
firebase.initializeApp(firebaseConfig);

new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App)
}).$mount('#app')
