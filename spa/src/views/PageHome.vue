<template>
  <messages-list v-if="messages" :messages="sortedMessages" @clap="clap" />
</template>

<script>
import { getMessages, clapMessage } from '../api/messages.api';
import MessagesList from '../components/MessagesList.vue';

export default {
  name: 'PageHome',

  components: { MessagesList },

  data() {
    return {
      messages: null,
    };
  },

  created() {
    getMessages().then((messages) => {
      this.messages = messages;
    });
  },

  computed: {
    sortedMessages() {
      return this.messages.sort((a, b) => b.claps - a.claps);
    },
  },

  methods: {
    clap(message) {
      clapMessage(message.id).then((info) => {
        message.claps = info.count;
      });
    },
  },
};
</script>

<style scoped></style>
