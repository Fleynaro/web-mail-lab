import { createApp } from 'vue';
import { router } from './router';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Popover } from 'bootstrap';
import App from './App.vue';

createApp(App).use(router).mount('#app');

var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
popoverTriggerList.map(function (popoverTriggerEl) {
  return new Popover(popoverTriggerEl);
});
