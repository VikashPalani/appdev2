<template>
    <header class="header">
      <div class="search-bar">
        <form @submit.prevent="search">
          <input type="text" v-model="searchQuery" placeholder="Search..." class="search-input">
          <button type="submit" class="search-button">Search</button>
        </form>
      </div>
      <div class="logo">
        <img src="@/assets/harmonix.png" alt="Website Logo" class="logo-img">
      </div>
      <div class="header-buttons">
        <button @click="playlist" class="header-button">My Playlists</button>
        <button @click="signOut" class="header-button">Log Out</button>
      </div>
    </header>
  </template>
  
  <script>

  console.log("Hii")
  export default {
    data() {
      return {
        searchQuery: ''
      };
    },
    methods: {
      search() {
        // Implement search functionality
      },
      playlist() {
        // Implement playlist functionality
      },
      signOut() {
        // Implement sign-out functionality
      }
    }
  };
  </script>
  
  <style>
  /* Header Styles */
  .header {
    margin-top: 700px;
    color: #333;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
  }
  
  .logo img {
    height: 75px;
  }
  
  .header-buttons button {
    margin-left: 10px;
    width: 120px;
  }
  
  /* Search Bar Styles */

  
  .search-bar input {
    padding: 5px;
    margin-right: 5px;
    width: 150px;
  }

  .search-bar button {
    padding: 5px;
    margin-left: 5px;
    margin-right: 5px;
    width: 120px;
  }
  </style>
  