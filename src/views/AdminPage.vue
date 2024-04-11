<template>
    <div class="wrapper">
      <!-- Header Section -->
      <header class="header">
        <div class="left-header">
          <img class="logo" src="@/assets/harmonix.png" alt="Logo">
        </div>
        <div class="title">
          <h1>ADMIN DASHBOARD</h1>
        </div>
        <div class="right-header">
          <button @click="navigateTo('/song')">Songs List</button>
          <button @click="logout">Log out</button>
        </div>
      </header>

      <br>
  
      <!-- Main Content Section -->
      <div class="main-content">
        <!-- Left Content - Statistics Boxes -->
        <div class="left-content">
          <div class="box">
            <div class="box-title">Number of Users</div>
            <div class="box-content">{{ numUsers }} Users</div>
          </div>
          <div class="box">
            <div class="box-title">Number of Creators</div>
            <div class="box-content">{{ numCreators }} Creators</div>
          </div>
          <div class="box">
            <div class="box-title">Number of Songs</div>
            <div class="box-content">{{ numSongs }} Songs</div>
          </div>
          <div class="box">
            <div class="box-title">Number of Playlists</div>
            <div class="box-content">{{ numPlaylists }} Playlists</div>
          </div>
          <div class="box">
            <div class="box-title">Number of Genres</div>
            <div class="box-content">{{ numGenres }} Genres</div>
          </div>
        </div>
  
        <!-- Right Content - Graphs -->
        <div class="right-content">
          <div class="graph-box small">
            <div class="chart-container">
              <div class="box-title">Top Creators by Average Ratings</div>
              <canvas ref="topCreatorsChart"></canvas>
            </div>
          </div>
          <div class="graph-box small">
            <div class="chart-container">
              <div class="box-title">Top Songs by Average Ratings</div>
              <canvas ref="topSongsChart"></canvas>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Footer Section -->
      <footer class="footer">
        <p>&copy; Harmonix. All rights reserved.</p>
        <p>Contact: contact@harmonix.com</p>
      </footer>
    </div>
  </template>
  
  <script>
  import Chart from 'chart.js/auto';
  
  export default {
    data() {
      return {
        numUsers: 0,
        numCreators: 0,
        numSongs: 0,
        numPlaylists: 0,
        numGenres: 0,
        currentGraphIndex: 0,
        topCreators: [],
        topSongs: []
      };
    },
    mounted() {
      // Mock data for demonstration
      this.numUsers = 100;
      this.numCreators = 50;
      this.numSongs = 500;
      this.numPlaylists = 200;
      this.numGenres = 10;
      this.topCreators = [
        { creatorname: 'Creator A', average_rating: 4.5 },
        { creatorname: 'Creator B', average_rating: 4.8 },
        { creatorname: 'Creator C', average_rating: 4.2 }
      ];
      this.topSongs = [
        { song_name: 'Song X', average_rating: 4.7 },
        { song_name: 'Song Y', average_rating: 4.6 },
        { song_name: 'Song Z', average_rating: 4.9 }
      ];
      this.createBarChart('topCreatorsChart', this.topCreators, 'creatorname', 'average_rating');
      this.createBarChart('topSongsChart', this.topSongs, 'song_name', 'average_rating');
    },
    methods: {
      createBarChart(elementId, data, labelKey, dataKey) {
        const ctx = this.$refs[elementId].getContext('2d');
        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: data.map(item => item[labelKey]),
            datasets: [{
              label: 'Average Ratings',
              data: data.map(item => item[dataKey]),
              backgroundColor: this.generateRandomColors(data.length),
              borderColor: this.generateRandomColors(data.length),
              borderWidth: 1
            }]
          },
          options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
        });
      },
      generateRandomColors(count) {
        const colors = [];
        for (let i = 0; i < count; i++) {
          const randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
          colors.push(randomColor);
        }
        return colors;
      },
      navigateTo(path) {
        this.$router.push(path);
      },
      logout() {
        // Handle logout action
        // Example: Redirect to login page
        this.$router.push('/');
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add scoped CSS styles here */
  .wrapper {
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
  }
  
  .logo {
    width: 200px;
    height: 100%;
  }
  
  .title {
    flex: 1;
    text-align: center;
    font-size: 16px;
    font-weight: bold;
  }
  
  .right-header {
    display: flex;
    align-items: center;
  }
  
  button {
    padding: 10px 20px;
    margin-right: 10px;
    background-color: #333;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    font-size: 16px;
  }
  
  button:hover {
    background-color: #555;
  }
  
  .main-content {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    margin-top: 20px; /* Adjust top margin */
  }
  
  .left-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
  
  .box {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  
  .box-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
    text-align: center;
  }
  
  .box-content {
    font-size: 20px;
    text-align: center;
  }
  
  .right-content {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin-top: 20px; /* Adjust top margin */
  }
  
  .graph-box {
    flex: 1;
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    height: 400px;
  }
  
  .chart-container {
    height: 300px;
  }
  
  .footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 20px;
    margin-top: auto;
  }
  </style>
  