import { httpService } from './http.service';

export function getMessages() {
  return httpService.get('/messages').then((response) => response.data);
}

export function getMessage(id) {
  return httpService.get(`/messages/${id}`).then((response) => response.data);
}

export function createMessage(message) {
  return httpService.post('/messages', message).then((response) => response.data);
}

export function clapMessage(id) {
  return httpService.post(`/messages/${id}/claps`).then((response) => response.data);
}
