<template>
  <card v-if="message">
    <template v-slot:header>
      <div class="text-muted" data-test="message-author">{{ message.author }}</div>
    </template>

    <template v-slot:main>
      <div data-test="message-text">{{ message.message }}</div>
    </template>

    <template v-slot:footer>
      <message-clap-btn :message="message" @clap="clap" class="ms-auto" />
    </template>
  </card>
</template>

<script>
import { getMessage, clapMessage } from '../api/messages.api';
import Card from '../components/Card.vue';
import MessageClapBtn from '../components/MessageClapBtn.vue';

export default {
  name: 'PageMessage',

  components: { Card, MessageClapBtn },

  data() {
    return {
      message: null,
    };
  },

  created() {
    getMessage(this.$route.params.id).then((message) => {
      this.message = message;
    });
  },

  methods: {
    clap() {
      clapMessage(this.message.id).then((info) => {
        this.message.claps = info.count;
      });
    },
  },
};
</script>

<style scoped></style>
