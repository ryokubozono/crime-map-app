import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

import auth from '@/store/modules/auth'
import core from '@/store/modules/core'
import message from '@/store/modules/message'
import * as Cookies from 'js-cookie'

Vue.use(Vuex)

const options = {
  reducer: state => ({
    auth: state.auth,
    // message: state.message
  }),
  storage: {
    getItem: key => Cookies.get(key),
    setItem: (key, value) => Cookies.set(key, value, { expires: 365 }),
    removeItem: key => Cookies.remove(key)
  }
}

export default new Vuex.Store({
  modules: {
    auth,
    core,
    message
  },
  plugins: [createPersistedState(options)]
})
