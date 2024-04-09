import { createRouter, createWebHistory } from 'vue-router'; // Import createRouter and createWebHistory from Vue Router

import LoginForm from './components/auth/LoginForm.vue';
import SignupForm from './components/auth/SignupForm.vue';
import HomePage from './views/HomePage.vue';
import UserPage from './views/UserPage.vue';
import SamplePage from './views/SamplePage.vue';
import CreatorPage from './views/CreatorPage.vue';
import SongPage from './views/SongPage.vue';



const routes = [
  { path: '/', component: HomePage }, // Set the HomePage as the landing page
  { path: '/login', component: LoginForm },
  { path: '/signup', component: SignupForm },
  { path: '/user', component: UserPage },
  { path: '/sample', component: SamplePage },
  { path: '/creator', component: CreatorPage },
  { path: '/song', component: SongPage }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
