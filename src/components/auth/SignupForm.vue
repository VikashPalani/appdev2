<template>
  <div class="wrapper">
    <h1 class="title"><b>Welcome to Harmonix</b></h1>
    <div class="container">
      <div class="signup-box">
        <h2>Sign Up</h2>
        <template v-if="error">
          <p style="color: red;">{{ error }}</p>
        </template>

        <form @submit.prevent="handleSignup">
          <input type="text" v-model="role" placeholder="Role" required>
          <input type="text" v-model="name" placeholder="Name" required>
          <input type="email" v-model="email" placeholder="Email" required>
          <input type="password" v-model="password" placeholder="Password" required>
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
      role: '',
      name: '',
      email: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async handleSignup() {
      try {
        const response = await fetch('/api/signup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            role: this.role,
            name: this.name,
            email: this.email,
            password: this.password
          })
        });
        const data = await response.json();
        if (response.ok) {
          this.$router.push('/login'); // Redirect to /user upon successful signup
        } else {
          this.error = data.message;
        }
      } catch (error) {
        console.error('Error:', error);
        this.error = 'Failed to sign up. Please try again.';
      }
    }
  }
};
</script>

<style scoped>
.wrapper {
  background-color: #333; /* Set wrapper background color to #333 */
  height: 100vh; /* Ensure wrapper covers the full viewport height */
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column; /* Stack child elements vertically */
}

.title {
  font-size: 40px;
  margin-bottom: 30px;
  color: #fff; /* Text color for the title */
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center child elements horizontally */
  width: 500px;
}

.signup-box {
  background-color: #ffffff8e;
  border-radius: 10px;
  box-shadow: 0 0 10px #00000033;
  padding: 40px;
  width: 100%; /* Ensure signup box fills container width */
  max-width: 400px; /* Limit maximum width of the signup box */
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #000; /* Text color for headings */
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
  background-color: #e35f21;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #9c4117;
}

a {
  color: #e35f21;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

.login-link {
  font-size: 20px;
  text-align: center;
}
</style>
