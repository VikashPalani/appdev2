<template>
  <div class="creator-page">
    <!-- Header -->
    <header>
      <div class="logo">
        <img src="@/assets/harmonix.png" alt="Website Logo">
      </div>
      <div class="header-buttons">
        <button @click="redirectToAlbumPage">My Albums</button>
        <button @click="redirectToLogout">Logout</button>
      </div>
    </header>

    <!-- User Info Container -->
    <div class="user-info-container">
      <div class="user-info">
        <img class="user-image" src="@/assets/creator2.jpg" alt="Creator Photo">
        <p>{{ userName }}</p> <!-- Updated to use userName -->
      </div>
      <div class="stats-container">
        <div class="stats-box">
          <p>Total Songs</p>
          <p>{{ total_songs }}</p>
        </div>
        <div class="stats-box">
          <p>Average Rating</p>
          <p>{{ avg_rating }}</p>
        </div>
        <div class="stats-box">
          <p>Genre</p>
          <p>{{ genre }}</p>
        </div>
      </div>
    </div>
    
    <!-- Section - Your Uploads -->
    <section>
      <div class="uploads-header">
        <h2>Your Uploads</h2>
        <button class="add-song-button" @click="openAddSongModal">Add New Song</button>
      </div>

      <table>
        <thead>
          <tr>
            <th>Song Name</th>
            <th>View Lyrics</th>
            <th>Edit Lyrics</th>
            <th>Delete Song</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="song in songs" :key="song.song_id">
            <td>{{ song.song_name }}</td>
            <td><button class="view-button" @click="viewLyrics(song.song_id)">View</button></td>
            <td><button class="edit-button" @click="openEditLyricsModal(song.song_id, song.lyrics)">Edit</button></td>
            <td><button class="delete-button" @click="confirmDelete(song.song_id, song.song_name)">Delete</button></td>
          </tr>
        </tbody>
      </table>
      
    </section>

    <!-- Footer -->
    <footer>
      <p>&copy; Harmonix. All rights reserved.</p>
      <p>Contact: contact@harmonix.com</p>
    </footer>

    <!-- Lyrics Popup -->
    <div class="lyrics-popup" v-show="isLyricsPopupOpen">
      <span class="close-popup" @click="closeLyricsPopup">&times;</span>
      <h3>Lyrics</h3>
      <pre>{{ currentLyrics }}</pre>
    </div>

    <!-- Add Song Modal -->
    <div class="add-song-modal" v-show="isAddSongModalOpen">
      <h2>Add New Song</h2>
      <form @submit.prevent="addNewSong">
        <input type="text" v-model="newSong.genre" placeholder="Genre" required>
        <input type="text" v-model="newSong.song_name" placeholder="Song Name" required>
        <input type="text" v-model="newSong.duration" placeholder="Duration" required>
        <textarea v-model="newSong.lyrics" placeholder="Lyrics" required></textarea>
        <input type="text" v-model="newSong.creator_name" placeholder="Creator Name" required>
        <input type="text" v-model="newSong.song_path" placeholder="Song Path" required>
        <input type="text" v-model="newSong.image_path" placeholder="Image Path" required>
        <input type="integer" v-model="newSong.avg_rating" placeholder="Average Rating" required>
        <button type="submit">Add Song</button>
        <button @click="closeAddSongModal">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userName: localStorage.getItem('userName') || 'John Doe', // Use userName from localStorage or default to 'John Doe'
      total_songs: 10,
      avg_rating: 4.5,
      genre: 'Pop',
      songs: [],
      newSong: {
        genre: '',
        song_name: '',
        duration: '',
        lyrics: '',
        creator_name: '',
        song_path: '',
        image_path: '',
        avg_rating: 0
      },
      isLyricsPopupOpen: false,
      isAddSongModalOpen: false
    };
  },
  methods: {
    redirectToAlbumPage() {
      this.$router.push('/album');
    },
    redirectToLogout() {
      this.$router.push('/login');
    },
    confirmDelete(songId, songName) {
      const result = confirm(`Are you sure you want to delete the song "${songName}"?`);
      if (result) {
        this.deleteSong(songId);
      }
    },
    deleteSong(songId) {
      // Implement delete song logic here (e.g., API call)
      console.log('Deleting song with ID:', songId);
    },
    viewLyrics(songId) {
      // Implement view lyrics logic here (e.g., API call)
      console.log('Viewing lyrics for song with ID:', songId);
    },
    closeLyricsPopup() {
      this.isLyricsPopupOpen = false;
      console.log('Closing lyrics popup');
    },
    openAddSongModal() {
      this.isAddSongModalOpen = true;
      console.log('Opening add song modal');
    },
    closeAddSongModal() {
      this.isAddSongModalOpen = false;
      console.log('Closing add song modal');
    },
    addNewSong() {
      // Implement adding new song logic here (e.g., API call)
      axios.post('/api/add_song', this.newSong)
        .then(() => {
          alert('Song added successfully');
          this.closeAddSongModal();
          // Optionally, refresh song list
        })
        .catch(error => {
          console.error('Error adding song:', error);
          alert('Failed to add song. Please try again.');
        });
    }
  }
};
</script>


<style scoped>
/* CSS Styles */

.creator-page {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  background-color: #333;
  color: #fff;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100px;
  margin-bottom: 10px;
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

.user-info-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.user-info {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-left: 50px;
}

.user-image {
  border-radius: 50%;
  margin-bottom: 10px;
  height: 200px;
  width: 200px;
  transition: transform 0.2s ease-in-out;
}

.user-info:hover .user-image {
  transform: scale(1.1);
}

.user-info p {
  margin: 0;
  font-weight: bold;
  font-size: larger;
}

.stats-container {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  width: 100%;
}

.stats-box {
  background-color: #f2f2f2;
  padding: 20px;
  text-align: center;
  margin: 0 10px;
  border-radius: 10px;
  flex: 1;
  max-width: 250px;
  transition: background-color 0.3s ease-in-out, transform 0.2s ease-in-out;
  font-weight: bold;
}

.stats-box:hover {
  background-color: #b0b0b0;
  transform: scale(1.05);
}

section {
  margin-top: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.uploads-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

h2 {
  padding-left: 8px;
  margin-top: 20px;
  margin-bottom: 1px;
}

.add-song-button {
  margin-bottom: 10px;
  padding: 16px 24px;
  background-color: #E35F21;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out, transform 0.2s ease-in-out;
  margin-top: 20px;
  height: 50px;
}

.add-song-button:hover {
  background-color: #9c4117;
  transform: scale(1.05);
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

hr {
  margin-top: 20px;
  border: none;
  border-top: 1px solid ;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px;
  margin-top: auto;
}

.lyrics-popup {
  display: none;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 20px;
  background-color: #fff;
  border: 2px solid #333;
  z-index: 1000;
}

.close-popup {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
}

.add-song-modal {
  width: 500px;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  border: 2px solid #333;
  z-index: 1000;
}

.add-song-modal h2 {
  margin-bottom: 20px;
}

.add-song-modal form {
  display: flex;
  flex-direction: column;
}

.add-song-modal input,
.add-song-modal textarea {
  margin-bottom: 10px;
  padding: 8px;
}

.add-song-modal button {
  padding: 12px 20px;
  margin-top: 10px;
  cursor: pointer;
}

</style>
