<template>
  <div class="playlist-page">
    <!-- Header -->
    <header class="header">
      <div class="left-header">
        <img class="logo" src="@/assets/harmonix.png" alt="Logo">
      </div>
      <div class="playlist-heading"><b>My Playlists</b></div>
      <div class="right-header">
        <button id="home-button" @click="redirectToHome">Home</button>
      </div>
    </header>

    <br>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Left Section -->
      <div class="left-section">
        <div class="user-section">
          <img class="user-photo" src="@/assets/creator1.jpg" alt="User Photo">
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
              v-for="playlist in unique_playlists"
              :key="playlist"
              class="playlist-box"
              @click="displayedSongs(playlist)"
            >
              {{ playlist }}
            </button>
          </div>
        </div>

        <div class="table-container">
          <div class="table-heading">Create New Playlist</div>
          <table>
            <thead>
              <tr>
                <th>S.No</th>
                <th>Song Name</th>
                <th>Creator Name</th>
                <th>Add to Playlist</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(song, index) in songs" :key="song.song_id">
                <td>{{ index + 1 }}</td>
                <td>{{ song.song_name }}</td>
                <td>{{ song.creator_name }}</td>
                <td>
                  <form @submit.prevent="addToPlaylist(song.song_name, song.creator_name)">
                    <input type="text" v-model="newPlaylistName" placeholder="Enter Playlist Name" required>
                    <button class="add-button" type="submit">Add</button>
                  </form>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <br>

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
    // async showLyrics(song) {
    //   try {
    //     const response = await fetch(`/api/songs/${song.song_id}/lyrics`);
    //     if (!response.ok) {
    //       throw new Error('Failed to fetch lyrics');
    //     }
    //     const lyricsData = await response.json();

    //     // Set the selected song with lyrics
    //     this.selectedSong = {
    //       ...song,
    //       lyrics: lyricsData.lyrics // Assuming the response contains { lyrics: '...' }
    //     };

    //     // Display the modal
    //     this.isModalVisible = true;
    //   } catch (error) {
    //     console.error('Error showing lyrics:', error);
    //   }
    // },
    // closeModal() {
    //   this.isModalVisible = false;
    //   this.selectedSong = null;
    // },
    redirectToHome() {
      // Redirect to admin dashboard (replace with your route)
      this.$router.push('/user');
    },
    searchSongs() {
      // Implement search logic here (e.g., filter songs in displayedSongs)
      console.log('Searching songs with query:', this.searchQuery);
    }
  },
  mounted() {
    // Fetch songs when component is mounted
    this.fetchSongs();
  },


  closeModal() {
    this.isModalVisible = false;
  },
  addToPlaylist(songName, creatorName) {
    // Placeholder for adding song to playlist logic
    alert(`Add "${songName}" by ${creatorName} to the playlist: ${this.newPlaylistName}`);
    // Implement API call or logic to add song to the selected playlist
  },
  redirectToHome() {
    // Example redirection to home
    this.$router.push('/user');
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
  background-color: #333;
  color: #fff;
  width: 150px;
}

button#home-button:hover {
  background-color: #555;
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
  background-color: #333;
  color: #fff;
  width: 80px;
}

button.add-button[type="submit"]:hover {
  background-color: #555;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px;
}
</style>