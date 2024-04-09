<template>
  <div class="wrapper">
    <h1 class="title"><b>Welcome to Harmonix</b></h1>
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

          <input type="text" v-model="username" placeholder="Name">
          <input type="password" v-model="password" placeholder="Password">
          <button type="submit">Login</button>
        </form>
        <div class="signup">
          <p>New to Harmonix? <router-link to="/signup">Sign Up</router-link></p>
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

<style scoped>


/* Wrapper Background */
.wrapper {
  background-color: #333; /* Set wrapper background color to #333 */
  height: 100vh; /* Ensure wrapper covers the full viewport height */
  display: flex;
  flex-direction: column; /* Stack children vertically */
  justify-content: center;
  align-items: center;
}

/* Title Styling */
.title {
  font-size: 40px;
  margin-bottom: 30px; /* Margin below the title */
  color: #fff; /* Text color for the title */
}


.login-box {
  background-color: #ffffff8e; 
  border-radius: 10px;
  box-shadow: 0 0 10px #00000033; /* Subtle shadow effect */
  padding: 40px;
  width: 400px; /* Set width of the login box */
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #000; /* Set color for headings */
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
  background-color: #e35f21; /* Orange background color for buttons */
  color: #fff; /* White text color for buttons */
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #9c4117; /* Darker orange color on button hover */
}

a {
  color: #e35f21; /* Orange color for links */
  text-decoration: none;
}

a:hover {
  text-decoration: underline; /* Underline links on hover */
}

.signup {
  font-size: 20px;
  text-align: center;
}
</style>
