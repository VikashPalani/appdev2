<template>
    <div>
      <h1>List of Songs</h1>
      <ul>
        <li v-for="song in songs" :key="song.song_id">
          <strong>Title:</strong> {{ song.title }} <br>
          <strong>Artist:</strong> {{ song.artist }} <br>
          <strong>Album:</strong> {{ song.album || 'N/A' }} <br>
          <strong>Release Date:</strong> {{ formatDate(song.release_date) }} <br>
          <strong>Audio URL:</strong> <a :href="song.audio_url" target="_blank">{{ song.audio_url }}</a> <br>
          <strong>Lyrics:</strong> <pre>{{ song.lyrics || 'N/A' }}</pre> <br>
          <strong>Creator ID:</strong> {{ song.creator_id }} <br>
          <hr>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        songs: []
      };
    },
    mounted() {
      this.fetchSongs();
    },
    methods: {
      async fetchSongs() {
        try {
          const response = await fetch('/api/songs');
          if (!response.ok) {
            throw new Error('Failed to fetch songs');
          }
          const data = await response.json();
          this.songs = data;
        } catch (error) {
          console.error('Error fetching songs:', error);
        }
      },
      formatDate(dateString) {
        if (!dateString) return 'N/A';
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
      }
    }
  };
  </script>
  
  <style scoped>
  /* Styles specific to this component */
  </style>
