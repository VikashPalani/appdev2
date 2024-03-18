<template>

  <!--
  <img alt="Vue logo" src="./assets/logo.png">
  -->

  <!--
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  -->
  <div id="app">
    <LoginForm></LoginForm>
  </div>

</template>

<script>
import LoginForm from './components/auth/LoginForm.vue';

export default {
  name: 'App',
  components: {
    LoginForm
  }
}
</script>

<!--
  
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

-->