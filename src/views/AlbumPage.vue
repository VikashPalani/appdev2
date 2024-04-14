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
            <p class="user-name">{{ userName }}</p>
          </div>
        </div>
      </div>

      <!-- Right Section -->
      <div class="right-section">
        <div class="playlist-section">
          <div class="playlist-container">
            <div
            v-for="album in uniqueAlbums"
            :key="album.album_id"
            class="playlist-box"
            @click="displayAlbumsForSelectedAlbum(album.album_name)"
            >
            <div class="album-name">{{ album.album_name }}</div>
            <ul class="song-list" v-if="album.album_name === selectedAlbum">
              <li v-for="song in songsInAlbum" :key="song.song_id">
                {{ song.song_name }} by {{ song.creator_name }}
              </li>
            </ul>
          </div>

          <!-- Display Matching Albums Table -->
          <div v-if="matchingAlbums.length > 0">
            <h3>Matching Albums</h3>
            <table>
              <thead>
                <tr>
                  <th>Album Name</th>
                  <th>Song Name</th>
                  <th>Creator Name</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="album in matchingAlbums" :key="album.album_id">
                  <td>{{ album.album_name }}</td>
                  <td>{{ album.song_name }}</td>
                  <td>{{ album.creator_name }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

        <!-- Songs Section (display songs of selected album) -->
        <div v-if="selectedAlbum" class="songs-section">
          <ul>
            <li v-for="song in songsInAlbum" :key="song.song_id">
              {{ song.song_name }} by {{ song.creator_name }}
            </li>
          </ul>
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
import axios from 'axios';
export default {
  data() {
    return {
      userName: localStorage.getItem('userName') || 'John Doe',
      uniqueAlbums: [], // Example unique albums
      songs: [], // Populate with actual data or fetch from API
      newAlbumName: '',
      isModalVisible: false,
      modalSongs: [],
      albums: [], // Array to store real album data from API
      selectedAlbum: null, // To keep track of the selected album
      songsInAlbum: [], // Array to store songs of the selected album
      matchingAlbums: [] // New property to store matching albums
    };
  },
  methods: {

    displayAlbumsForSelectedAlbum(albumName) {
      this.selectedAlbum = albumName;
      const userName = localStorage.getItem('userName');
      axios.get(`/api/albums/${encodeURIComponent(albumName)}/matching_albums?userName=${userName}`)
        .then(response => {
          this.matchingAlbums = response.data;
        })
        .catch(error => {
          console.error('Error fetching matching albums:', error);
        });
    },
    fetchAlbums() {
      axios.get('/api/albums')
        .then(response => {
          this.albums = response.data;
          this.uniqueAlbums = this.getUniqueAlbums(response.data);
        })
        .catch(error => {
          console.error('Error fetching albums:', error);
        });
    },
    getUniqueAlbums(albums) {
      const uniqueAlbums = [];
      const albumNames = new Set();
      albums.forEach(album => {
        if (!albumNames.has(album.album_name)) {
          albumNames.add(album.album_name);
          uniqueAlbums.push(album);
        }
      });
      return uniqueAlbums;
    },
    displaySongs(album) {
      this.selectedAlbum = album.album_name;
      axios.get(`/api/albums/${album.album_id}/songs`)
        .then(response => {
          this.songsInAlbum = response.data;
        })
        .catch(error => {
          console.error(`Error fetching songs for album ${album.album_name}:`, error);
        });
    },
    fetchSongs() {
      axios.get('/api/songs')
        .then(response => {
          // Filter songs based on the logged-in user's name
          this.songs = response.data.filter(song => song.creator_name === this.userName);
        })
        .catch(error => {
          console.error('Error fetching songs:', error);
        });
    },
    closeModal() {
      this.isModalVisible = false;
    },
    redirectToHome() {
      // Example redirection to home
      this.$router.push('/creator');
    },
    
    addToAlbum(songName, creatorName) {
      if (!this.newAlbumName) {
        alert('Please enter an album name.');
        return;
      }

      const data = {
        song_name: songName,
        creator_name: creatorName,
        album_name: this.newAlbumName
      };

      axios.post('/api/add_to_album', data)
        .then(response => {
          // Check if the request was successful (status code 201)
          if (response.status === 201) {
            alert('Song added to album successfully!');
            // Optionally, you can update the UI or perform additional actions after success
          } else {
            alert('Failed to add song to album. Please try again.');
          }
        })
        .catch(error => {
          console.error('Error adding song to album:', error);
          alert('Failed to add song to album. Please try again.');
        });
      },
  },
  mounted() {
    // Fetch songs when the component is mounted
    this.fetchSongs();
    this.fetchAlbums(); // Fetch albums when the component is mounted
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

button{
  font-size: 16px;
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

.playlist-box {
  position: relative;
  width: 200px;
  height: 200px;
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
  font-size: 16px;
  overflow: hidden;
}

.album-name {
  position: absolute;
  text-align: center;
  font-size: 28px;
  font-weight: bold;
  color: #333;
}

.song-list {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 0;
  list-style: none;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  max-height: 80%;
  overflow-y: auto;
  display: none;
}

.playlist-box:hover .song-list {
  display: block;
}

.song-list li {
  padding: 8px;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px;
}
</style>