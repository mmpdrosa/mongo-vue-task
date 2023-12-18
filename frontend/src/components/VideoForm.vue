<template>
  <form @submit.prevent="submit">
    <v-text-field
      v-model="name.value.value"
      :error-messages="name.errorMessage.value"
      label="Name"
    ></v-text-field>

    <v-text-field
      v-model="url.value.value"
      :error-messages="url.errorMessage.value"
      label="URL"
    ></v-text-field>

    <v-text-field
      v-model="theme.value.value"
      :error-messages="theme.errorMessage.value"
      label="Theme"
    ></v-text-field>

    <v-btn type="submit">Submit</v-btn>

    <v-btn @click="handleReset">Clear</v-btn>
  </form>
</template>

<script setup lang="ts">
import { api } from '@/lib/axios';
import { isAxiosError } from 'axios';
import { useField, useForm } from 'vee-validate'

const { handleSubmit, handleReset } = useForm({
  validationSchema: {
    name(value: string) {
      if (value?.length >= 2) return true

      return 'Name needs to be at least 2 characters.'
    },
    url(value: string) {
      if (value) return true

      return 'URL is required.'
    },
    theme(value: string) {
      if (value) return true

      return 'Theme is required.'
    },
  },
})

const name = useField('name')
const url = useField('url')
const theme = useField('theme')

const emit = defineEmits(['videoSubmitted'])

const submit = handleSubmit((values) => {
  api
    .post('/videos', values)
    .then(() => {
      handleReset()
      alert('Video submitted!')

      emit('videoSubmitted')
    })
    .catch((error) => {
      if (isAxiosError(error)) {
        console.error('Error:', error.message)
      } else {
        console.error('Error:', error)
      }
    })
})
</script>
