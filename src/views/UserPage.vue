<template>

  <div>

    <UserHeader/>

    <div class="section">
      <hr><hr>
      <h2>SONGS</h2>
      <hr><hr>
      <div class="list">
        <p v-if="query">Search results for "{{ query }}":</p>
        <div v-for="song in songs" :key="song.song_id" class="item">

          <!-- Song Details -->
          <img :src="`/${song.image_path}`" :alt="song.song_name" class="song-image">
          <div class="lyrics-container">
            <p>{{ song.lyrics }}</p>
          </div>
          <div class="details">
            <div class="details-row">
              <p><strong>Name: {{ song.song_name }}</strong></p>
              <p><strong>By: {{ song.creator_name }}</strong></p>
            </div>
            <div class="details-row">
              <p><strong>Genre: {{ song.genre }}</strong></p>
              <p><strong>Average Rating: {{ song.avg_rating }}</strong></p>
            </div>
            <audio controls>
              <source :src="`/${song.song_path}`" type="audio/mpeg">
            </audio>
            <div class="rating">
              <p>Rate this song:</p>
              <span v-for="star in 5" :key="star" class="star" @click="rateSong(song.song_id, star)">
                &#9733;
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <hr><hr>

    <!-- Creators Section -->
    <div class="creators-section">
      <h2>CREATORS</h2>
      <div class="creators-list">
        <!-- Creator Images -->
        <div class="creator-item">
          <img src="@/assets/alanwalker.jpg" alt="alanwalker">
        </div>
        <div class="creator-item">
          <img src="@/assets/elliegoulding.png" alt="ellie goulding">
        </div>
        <div class="creator-item">
          <img src="@/assets/imaginedragons.jpg" alt="imagine dragons">
        </div>
        <div class="creator-item">
          <img src="@/assets/justinbieber.jpg" alt="justin bieber">
        </div>
        <div class="creator-item">
          <img src="@/assets/hippiesabotage.jpg" alt="hippie sabotage">
        </div>
        <div class="creator-item">
          <img src="@/assets/otnicka.jpg" alt="otnicka">
        </div>
      </div>
      <div class="creators-names">
        <!-- Creator Names -->
        <div v-for="(creator, index) in creators" :key="index" class="creator-name">{{ creator.name }}</div>
      </div>
    </div>

    <hr><hr>


    <!-- Footer -->
    <footer>
      <p>&copy; Harmonix. All rights reserved.</p>
      <p>Contact: contact@harmonix.com</p>
    </footer>
    <hr><hr>
  </div>
</template>

<script>

import UserHeader from '@/components/common/UserHeader.vue';
export default {
  components: {
    UserHeader
  },

  data() {
    return {
      searchQuery: '',
      query: '',
      songs: [],
      creators: [
        { name: 'Alan Walker', image: '@/assets/alanwalker.jpg' },
        { name: 'Ellie Goulding', image: '@/assets/elliegoulding.png' },
        { name: 'Imagine Dragons', image: '@/assets/imaginedragons.jpg' },
        { name: 'Justin Bieber', image: '@/assets/justinbieber.jpg' },
        { name: 'Hippie Sabotage', image: '@/assets/hippiesabotage.jpg' },
        { name: 'Otnicka', image: '@/assets/otnicka.jpg' }
      ]
    };
  },
  mounted() {
    // Fetch songs data when the component is mounted
    this.fetchSongs();
  },
  methods: {
    fetchSongs() {
  // Make API call to fetch songs data from backend
  fetch('/api/songs')
    .then(response => response.json())
    .then(data => {
      this.songs = data;
      // Print the value of song.image_path for each song
      this.songs.forEach(song => {
        console.log(song.image_path);
      });
    })
    .catch(error => {
      console.error('Error fetching songs:', error);
    });
    },

    search() {
      // Perform search based on the search query
      this.query = this.searchQuery;
      // Make API call to search songs
      fetch(`/api/search?query=${this.searchQuery}`)
        .then(response => response.json())
        .then(data => {
          this.songs = data;
        })
        .catch(error => {
          console.error('Error searching songs:', error);
        });
    },

    signOut() {
      // Implement sign-out functionality
    },

    goToPlaylists() {
      // Redirect to user's playlists page
    },

    rateSong(songId, rating) {
      // Rate the song
      // Make API call to rate the song
      fetch(`/api/songs/${songId}/rate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rating: rating })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // Update the rating locally
        const songIndex = this.songs.findIndex(song => song.song_id === songId);
        if (songIndex !== -1) {
          this.songs[songIndex].avg_rating = rating;
        }
      })
      .catch(error => {
        console.error('Error rating song:', error);
      });
    }
  }
};
</script>


<style>

/* Section Styles */
.section {
  margin: 10px;
}

.section h2 {
  color: #fff;
  font-size: 24px;
  text-align: center;
  padding: 5px;
}

/* List Styles */
.list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.item {
  width: 31%;
  margin: 10px 0;
  padding: 10px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
  position: relative;
  overflow: hidden;
}

.item:hover {
  transform: scale(1.05);
}

.item img {
  width: 100%;
  height: auto;
  border-radius: 6px;
  overflow: hidden;
}

.lyrics-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 80%;
  background-color: rgba(0, 0, 0, 0.9);
  color: #fff;
  display: none;
  align-items: flex-start;
  justify-content: flex-start;
  text-align: left;
  opacity: 100;
  transition: opacity 0.3s ease-in-out;
  z-index: 1;
}

.item:hover .lyrics-container {
  display: flex;
  opacity: 1;
}

.lyrics-container p {
  margin: 0;
  font-size: 14px;
  max-height: 100%;
  overflow-y: auto;
  padding: 10px;
  box-sizing: border-box;
}

.details {
  margin-top: 10px;
  text-align: center;
  display: flex;
  flex-direction: column;
}

.details-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.details p {
  margin: 5px 0;
}

.details strong {
  font-size: 16px;
  color: #333;
}

.rating {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.rating p {
  margin-right: 10px;
  font-weight: bold;
}

.star {
  font-size: 20px;
  color: #ccc;
  cursor: pointer;
}

.star:hover,
.star.active {
  color: #FFD700;
}

/* Creators Section Styles */

.creators-section h2 {
  color: #fff;
  font-size: 24px;
  margin-bottom: 10px;
}

.creators-section {
  margin: 20px;
  text-align: center;
  color: #fff
  
}

.creators-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.creator-item {
  width: 15%;
  margin: 10px 0;
  text-align: center;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
  border-radius: 50%;
}

.creator-item:hover {
  transform: scale(1.1);
}

.creator-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.creators-names {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.creator-name {
  width: 15%;
  text-align: center;
  font-size: 20px;
  margin: 10px 0;
}

/* Footer Styles */
footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px;
  margin-top: 10px;
}
</style>
