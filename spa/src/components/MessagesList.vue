<template>
  <ul>
    <messages-list-item v-for="message in messages" :key="message" :message="message" />
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
      required: true
    }
  },

  emits: ['clap']
};
</script>

<style scoped>

</style>
