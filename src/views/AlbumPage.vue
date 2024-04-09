<template>
    <div class="playlist-page">
      <!-- Header -->
      <header class="header">
        <div class="left-header">
          <img class="logo" src="@/assets/harmonix.png" alt="Logo">
        </div>
        <div class="playlist-heading"><b>My Albums</b></div>
        <div class="right-header">
          <button id="home-button" @click="redirectToHome">Home</button>
        </div>
      </header>
  
      <!-- Main Content -->
      <div class="main-content">
        <!-- Left Section -->
        <div class="left-section">
          <div class="user-section">
            <img class="user-photo" src="@/assets/creator2.jpg" alt="User Photo">
            <div class="user-details">
              <p class="user-name">User {{ user_id }}</p>
            </div>
          </div>
        </div>
  
        <!-- Right Section -->
        <div class="right-section">
          <div class="playlist-section">
            <div class="playlist-container">
              <button
                v-for="album in unique_albums"
                :key="album"
                class="playlist-box"
                @click="displaySongs(album)"
              >
                {{ album }}
              </button>
            </div>
          </div>
  
          <div class="separator-line"></div>
  
          <div class="table-container">
            <div class="table-heading">Create New Album</div>
            <table>
              <thead>
                <tr>
                  <th>S.No</th>
                  <th>Song Name</th>
                  <th>Creator Name</th>
                  <th>Add to Album</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(song, index) in songs" :key="song.song_id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ song.song_name }}</td>
                  <td>{{ song.creator_name }}</td>
                  <td>
                    <form @submit.prevent="addToAlbum(song.song_name, song.creator_name)">
                      <input type="text" v-model="newAlbumName" placeholder="Enter Album Name" required>
                      <button class="add-button" type="submit">Add</button>
                    </form>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
  
      <!-- Footer -->
      <footer>
        <p>&copy; Harmonix. All rights reserved.</p>
        <p>Contact: contact@harmonix.com</p>
      </footer>
  
      <!-- Modal -->
      <div class="modal" v-if="isModalVisible">
        <div class="modal-content">
          <span class="close" @click="closeModal">&times;</span>
          <div id="modalSongsContainer">
            <p v-for="song in modalSongs" :key="song.song_id">{{ song.song_name }} by {{ song.creator_name }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        user_id: '123', // Example user ID
        unique_albums: ['Album 1', 'Album 2', 'Album 3'], // Example unique albums
        songs: [], // Populate with actual data or fetch from API
        newAlbumName: '',
        isModalVisible: false,
        modalSongs: []
      };
    },
    methods: {
      closeModal() {
        this.isModalVisible = false;
      },
      addToAlbum(songName, creatorName) {
        // Placeholder for adding song to album logic
        alert(`Add "${songName}" by ${creatorName} to the album: ${this.newAlbumName}`);
        // Implement API call or logic to add song to the selected album
      },
      redirectToHome() {
        // Example redirection to home
        this.$router.push('/creator');
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add your scoped styles here */
  .playlist-page {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  .header {
    background-color: #333;
    color: #fff;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100px;
    font-size: 28px;
  }
  
  .logo {
    max-width: 200px;
    height: 100%;
    margin-left: 10px;
  }
  
  .main-content {
    display: flex;
    flex: 1;
    justify-content: space-between;
  }
  
  .left-section {
    flex: 1;
    width: 20%; /* Adjusted width for left section */
    background-color: #dadada;
    margin-right: 10px;
  }
  
  .user-section {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .user-photo {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin: 20px;
  }
  
  .user-details {
    text-align: center;
  }
  
  .user-name {
    font-size: 18px;
    font-weight: bold;
    margin: 0;
  }
  
  .right-section {
    flex: 7; /* Adjusted width for right section */
  }
  
  .playlist-section {
    text-align: left;
  }
  
  .playlist-container {
    display: flex;
    flex-wrap: wrap;
    margin-top: 10px;
  }
  
  .playlist-box {
    flex: 0 0 calc(33.33% - 10px);
    height: 150px;
    background-color: #f2f2f2;
    border: 2px solid #E35F21;
    border-radius: 4px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 10px;
    margin-bottom: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    color: #333;
    font-size: 20px;
  }
  
  .playlist-box:hover {
    background-color: #ccc;
  }
  
  .separator-line {
    margin-top: 20px;
    border-top: 2px solid #ccc;
  }
  
  .table-container {
    margin-top: 20px;
  }
  
  .table-heading {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th,
  td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
  }
  
  th {
    background-color: #333;
    color: #fff;
  }
  
  .right-header {
    text-align: right;
  }
  
  button {
    padding: 8px 16px;
    margin-right: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  button#home-button {
    background-color: #E35F21;
    color: #fff;
    width: 150px;
  }
  
  button#home-button:hover {
    background-color: #FF7F50;
  }
  
  button.add-button {
    background-color: #ccc;
    color: #fff;
    width: 150px;
  }
  
  button.add-button:hover {
    background-color: #999;
  }
  
  .form-container {
    display: flex;
    align-items: center;
    margin-top: 20px;
  }
  
  input {
    padding: 8px;
    margin-right: 10px;
    width: 200px;
    box-sizing: border-box;
  }
  
  button.add-button[type="submit"] {
    background-color: #E35F21;
    color: #fff;
    width: 80px;
  }
  
  button.add-button[type="submit"]:hover {
    background-color: #FF7F50;
  }
  
  footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px;
  }
  </style>
  