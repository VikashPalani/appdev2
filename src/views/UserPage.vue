<template>
    <div class="user-page">
      <header>
        <form @submit.prevent="search" class="search-bar">
          <input type="text" v-model="query" placeholder="Search...">
          <button type="submit">Search</button>
        </form>
        <img src="@/assets/harmonix.png" alt="Harmonix Logo" class="logo">
        <div class="header-buttons">
          <button @click="openCreatorLogin">Creator Login</button>
          <button @click="playlist">My Playlists</button>
          <button @click="signOut">Log Out</button>
        </div>
      </header>
      
      <div class="user-info">
        <p><strong>Welcome User!</strong></p>
      </div>
  
      <div class="section">
        <h2>SONGS</h2>
        <div class="list">
          <p v-if="query">Search results for "{{ query }}":</p>
          <div class="item" v-for="song in songs" :key="song.id">
            <img :src="`/${song.image_path}`" :alt="song.song_name" class="song-image">
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
                <span v-for="star in 5" :key="star" class="star" @click="rateSong(song.id, star)" :class="{ 'active': star <= song.rating }">&#9733;</span>
              </div>
              <div class="lyrics-container" @mouseover="showLyrics(song.id)" @mouseout="hideLyrics(song.id)">
                <p>{{ song.lyrics }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <hr>
  
      <div class="creators-section">
        <h2>CREATORS</h2>
        <div class="creators-list">
          <div class="creator-item" v-for="(creator, index) in creators" :key="index">
            <img :src="`/static/${creator.image}`" :alt="creator.name" class="creator-image">
          </div>
        </div>
        <div class="creators-names">
          <div class="creator-name" v-for="(creator, index) in creators" :key="index">{{ creator.name }}</div>
        </div>
      </div>
    
      <footer>
        <p>&copy; Harmonix. All rights reserved.</p>
        <p>Contact: contact@harmonix.com</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        query: '',
        songs: [],
        creators: [
          { name: 'Alan Walker', image: 'alanwalker.jpg' },
          { name: 'Ellie Goulding', image: 'elliegoulding.png' },
          { name: 'Imagine Dragons', image: 'imaginedragons.jpg' },
          { name: 'Justin Bieber', image: 'justinbieber.jpg' },
          { name: 'Hippie Sabotage', image: 'hippiesabotage.jpg' },
          { name: 'Otnicka', image: 'otnicka.jpg' }
        ]
      };
    },
    methods: {
      search() {
        console.log('Search button clicked');
      },
      signOut() {
        window.location.href = '/';
      },
      openCreatorLogin() {
        window.location.href = '/creator_login';
      },
      playlist() {
        window.location.href = '/playlist';
      },
      rateSong(songId, rating) {
        console.log(`Rated Song ${songId} with ${rating} stars`);
      },
      showLyrics(songId) {
        const lyricsContainer = document.querySelector(`.lyrics-container-${songId}`);
        if (lyricsContainer) {
          lyricsContainer.style.display = 'flex';
        }
      },
      hideLyrics(songId) {
        const lyricsContainer = document.querySelector(`.lyrics-container-${songId}`);
        if (lyricsContainer) {
          lyricsContainer.style.display = 'none';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .user-page {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
  }
  
  header {
    background-color: #333;
    color: #fff;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 70px;
  }
  
  .logo {
    height: 50px;
  }
  
  .search-bar {
    display: flex;
    align-items: center;
  }
  
  input[type="text"] {
    padding: 8px;
    border: none;
    border-radius: 4px;
    margin-right: 8px;
  }
  
  button {
    padding: 8px 12px;
    background-color: #333;
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
  
  .header-buttons button {
    margin-left: 10px;
  }
  
  .section {
    margin: 20px;
  }
  
  h2 {
    color: #333;
    font-size: 20px;
    text-align: center;
  }
  
  .list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  
  .item {
    width: 23%;
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

audio {
  width: 100%;
  margin-top: 10px;
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

.creators-section {
  margin: 20px;
  text-align: center;
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

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px;
  margin-top: 10px;
}

.user-info {
  background-color: #444444;
  color: #fff;
  padding: 10px;
  text-align: left;
  margin-bottom: 20px;
  margin-top: 15px;
}

.user-info p {
  margin: 0;
  font-size: 26px;
}
</style>

  