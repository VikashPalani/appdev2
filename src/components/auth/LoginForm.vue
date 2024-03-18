<template>
    <div class="login-container">
      <nav class="navbar">
        <img src="/assets/Harmonix.png" alt="Website Logo" class="logo">
      </nav>
      <div class="login-form">
        <h2>Login</h2>
        <form @submit.prevent="login">
          <div class="form-group">
            <label for="role">Role</label>
            <select v-model="role" id="role">
              <option value="user">User</option>
              <option value="creator">Creator</option>
              <option value="admin">Admin</option>
            </select>
          </div>
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" v-model="name" id="name" placeholder="Enter your name" required>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" v-model="password" id="password" placeholder="Enter your password" required>
          </div>
          <p>New to website? <router-link to="/signup">Sign up here</router-link></p>
          <button type="submit">Login</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        role: 'user',
        name: '',
        password: ''
      };
    },
    methods: {
      login() {
        // Your login logic here
        console.log('Login credentials:', this.role, this.name, this.password);
      }
    }
  };
  </script>
  
  <style scoped>
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
        color: rgb(240, 255, 255);
    }

    .container {
        display: flex;
        width: 800px;
    }

    .left-box,
    .right-box {
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
        color: #E35F21; /* Match button color */
    }

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
        transition: background-color 0.3s; /* Add smooth transition */
    }

    button:hover {
        background-color: #9c4117; /* Darken button color on hover */
    }

  </style>

  ./loginForm.vue./LoginForm.vue