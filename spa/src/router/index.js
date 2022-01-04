import { createRouter, createWebHistory } from 'vue-router';

export const router = createRouter({
  history: createWebHistory(),

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
