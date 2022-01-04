import axios from 'axios';

export const httpService = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
});
