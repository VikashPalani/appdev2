<template>
    <div>
      <div class="title">
        <h1><b>Welcome to Harmonix</b></h1>
      </div>
      <div class="container">
        <div class="signup-box">
          <h2>Sign Up</h2>
          <template v-if="error">
            <p style="color: red;">{{ error }}</p>
          </template>
  
          <form @submit.prevent="handleSignup">
            <input type="text" v-model="name" placeholder="Name">
            <input type="email" v-model="email" placeholder="Email">
            <input type="password" v-model="password" placeholder="Password">
            <select v-model="selectedRole">
              <option value="user">User</option>
              <option value="creator">Creator</option>
            </select>
            <button type="submit">Sign Up</button>
          </form>
          <div class="login-link">
            <p>Already have an account? <router-link to="/login">Login</router-link></p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        name: '',
        email: '',
        password: '',
        selectedRole: 'user',
        error: ''
      };
    },
    methods: {
      handleSignup() {
        // Here you can implement the logic to store user data
        // For now, let's just display the entered data
        console.log('Name:', this.name);
        console.log('Email:', this.email);
        console.log('Password:', this.password);
        console.log('Role:', this.selectedRole);
      }
    }
  };
  </script>
  
  <style>
  /* Styles copied from LoginForm.vue */
  body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background-color: #333;
    background-size: cover;
    background-position: center;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    flex-direction: column;
  }
  
  .title {
    font-size: 24px;
    margin-bottom: 30px;
    color: rgb(255, 255, 255);
  }
  
  .container {
    display: flex;
    width: 500px;
  }
  
  .signup-box {
    flex: 1;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    padding: 40px;
    margin: 0 10px;
  }
  
  h2 {
    text-align: center;
    margin-bottom: 30px;
    color: rgb(0, 0, 0);
  }
  
  select,
  input,
  button {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    margin-bottom: 20px;
    box-sizing: border-box;
  }
  
  button {
    background-color: #E35F21;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #9c4117;
  }
  
  a {
    color: #E35F21;
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .login-link {
    text-align: center;
  }
  </style>
  