<template>
  <div class="song-page">
    <!-- Header -->
    <header>
      <div class="logo">
        <img src="@/assets/harmonix.png" alt="Website Logo">
      </div>
      <div class="header-buttons">
        <button @click="redirectToAdmin">Admin Dashboard</button>
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
                <button class="view-lyrics-button" @click="showLyrics(song)">View Lyrics</button>
              </td>
              <td>
                <div class="flag-song-container">
                  <select v-model="flagOption">
                    <option value="blacklist">Blacklist</option>
                    <option value="whitelist">Whitelist</option>
                  </select>
                  <!-- <button class="flag-song-button" @click="flagSong(song.song_id)">Flag Song</button> -->
                  <button class="flag-song-button">Flag Song</button>
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

    <br><br>

    <!-- Footer -->
    <footer>
      <p>&copy; Harmonix. All rights reserved.</p>
      <p>Contact: contact@harmonix.com</p>
    </footer>

    <!-- Modal for Lyrics -->
    <div class="modal" v-if="isModalVisible">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h3 v-if="selectedSong">{{ selectedSong.song_name }}</h3>
        <pre v-if="selectedSong && selectedSong.lyrics">{{ selectedSong.lyrics }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      isModalVisible: false,
      selectedSong: null,
      songs: [] // This will be populated with songs data from backend
    };
  },
  computed: {
    displayedSongs() {
      return this.songs.filter(song =>
        song.song_name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  methods: {
    async fetchSongs() {
      try {
        const response = await fetch('/api/songs');
        if (!response.ok) {
          throw new Error('Failed to fetch songs');
        }
        this.songs = await response.json();
      } catch (error) {
        console.error('Error fetching songs:', error);
      }
    },
    async showLyrics(song) {
      try {
        const response = await fetch(`/api/songs/${song.song_id}/lyrics`);
        if (!response.ok) {
          throw new Error('Failed to fetch lyrics');
        }
        const lyricsData = await response.json();

        // Set the selected song with lyrics
        this.selectedSong = {
          ...song,
          lyrics: lyricsData.lyrics // Assuming the response contains { lyrics: '...' }
        };

        // Display the modal
        this.isModalVisible = true;
      } catch (error) {
        console.error('Error showing lyrics:', error);
      }
    },
    closeModal() {
      this.isModalVisible = false;
      this.selectedSong = null;
    },
    redirectToAdmin() {
      // Redirect to admin dashboard (replace with your route)
      this.$router.push('/admin');
    },
    searchSongs() {
      // Implement search logic here (e.g., filter songs in displayedSongs)
      console.log('Searching songs with query:', this.searchQuery);
    }
  },
  mounted() {
    // Fetch songs when component is mounted
    this.fetchSongs();
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
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.song-page {
  width: 100%;
}

header {
  background-color: #333;
  color: #fff;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
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
  flex: 1;
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
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 4px;
  margin-right: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: #555;
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

.flag-song-container {
  display: flex;
  align-items: center;
}

.flag-song-container select {
  width: 300px; /* Set the width of the select element */
  padding: 8px; /* Add padding for better appearance */
  margin-left: 200px;
  margin-right: 10px;
  border: 1px solid #ccc; /* Add border for visibility */
  border-radius: 5px; /* Add border radius for rounded corners */
}

.flag-song-container button {
  padding: 8px 16px;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.flag-song-container button:hover {
  background-color: #555;
}


.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: #fefefe;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 600px;
  text-align: center;
  position: relative;
}

.close {
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 24px;
  cursor: pointer;
  color: #aaa;
}

.close:hover {
  color: black;
}

footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px;
}
</style>
