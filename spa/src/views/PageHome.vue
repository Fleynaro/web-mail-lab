<template>
  <message-sent-form ref="form" @submit="onSubmit" class="mb-3" />
  <messages-list v-if="messages" :messages="sortedMessages" @clap="onClap" />
  <alert v-else ref="alert" />
</template>

<script>
import { getMessages, createMessage, clapMessage } from '../api/messages.api';
import Alert from '../components/Alert.vue';
import MessageSentForm from '../components/MessageSentForm.vue';
import MessagesList from '../components/MessagesList.vue';

export default {
  name: 'PageHome',

  components: { Alert, MessageSentForm, MessagesList },

  data() {
    return {
      messages: null,
    };
  },

  created() {
    getMessages().then((messages) => {
      this.messages = messages;
      this.$refs.alert.show = false;
    });
  },

  mounted() {
    this.$refs.alert.loading();
  },

  computed: {
    sortedMessages() {
      return this.messages.sort((a, b) => b.claps - a.claps);
    },
  },

  methods: {
    onSubmit() {
      createMessage({
        author: this.$refs.form.sender,
        message: this.$refs.form.message,
      }).then((message) => {
        this.messages.push(message);
        this.$refs.form.success(message);
      }).catch((error) => {
        this.$refs.form.error(error.response.data.message);
      });
    },

    onClap(message) {
      clapMessage(message.id).then((info) => {
        message.claps = info.count;
      });
    },
  },
};
</script>

<style scoped></style>
