<template>
  <v-app-bar
        color="primary"
        density="compact"
      >
        <template v-slot:prepend>
          <v-btn to="/"><v-icon>mdi-home</v-icon></v-btn>
        </template>

        <v-app-bar-title>Analysis of movie reviews</v-app-bar-title>

        
          <h4 v-if="authToken!=null" class="mr-2"> {{ user.email }}</h4>
          <v-btn v-if="authToken==null" to="/login" >Login/Register</v-btn>

      </v-app-bar>
</template>

<script setup>
import { ref, reactive,computed, onMounted, onUnmounted } from "vue";
import { useStore } from 'vuex'

// Accéder au store
const store = useStore()
const authToken =  computed(() => store.state.moviesstore.authToken)
const user = computed(() => store.state.moviesstore.user)
</script>

<style>

</style>