import { createRouter, createWebHistory } from 'vue-router';

export const router = createRouter({
  history: createWebHistory(process.env.VUE_APP_BASE_URL),

  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/PageHome.vue'),
    },

    {
      path: '/messages/:id(\\d+)',
      name: 'message',
      component: () => import('../views/PageMessage.vue'),
    },
  ],
});
