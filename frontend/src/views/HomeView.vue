<template>
<v-container fluid>
          <v-row dense>
            <v-col
              md="3" cols="6" v-for="movie in movieList" :key='movie.id'
            >
            <FilmsComponent :movie="movie" />
            </v-col>
          </v-row>
        </v-container>
</template>

<script setup>
import FilmsComponent from '../components/FilmsComponent.vue';
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex'

// Accéder au store
const store = useStore()
const movieList = computed(() => store.state.moviesstore.movies)

// Action pour récupérer les films
onMounted(() => {
  store.dispatch('moviesstore/fetchTopRatedMovies');
});
</script>

<style>

</style>