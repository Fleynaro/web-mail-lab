import { createApp } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Popover } from 'bootstrap';
import App from './App.vue';

createApp(App).mount('#app');

var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new Popover(popoverTriggerEl);
});
