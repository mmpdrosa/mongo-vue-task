import axios from 'axios'

console.log(process.env.VUE_APP_API_URL)

export const api = axios.create({
  baseURL: 'https://flask-video-task.onrender.com/api',
})