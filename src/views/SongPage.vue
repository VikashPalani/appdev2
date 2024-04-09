<template>
    <div class="song-page">
      <!-- Header -->
      <header>
        <div class="logo">
          <img src="@/assets/harmonix.png" alt="Website Logo">
        </div>
        <div class="header-buttons">
          <button @click="redirectToAdminDashboard">Admin Dashboard</button>
        </div>
      </header>
  
      <!-- Content -->
      <div class="content">
        <div class="search-bar-container">
          <h2>All Songs</h2>
          <form @submit.prevent="searchSongs">
            <input type="text" v-model="searchQuery" class="search-bar" placeholder="Search...">
            <button type="submit" class="search-button">Search</button>
          </form>
        </div>
  
        <!-- Separator -->
        <div class="separator"></div>
  
        <!-- Table Container -->
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Song Name</th>
                <th>Lyrics</th>
                <th>Flag Song</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="song in displayedSongs" :key="song.song_id">
                <td>{{ song.song_name }}</td>
                <td>
                  <button class="lyrics-button" @click="showLyrics(song.song_id)">Lyrics</button>
                </td>
                <td>
                  <div class="flag-song-container">
                    <select v-model="flagOption">
                      <option value="blacklist">Blacklist</option>
                      <option value="whitelist">Whitelist</option>
                    </select>
                    <button class="flag-song-button" @click="flagSong(song.song_id)">Flag Song</button>
                  </div>
                </td>
                <td>
                  <button class="delete-button" @click="confirmDelete(song.song_id)">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  
      <!-- Footer -->
      <footer>
        <p>&copy; Harmonix. All rights reserved.</p>
        <p>Contact: contact@harmonix.com</p>
      </footer>
  
      <!-- Modal -->
      <div class="modal" v-if="isModalVisible">
        <span class="close" @click="closeModal">&times;</span>
        <div class="modal-content">
          <pre>{{ currentLyrics }}</pre>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '',
        flagOption: 'blacklist',
        isModalVisible: false,
        currentLyrics: '',
        songs: [] // Populate with actual data or fetch from API
      };
    },
    computed: {
      displayedSongs() {
        // Filter songs based on search query
        return this.songs.filter(song =>
          song.song_name.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
    },
    methods: {
      searchSongs() {
        // Implement search logic (e.g., fetch filtered songs from API)
        console.log('Searching songs with query:', this.searchQuery);
        // Example: Make API call to search songs
      },
      flagSong(songId) {
        // Implement flag song logic (e.g., make API call to flag song)
        console.log('Flagging song with ID:', songId, 'as', this.flagOption);
        // Example: Make API call to flag song
      },
      confirmDelete(songId) {
        // Implement delete confirmation logic
        const result = confirm(`Are you sure you want to delete the song with ID ${songId}?`);
        if (result) {
          // Call delete song method
          this.deleteSong(songId);
        }
      },
      deleteSong(songId) {
        // Implement delete song logic (e.g., make API call to delete song)
        console.log('Deleting song with ID:', songId);
        // Example: Make API call to delete song
      },
      showLyrics(songId) {
        // Implement fetch lyrics logic (e.g., make API call to fetch lyrics)
        console.log('Fetching lyrics for song with ID:', songId);
        // Example: Make API call to fetch lyrics and set currentLyrics
        this.currentLyrics = 'Lyrics will be displayed here...';
        this.isModalVisible = true; // Show modal
      },
      closeModal() {
        // Close the lyrics modal
        this.isModalVisible = false;
      },
      redirectToAdminDashboard() {
        // Redirect to admin dashboard
        this.$router.push('/login');
        // Example: Redirect using router or window.location
      }
    }
  };
  </script>
  
  <style scoped>
  /* CSS Styles */
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  .song-page {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  header {
    background-color: #333;
    color: #fff;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100px;
  }
  
  .logo img {
    width: 200px;
  }
  
  .header-buttons {
    display: flex;
  }
  
  button {
    padding: 12px 20px;
    margin-left: 5px;
    margin-right: 5px;
    background-color: #333;
    font-size: 16px;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease-in-out, transform 0.2s ease-in-out;
  }
  
  button:hover {
    background-color: #555;
    transform: scale(1.05);
  }
  
  .content {
    flex: 1; /* Grow to fill remaining space */
    display: flex;
    flex-direction: column;
  }
  
  .search-bar-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 10px;
    margin-left: 10px;
  }
  
  .search-bar {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-right: 10px;
  }
  
  .search-button {
    padding: 8px 16px;
    background-color: #555;
    color: #fff;
    border: none;
    border-radius: 4px;
    margin-right: 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .search-button:hover {
    background-color: #333;
  }
  
  .separator {
    border-bottom: 2px solid #ccc;
    margin: 10px 0;
  }
  
  .table-container {
    width: 100%;
    overflow-x: auto;
    margin-left: 10px;
    margin-right: 10px;
  }
  
  table {
    width: 98%;
    border-collapse: collapse;
  }
  
  th,
  td {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
    font-size: 20px;
  }
  
  th {
    background-color: #333;
    color: #fff;
  }
  
  footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px;
  }
  
  .modal {
    display: none;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
  }
  
  .modal-content {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fefefe;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
    max-width: 800px;
  }
  
  .close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }
  
  .close:hover,
  .close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
  }
  
  .flag-song-container {
    display: flex;
    align-items: center;
  }
  
  .flag-song-container button {
    margin-right: 10px;
  }
  
  .flag-options label {
    margin-right: 5px;
  }
  </style>
  