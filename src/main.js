import { createApp } from 'vue'; // Import createApp from Vue 3
import App from './App.vue';
import router from './router';

const app = createApp(App); // Create Vue 3 app instance

app.use(router); // Use Vue Router

app.mount('#app'); // Mount the app to the DOM
