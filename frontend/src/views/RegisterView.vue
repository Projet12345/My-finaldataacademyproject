<!-- RegisterForm.vue -->
<template>
    <v-card width="400" class="mx-auto mt-10">
      <v-card-title class="text-center">
        <h2>Register</h2>
      </v-card-title>
      <v-card-text>
        <v-form ref="registerForm" v-model="valid" @submit.prevent="register">
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
            Register
          </v-btn>
        </v-form>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn color="primary" to="/login">
          Already have an account? Login
        </v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
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
  
  const register = () => {
  if (valid.value) {
    loading.value = true;
    axios
      .post('/api/register', { email: email.value, password: password.value })
      .then(() => {
        // Add your redirection or success message logic here
      })
      .catch((error) => {
        console.error(error);
        // Add your error handling logic here
      })
      .finally(() => {
        loading.value = false;
      });
  }
};
 
  </script>