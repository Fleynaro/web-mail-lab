<template>
  <card v-if="message">
    <template v-slot:header>
      <div class="text-muted" data-test="message-author">{{ message.author }}</div>
    </template>

    <template v-slot:main>
      <div data-test="message-text">{{ message.message }}</div>
    </template>

    <template v-slot:footer>
      <message-clap-btn :message="message" @clap="onClap" class="ms-auto" />
    </template>
  </card>
  <alert v-else ref="alert" />
</template>

<script>
import { getMessage, clapMessage } from '../api/messages.api';
import Alert from '../components/Alert.vue';
import Card from '../components/Card.vue';
import MessageClapBtn from '../components/MessageClapBtn.vue';

export default {
  name: 'PageMessage',

  components: { Alert, Card, MessageClapBtn },

  data() {
    return {
      message: null,
    };
  },

  created() {
    getMessage(this.$route.params.id).then((message) => {
      this.message = message;
      this.$refs.alert.show = false;
    });
  },

  mounted() {
    this.$refs.alert.loading();
  },

  methods: {
    onClap(btn) {
      clapMessage(btn.message.id).then((info) => {
        btn.message.claps = info.count;
        btn.disabled = false;
      });
    },
  },
};
</script>
