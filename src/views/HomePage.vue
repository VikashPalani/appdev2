<template>
  <div class="home-page">
    <div class="header">
      <img src="@/assets/harmonix.png" alt="Harmonix Logo" class="logo">
    </div>
    <div class="content">
      <div class="left-section">
        <h1 class="heading">Harmonix</h1>
        <p class="description">
          Welcome to Harmonix, where music comes alive. Play, pause, and immerse yourself in the world of melodies. Explore lyrics, rate songs, and create playlists. For creators, it's not just about listening, but also about sharing. Upload songs, albums, and lyrics. It's your stage, your music.
        </p>
        <p class="join-message"><i>
          Join Harmonix and let the music flow.</i>
        </p>
        <button class="login-button" @click="goToLogin">Login</button>
      </div>
      <div class="right-section">
        <img src="@/assets/panda.png" alt="Panda Image" class="panda-image">
      </div>
    </div>
    <footer class="footer">
      <p>&copy; Harmonix. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  methods: {
    goToLogin() {
      this.$router.push('/sample');
    }
  }
}
</script>

<style>
.home-page {
  background-color: black;
  color: white;
  font-family: Arial, sans-serif;
  min-height: 100vh; /* Use min-height instead of height */
  padding: 20px; /* Add padding */
  display: flex;
  flex-direction: column;
}

.header {
  display: flex;
  justify-content: center;
  margin-bottom: 100px; /* Decrease margin */
  margin-top: 20px; /* Decrease margin */
}

.logo {
  width: 250px; /* Increase the logo size */
}

.login-button {
  background-color: #E35F21;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px; /* Add margin between paragraph and button */
  width: 100px;
}

.content {
  display: flex;
  justify-content: center; /* Center align content */
  align-items: center;
  margin-left: 50px;
}

.left-section {
  flex: 1;
  padding-right: 20px;
  text-align: justify; /* Justify align text */
}

.heading {
  font-size: 60px;
  margin-bottom: 20px;
}

.description {
  font-size: 22px;
  line-height: 1.5;
}

.join-message {
  font-size: 22px;
  margin-top: 20px;
}

.right-section {
  flex: 1;
  display: flex;
  justify-content: center;
}

.panda-image {
  max-width: 60%;
  height: auto;
}

.footer {
  background-color: #000000; /* Dummy footer background color */
  color: white;
  text-align: center;
  padding: 20px 0; /* Add padding */
  position: fixed; /* Fixed position for footer */
  bottom: 0;
  width: 100%;
}
</style>
