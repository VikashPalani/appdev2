<template>
  <div class="wrapper">
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

    <div class="main-content">
      <div class="left-content">
        <div class="box" v-for="(value, label) in statistics" :key="label">
          <div class="box-title">{{ label }}</div>
          <div class="box-content">{{ value }}</div>
        </div>
      </div>

      <div class="right-content">
        <div class="graph-box" v-for="(graph, index) in graphs" :key="index">
          <div class="chart-container">
            <div class="box-title">{{ graph.title }}</div>
            <canvas ref="chartCanvas" :id="graph.canvasRef" width="400" height="300"></canvas>
          </div>
        </div>
      </div>
    </div>

    <footer class="footer">
      <p>&copy; Harmonix. All rights reserved.</p>
      <p>Contact: contact@harmonix.com</p>
    </footer>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';

export default {
  data() {
    return {
      statistics: {},
      graphs: []
    };
  },
  mounted() {
    this.fetchAdminData();
  },
  methods: {
    fetchAdminData() {
      axios.get('/api/admin_data')
        .then(response => {
          const data = response.data;
          this.statistics = {
            'Number of Users': data.num_users,
            'Number of Creators': data.num_creators,
            'Number of Songs': data.num_songs,
            'Number of Playlists': data.num_playlists,
            'Number of Genres': data.num_genres
          };
          this.generateGraphs(data.top_creators, 'Top Creators by Average Ratings');
          this.generateGraphs(data.top_songs, 'Top Songs by Average Ratings');
        })
        .catch(error => {
          console.error('Error fetching admin data:', error);
        });
    },
    generateGraphs(data, title) {
      if (!data || data.length === 0) {
        console.warn(`No data provided for '${title}' graph.`);
        return;
      }

      const labels = data.map(item => item.creatorname || item.song_name);
      const dataset = data.map(item => item.average_rating);
      const canvasRef = `graph-${this.graphs.length}`;

      this.graphs.push({ title, canvasRef });

      this.$nextTick(() => {
        const canvas = document.getElementById(canvasRef);
        console.log('Canvas Element:', canvas);

        if (!canvas || !(canvas instanceof HTMLCanvasElement)) {
          console.error(`Invalid canvas element for ref '${canvasRef}'.`);
          return;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) {
          console.error(`Failed to get 2D rendering context for canvas '${canvasRef}'.`);
          return;
        }

        new Chart(ctx, {
          type: 'bar',
          data: {
            labels,
            datasets: [{
              label: 'Average Ratings',
              data: dataset,
              backgroundColor: this.generateRandomColors(labels.length),
              borderColor: this.generateRandomColors(labels.length),
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
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>

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
  margin-top: 20px;
}

.left-content {
  margin-bottom: 20px;
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
  margin-top: 20px;
}

.graph-box {
  flex: 1;
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  height: 600px;
  margin-bottom: 20px;
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
