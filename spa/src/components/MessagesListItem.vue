<template>
  <li class="mb-3">
    <card>
      <template v-slot:header>
        <div class="text-muted" data-test="message-author">{{ message.author }}</div>
        <router-link :to="`/messages/${message.id}`" class="card-link ms-auto" data-test="message-open">Открыть ↗️</router-link>
      </template>

      <template v-slot:main>
        <div data-test="message-text">{{ message.message }}</div>
      </template>

      <template v-slot:footer>
        <message-clap-btn :message="message" @clap="$emit('clap')" class="ms-auto" />
      </template>
    </card>
  </li>
</template>

<script>
import Card from './Card.vue';
import MessageClapBtn from './MessageClapBtn.vue';

export default {
  name: 'MessagesListItem',

  components: { Card, MessageClapBtn },

  props: {
    message: {
      type: Object,
      required: true,
    },
  },

  emits: ['clap'],
};
</script>

<style scoped></style>
