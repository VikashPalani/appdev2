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
          <input type="text" v-model="name" placeholder="Name" required>
          <input type="password" v-model="password" placeholder="Password" required>
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
      name: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await fetch('/api/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            name: this.name,
            password: this.password
          })
        });
        
        const data = await response.json();
        
        if (response.ok) {

          console.log('Login successful.');
          console.log('User ID:', data.id);
          console.log('User Name:', data.name);
          console.log('User Role:', data.role);

          localStorage.setItem('userId', data.id);
          localStorage.setItem('userName', data.name);
          localStorage.setItem('userRole', data.role);
          
          if (data.role === 'user') {
            this.$router.push('/user');
          } else if (data.role === 'creator') {
            this.$router.push('/creator');
          } else if (data.role === 'admin') {
            this.$router.push('/admin');
          } else {
            this.error = 'Invalid user role.';
          }
        } else {
          this.error = data.message || 'Login failed. Please try again.';
        }
      } catch (error) {
        console.error('Error:', error);
        this.error = 'Login failed. Please try again.';
      }
    }
  }
};
</script>


<style scoped>



.wrapper {
  background-color: #333;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}


.title {
  font-size: 40px;
  margin-bottom: 30px;
  color: #fff;
}


.login-box {
  background-color: #ffffff8e; 
  border-radius: 10px;
  box-shadow: 0 0 10px #00000033;
  padding: 40px;
  width: 400px;
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #000;
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
  color: #fff;
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

.signup {
  font-size: 20px;
  text-align: center;
}
</style>
