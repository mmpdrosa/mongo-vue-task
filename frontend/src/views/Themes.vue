<template>
  <div>
    <router-link to="/">Home</router-link>
    <h2>Themes List</h2>
    <v-list>
      <v-list-item-group v-if="themes.length > 0">
        <v-list-item v-for="[theme, score] in themes" :key="theme">
          <v-list-item-content>
            <v-list-item-title>{{ theme }}</v-list-item-title>
            <v-list-item-subtitle>Score: {{ score }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
      <v-alert v-else>No themes available</v-alert>
    </v-list>
  </div>
</template>

<script lang="ts" setup>
import { api } from '@/lib/axios';
import { isAxiosError } from 'axios';
import { onMounted } from 'vue';
import { ref } from 'vue';

const themes = ref<[string, number][]>([])

const fetchThemes = async () => {
  try {
    const response = await api.get('/themes')
    themes.value = response.data.themes

    console.log('themes', themes.value)
  } catch (error) {
    if (isAxiosError(error)) {
      console.error('Error:', error.message)
    } else {
      console.error('Error:', error)
    }
  }
}

onMounted(() => {
  fetchThemes()
})

</script>