import { createStore } from 'vuex'
import moviesstore from './modules/moviesstore'

import createPersistedState from "vuex-persistedstate";
// data to persist
const dataState = createPersistedState({
  //paths: ['filmstore .films']
})
const store = createStore({
  modules: {
    moviesstore
},

plugins:[dataState]
})
export default store;