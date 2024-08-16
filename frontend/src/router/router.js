import { createRouter, createWebHistory } from 'vue-router';


import Home from '../views/HomeView.vue';
import DetailsPage from '../views/DetailsMovies.vue';
import Login from '../views/LoginView.vue';
import Register from '../views/RegisterView.vue';


// Créez votre instance de routeur
const router = createRouter({
  history: createWebHistory(),
  routes: [
  
   { path: '/', component: Home },
   { path: '/login', component: Login },
   { path: '/register', component: Register },
   { path: '/details/:id', component: DetailsPage, props:true },
   
  ],
});
export default router;
