<template>
  <div id="element-to-convert">
    <div class="creator-page">
      <!-- Header -->
      <header>
        <div class="logo">
          <img src="@/assets/harmonix.png" alt="Website Logo">
        </div>
        <div class="header-buttons">
          <button @click="downloadAsPdf">Download Report</button>
          <button @click="redirectToAlbumPage">My Albums</button>
          <button @click="redirectToLogout">Logout</button>
        </div>
      </header>

      <!-- User Info Container -->
      <div class="user-info-container">
        <div class="user-info">
          <img class="user-image" src="@/assets/creator2.jpg" alt="Creator Photo">
          <p>{{ userName }}</p>
        </div>
        <div class="stats-container">
          <div class="stats-box">
            <p>Total Songs</p>
            <p>{{ songs.length }}</p>
          </div>
          <div class="stats-box">
            <p>Average Rating</p>
            <p>{{ averageRating }}</p>
          </div>
          <div class="stats-box">
            <p>Genre</p>
            <p>{{ firstGenre }}</p>
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
              <th>Lyrics</th>
              <th>Edit Lyrics</th>
              <th>Delete Song</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="song in songs" :key="song.song_id">
              <td>{{ song.song_name }}</td>
              <td>
                <button class="view-lyrics-button" @click="showLyrics(song)">View Lyrics</button>
              </td>
              <td><button class="edit-button" @click="openEditLyricsModal(song.song_id, song.lyrics)">Edit</button></td>
              <td><button class="delete-button" @click="confirmDelete(song.song_id)">Delete</button></td>
            </tr>
          </tbody>
        </table>
        
      </section>

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

      <!-- Edit Lyrics Modal -->
      <div class="modal" v-if="isEditModalOpen">
        <div class="modal-content">
          <span class="close" @click="closeEditModal">&times;</span>
          <h3>Edit Lyrics{{ selectedSong.song_name }}</h3>
          <textarea v-model="selectedSong.lyrics" placeholder="Enter updated lyrics" required></textarea>
          <button @click="saveEditedLyrics">Save</button>
          <button @click="closeEditModal">Cancel</button>
        </div>
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
          <input type="number" v-model="newSong.avg_rating" placeholder="Average Rating" required>
          <button type="submit">Add Song</button>
          <button @click="closeAddSongModal">Cancel</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import html2pdf from 'html2pdf.js';

export default {
  data() {
    return {
      userName: localStorage.getItem('userName') || 'John Doe',
      songs: [],
      isModalVisible: false,
      selectedSong: null,
      averageRating: 0,
      firstGenre: '',
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
      isAddSongModalOpen: false,
      isEditModalOpen: false
    };
  },
  methods: {

    downloadAsPdf(){
      html2pdf(document.getElementById('element-to-convert'),{
        margin:1,
        filename: 'MonthlyReport.pdf'
      });
    },
    fetchSongs() {
      axios.get('/api/songs')
        .then(response => {
          this.songs = response.data;
          this.filterSongsByCreator();
        })
        .catch(error => {
          console.error('Error fetching songs:', error);
        });
    },
    filterSongsByCreator() {
      this.songs = this.songs.filter(song => song.creator_name === this.userName);
      this.calculateAverageRating();
    },
    calculateAverageRating() {
      if (this.songs.length > 0) {
        const totalRating = this.songs.reduce((acc, song) => acc + song.avg_rating, 0);
        this.averageRating = (totalRating / this.songs.length).toFixed(2);
        this.firstGenre = this.songs[0].genre;
      } else {
        this.averageRating = 0;
        this.firstGenre = '';
      }
    },
    showLyrics(song) {
      axios.get(`/api/songs/${song.song_id}/lyrics`)
        .then(response => {
          this.selectedSong = { ...song, lyrics: response.data.lyrics };
          this.isModalVisible = true;
        })
        .catch(error => {
          console.error('Error fetching lyrics:', error);
        });
    },
    
    openEditLyricsModal(songId, currentLyrics) {
      this.selectedSong = { ...this.selectedSong, song_id: songId, lyrics: currentLyrics };
      this.isEditModalOpen = true;
    },
    closeEditModal() {
      this.isEditModalOpen = false;
      this.selectedSong = null;
    },
    saveEditedLyrics() {
      const { song_id, lyrics } = this.selectedSong;
      axios.put(`/api/songs/${song_id}`, { lyrics })
        .then(() => {
          this.closeEditModal();
          this.fetchSongs(); // Refresh songs after update
          alert('Lyrics updated successfully');
        })
        .catch(error => {
          console.error('Error updating lyrics:', error);
          alert('Failed to update lyrics');
        });
    },
    closeModal() {
      this.isModalVisible = false;
      this.selectedSong = null;
    },
    redirectToAlbumPage() {
      this.$router.push('/album');
    },
    redirectToLogout() {
      this.$router.push('/login');
    },
    confirmDelete(songId) {
      const confirmed = window.confirm('Are you sure you want to delete this song?');
      if (confirmed) {
        axios.delete(`/api/songs/${songId}`)
          .then(() => {
            this.fetchSongs();
            alert('Song deleted successfully');
          })
          .catch(error => {
            console.error('Error deleting song:', error);
          });
      }
    },
    openAddSongModal() {
      this.isAddSongModalOpen = true;
    },
    closeAddSongModal() {
      this.isAddSongModalOpen = false;
      this.resetNewSong();
    },
    addNewSong() {
      axios.post('/api/add_song', this.newSong)
        .then(() => {
          this.closeAddSongModal();
          this.fetchSongs();
          alert('Song added successfully');
        })
        .catch(error => {
          console.error('Error adding song:', error);
          alert('Failed to add song');
        });
    },
    resetNewSong() {
      this.newSong = {
        genre: '',
        song_name: '',
        duration: '',
        lyrics: '',
        creator_name: '',
        song_path: '',
        image_path: '',
        avg_rating: 0
      };
    }
  },
  mounted() {
    this.fetchSongs();
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
  margin: 15% auto;
}

.close {
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 24px;
  cursor: pointer;
  color: #aaa;
  font-weight: bold;
}

.close:hover {
  color: black;
}


.modal-content textarea {
  width: 100%;
  height: 200px;
  padding: 10px;
  box-sizing: border-box;
  margin-bottom: 10px;
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