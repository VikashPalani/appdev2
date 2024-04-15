<template>
  <div class="playlist-page">
    <header class="header">
      <div class="left-header">
        <img class="logo" src="@/assets/harmonix.png" alt="Logo">
      </div>
      <div class="playlist-heading"><b>My Playlists</b></div>
      <div class="right-header">
        <button id="home-button" @click="redirectToHome">Home</button>
      </div>
    </header>


    <div class="main-content">
      <div class="left-section">
        <div class="user-section">
          <img class="user-photo" src="@/assets/creator1.jpg" alt="User Photo">
          <div class="user-details">
            <p class="user-name">{{ user_id }}</p>
          </div>
        </div>
      </div>

      <div class="right-section">
        <div class="playlist-section">
          <div class="playlist-container">
            <button
              v-for="playlist in unique_playlists"
              :key="playlist"
              class="playlist-box"
              @click="displayPlaylist(playlist)"
            >
              {{ playlist }}
            </button>
          </div>
        </div>

        <div class="table-container">
          <div v-if="displayedSongs.length > 0" class="table-container">
            <div class="table-heading">Songs in Playlist: {{ selectedPlaylist }}</div>
            <table>
              <thead>
                <tr>
                  <th>S.No</th>
                  <th>Song Name</th>
                  <th>Creator Name</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(song, index) in displayedSongs" :key="song.song_id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ song.song_name }}</td>
                  <td>{{ song.creator_name }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div v-else>
            <p>No songs available for the selected playlist.</p>
          </div>
        </div>

        <div class="table-container">
          <div v-if="displayedSongs.length > 0" class="table-container">
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
              <tr v-for="(song, index) in displayedSongs" :key="song.song_id">
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
    </div>

    <br>

    <footer>
      <p>&copy; Harmonix. All rights reserved.</p>
      <p>Contact: contact@harmonix.com</p>
    </footer>

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
      user_id: localStorage.getItem('userName'),
      unique_playlists: [],
      newPlaylistName: '',
      displayedSongs: [], 
      isModalVisible: false,
      selectedPlaylist: '',
      modalSongs: [],
      songs: []
    };
  },

  computed: {
    filteredSongs() {
      return this.songs.filter(song =>
        song.song_name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },

  methods: {
    async fetchPlaylists() {
      try {
        const response = await fetch('/api/playlists');
        const data = await response.json();
        this.unique_playlists = data;
      } catch (error) {
        console.error('Failed to fetch playlists', error);
      }
    },
    
    async displayPlaylist(playlistName) {
    try {
      const response = await fetch(`/api/playlists/${playlistName}/songs`);
      if (!response.ok) {
        throw new Error('Failed to fetch songs for the playlist');
      }
      const songs = await response.json();
      this.displayedSongs = songs;
      this.selectedPlaylist = playlistName;
    } catch (error) {
      console.error('Error fetching songs for playlist:', error);
    }
  },
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
        } else {
          this.error = data.message || 'Login failed. Please try again.';
        }
      } 
      catch (error) {
        console.error('Error:', error);
        this.error = 'Login failed. Please try again.';
      }
    },

    async fetchSongs() {
      try {
        const response = await fetch('/api/songs');
        if (!response.ok) {
          throw new Error('Failed to fetch songs');
        }
        this.songs = await response.json();
        this.displayedSongs = this.songs;
      } catch (error) {
        console.error('Error fetching songs:', error);
      }
    },

    async addToPlaylist(songName, creatorName) {
      try {
        const playlistName = this.newPlaylistName.trim();

        if (!playlistName) {
          alert('Please enter a playlist name');
          return;
        }

        const response = await fetch('/api/add_to_playlist', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            playlist_name: playlistName,
            songs: [
              {
                song_name: songName,
                creator_name: creatorName
              }
            ]
          })
        });

        if (!response.ok) {
          throw new Error('Failed to add song to playlist');
        }

        alert(`"${songName}" by ${creatorName} added to playlist: ${playlistName}`);
        this.newPlaylistName = '';
      } catch (error) {
        console.error('Error adding song to playlist:', error);
        alert('Failed to add song to playlist. Please try again.');
      }
    },

    redirectToHome() {
      this.$router.push('/user');
    },

    closeModal() {
      this.isModalVisible = false;
    }
  },

  mounted() {
    this.fetchSongs();
    this.fetchPlaylists();
  }
};
</script>


<style scoped>

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
  width: 20%;
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
  flex: 7;
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