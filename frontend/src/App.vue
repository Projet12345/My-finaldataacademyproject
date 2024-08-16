<template>
  <v-app fluid>
     <!-- Start header app -->
     <Header/>
     <!-- end header app -->
  
    <!-- Start main app -->
    <v-main color="primary">
      <router-view></router-view>
    </v-main>
   <!-- end main app -->
  
   <!-- Start footer app -->
     <Footer/>
    <!-- end footer app -->
 
  </v-app>
  </template>
  <script setup>
  import {mapState} from 'vuex'
  import Footer from './components/Hearder_Footer/FooterComponent.vue';
  import Header from './components/Hearder_Footer/HeaderComponent.vue';

  </script>
  