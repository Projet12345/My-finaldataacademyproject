<!-- LoginForm.vue -->
<template>
    <v-card width="400" class="mx-auto mt-10">
      <v-card-title class="text-center">
        <h2>Login</h2>
      </v-card-title>
      <v-card-text>
        <v-form ref="loginForm" v-model="valid" @submit.prevent="login">
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="Email"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            :rules="passwordRules"
            label="Password"
            type="password"
            required
          ></v-text-field>
          <v-btn
            :disabled="!valid"
            color="primary"
            block
            large
            type="submit"
            :loading="loading"
          >
            Login
          </v-btn>
        </v-form>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn color="primary" to="/register">
          Don't have an account? Create one
        </v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { useStore } from 'vuex'

// Accéder au store
  const store = useStore()

  const router = useRouter();
  
  const valid = ref(false);
  const email = ref('');
  const password = ref('');
  const loading = ref(false);
  
  const emailRules = [
    (v) => !!v || 'Email is required',
    (v) => /.+@.+\..+/.test(v) || 'Email must be valid',
  ];
  const passwordRules = [
    (v) => !!v || 'Password is required',
    (v) => v.length >= 6 || 'Password must be at least 6 characters',
  ];

  const login = () => {
  if (valid.value) {
    store.dispatch('moviesstore/login', { email: email.value, password: password.value })
      .then(response => {
        router.push('/')
      })
      .catch(error => {
        console.error(error)
      })
  }}
  </script>