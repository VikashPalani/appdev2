<template>
  <div>
    <div class="title">
      <h1><b>Welcome to Harmonix</b></h1>
    </div>
    <div class="container">
      <div class="login-box">
        <h2>Login</h2>
        <template v-if="error">
          <p style="color: red;">{{ error }}</p>
        </template>

        <form @submit.prevent="handleLogin">
          <select v-model="selectedRole">
            <option value="user">User</option>
            <option value="creator">Creator</option>
            <option value="admin">Admin</option>
          </select>

          <input type="text" v-model="username" placeholder="Username">
          <input type="password" v-model="password" placeholder="Password">
          <button type="submit">Login</button>
        </form>
        <div class="signup">
          <p>New to Harmonix? <a href="#">Sign up</a></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedRole: 'user',
      username: '',
      password: '',
      error: ''
    };
  },
  methods: {
    handleLogin() {
      if (this.selectedRole === 'user') {
        this.validateUserLogin();
      } else if (this.selectedRole === 'creator') {
        // Handle creator login
        // Example: this.validateCreatorLogin();
      } else if (this.selectedRole === 'admin') {
        // Handle admin login
        // Example: this.validateAdminLogin();
      }
    },
    validateUserLogin() {
      if (this.username === 'user' && this.password === 'password') {
        this.$router.push('/user');
      } else {
        this.error = 'Invalid user credentials. Please try again.';
      }
    },
    // Additional methods for handling creator and admin logins can be added here
  }
};
</script>

<style>
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
  color: rgb(255, 255, 255)
}

.container {
  display: flex;
  width: 500px;
}

.login-box {
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

.signup {
  text-align: center;
}
</style>
