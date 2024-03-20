<template>
    <div>
      <header>
        <nav>
          <div class="logo">
            <img src="/src/assets/logo.jpg" alt="Harmonix Logo">
          </div>
          <div class="header-controls">
            <div class="search-bar">
              <input type="text" placeholder="Search">
            </div>
            <div class="login-buttons">
              <button @click="goToLogin" class="button-link">Login</button>
            </div>
          </div>
        </nav>
      </header>
  
      <main>
        <div class="slider">
          <img src="/src/assets/slider1.png" alt="Image 1" class="responsive">
          <img src="/src/assets/slider2.jpg" alt="Image 2" class="responsive">
          <img src="/src/assets/slider3.jpg" alt="Image 3" class="responsive">
          <img src="/src/assets/slider4.jpg" alt="Image 4" class="responsive">
        </div>
  
        <div class="song-list">
          <div class="song">
            <img src="/src/assets/alone.jpg" alt="Song 1">
            <p>Song 1</p>
          </div>
          <div class="song">
            <img src="/src/assets/song2.jpg" alt="Song 2">
            <p>Song 2</p>
          </div>
          <div class="song">
            <img src="/src/assets/song3.jpg" alt="Song 3">
            <p>Song 3</p>
          </div>
          <div class="song">
            <img src="/src/assets/song4.jpg" alt="Song 4">
            <p>Song 4</p>
          </div>
          <div class="song">
            <img src="/src/assets/song5.jpg" alt="Song 5">
            <p>Song 5</p>
          </div>
          <div class="song">
            <img src="/src/assets/song6.jpg" alt="Song 6">
            <p>Song 6</p>
          </div>
          <div class="song">
            <img src="/src/assets/song7.jpg" alt="Song 7">
            <p>Song 7</p>
          </div>
          <div class="song">
            <img src="/src/assets/song8.jpg" alt="Song 8">
            <p>Song 8</p>
          </div>
        </div>
      </main>
  
      <footer>
        <p>&copy; Harmonix. All rights reserved.</p>
        <br>
        <p>Contact: contact@harmonix.com</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goToLogin() {
        this.$router.push('/login');
      }
    }
  }
  </script>
  
  <style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
    font-family: Arial, sans-serif;
  }
  
  header {
    background-color: #333;
    color: #fff;
    padding: 20px;
  }
  
  nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .logo img {
    height: 50px;
  }
  
  .header-controls {
    display: flex;
    align-items: center;
  }
  
  .search-bar input[type="text"] {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-right: 5px;
    transition: border-color 0.3s ease-in-out;
  }
  
  .search-bar input[type="text"]:focus {
    outline: none;
    border-color: #555;
  }
  
  .search-bar .search-btn,
  .login-buttons a {
    padding: 8px 15px;
    background-color: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-left: 10px;
    transition: background-color 0.3s ease-in-out;
    text-decoration: none;
  }
  
  .login-buttons a:hover {
    background-color: #555;
  }
  
  .slider {
    width: 100%;
    height: 500px;
    overflow: hidden;
    position: relative;
    margin-top: 0px;
  }
  
  .slider img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    transition: opacity 0.5s ease-in-out;
  }
  
  .slider img:not(:first-child) {
    opacity: 0;
  }
  
  .song-list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 20px;
    margin-top: 20px;
  }
  
  .song {
    text-align: center;
    transition: transform 0.3s ease-in-out;
    margin: 0 10px;
  }
  
  .song img {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 5px;
    transition: transform 0.3s ease-in-out;
  }
  
  .song img:hover {
    transform: scale(0.9);
  }
  
  .song p {
    margin: 0;
    font-size: 18px;
    color: #333;
  }
  
  footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px;
    margin-top: 10px;
  }
  
  .button-link {
    text-decoration: none;
    padding: 10px 20px;
    border-radius: 5px;
    border: 1px solid #333;
    margin: 10px;
    display: inline-block;
    transition: background-color 0.3s, color 0.3s;
    color: #ffffff;
  }
  
  .button-link:hover {
    background-color: #201f1f;
    color: #fff;
  }
  </style>
  