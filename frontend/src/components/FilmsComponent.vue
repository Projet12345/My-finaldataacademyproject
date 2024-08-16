<template>
    <v-card class="mb-4 movie-card">
      <v-img height="250px" cover :src="getImageUrl(movie.poster_path)"></v-img>
  
      <v-card-title class="movie-title">{{ movie.title }}</v-card-title>
      <v-card-subtitle class="movie-release-date">{{ movie.release_date }}</v-card-subtitle>
      <v-card-subtitle class="movie-vote-average">Vote average: {{ movie.vote_average }}</v-card-subtitle>
      <v-card-subtitle class="movie-vote-count">Vote count: {{ movie.vote_count }}</v-card-subtitle>
      <v-card-actions class="movie-actions">
        <v-btn  icon class="action-btn bg-primary" :to="'/details/'+movie.id">
          <v-icon>mdi-arrow-right</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script setup>
  import { defineProps } from 'vue'
  
  const props = defineProps({
    movie: {
      type: Object,
      required: true
    }
  })
  
  const getImageUrl = (path) => {
    return `https://image.tmdb.org/t/p/w185${path}`
  }
  </script>
  
  <style scoped>
  .movie-card {
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
  }
  
  .movie-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
  }
  
  .movie-title {
    font-size: 1.25rem;
    font-weight: bold;
  }
  
  .movie-release-date,
  .movie-vote-average,
  .movie-vote-count {
    color: #666;
    font-size: 0.9rem;
  }
  
  .movie-actions {
    justify-content: flex-end;
  }
  
  .action-btn {
    transition: transform 0.3s;
  }
  
  .action-btn:hover {
    transform: translateX(4px);
  }
  </style>