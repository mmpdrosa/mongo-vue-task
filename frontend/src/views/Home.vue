<template>
  <div>
    <v-dialog width="500">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" text="Open Dialog"> </v-btn>
      </template>

      <template v-slot:default="{ isActive }">
        <v-card title="New Video">
          <video-form @videoSubmitted="handleFormSubmitted" />


          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
              text="Close Dialog"
              @click="isActive.value = false"
            ></v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>

    <router-link to="/themes">Go to themes</router-link>

    <h2>Video List</h2>
    <v-list>
      <v-list-item-group v-if="videos.length > 0">
        <v-list-item v-for="video in videos" :key="video.id">
          <v-list-item-content>
            <v-list-item-title>{{ video.name }}</v-list-item-title>
            <v-list-item-subtitle>URL: {{ video.url }}</v-list-item-subtitle>
            <v-list-item-subtitle>Theme: {{ video.theme }}</v-list-item-subtitle>
            <v-list-item-subtitle>
              Thumbs Up: {{ video.thumbs_up }} | Thumbs Down: {{ video.thumbs_down }}
            </v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn @click="thumbsUp(video.id)">Thumbs Up</v-btn>
            <v-btn @click="thumbsDown(video.id)">Thumbs Down</v-btn>
          </v-list-item-action>
        </v-list-item>
      </v-list-item-group>
      <v-alert v-else>No videos available</v-alert>
    </v-list>
  </div>
</template>


<script lang="ts" setup>
import VideoForm from '@/components/VideoForm.vue';
import { api } from '@/lib/axios';
import { isAxiosError } from 'axios';
import { ref, onMounted } from 'vue';


interface Video {
  id: string;
  name: string;
  theme: string;
  thumbs_up: number;
  thumbs_down: number;
  url: string;
}

const videos = ref<Video[]>([])

const fetchVideos = async () => {
  try {
    const response = await api.get('/videos')
    videos.value = response.data

    console.log('videos', videos.value)

  } catch (error) {
    if (isAxiosError(error)) {
      console.error('Error:', error.message)
    } else {
      console.error('Error:', error)
    }
  }
}

const thumbsUp = async (id: string) => {
  try {
    const response = await api.put(`/videos/${id}/thumbs-up`)

    videos.value = videos.value.map((video) =>
      video.id === id ? { ...video, thumbs_up: video.thumbs_up + 1 } : video
    );

    console.log('response', response.data)
  } catch (error) {
    if (isAxiosError(error)) {
      console.error('Error:', error.message)
    } else {
      console.error('Error:', error)
    }
  }
}

const thumbsDown = async (id: string) => {
  try {
    const response = await api.put(`/videos/${id}/thumbs-down`)
    
    videos.value = videos.value.map((video) =>
      video.id === id ? { ...video, thumbs_down: video.thumbs_down + 1 } : video
    );

    console.log('response', response.data)
  } catch (error) {
    if (isAxiosError(error)) {
      console.error('Error:', error.message)
    } else {
      console.error('Error:', error)
    }
  }
}

const handleFormSubmitted = () => {
  fetchVideos()
}

onMounted(() => {
  fetchVideos()
})

</script>
