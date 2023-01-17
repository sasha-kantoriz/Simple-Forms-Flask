import { createRouter, createWebHistory } from 'vue-router';
import Main from '../views/Main.vue';
import User from '../views/User.vue';


const routes = [
  {
    path: '/',
    name: 'home',
    component: Main
  },
  {
    path: '/user/:id',
    name: 'user',
    component: User
  },
]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router