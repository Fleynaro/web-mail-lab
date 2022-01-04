<template>
  <ul class="list-unstyled">
    <messages-list-item v-for="message in messages" :key="message" :message="message" @clap="$emit('clap', message)" />
  </ul>
</template>

<script>
import MessagesListItem from './MessagesListItem.vue';

export default {
  name: 'MessagesList',

  components: { MessagesListItem },

  props: {
    messages: {
      type: Array,
      required: true,
    },
  },

  emits: ['clap'],
};
</script>

<style scoped></style>
