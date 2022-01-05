<template>
  <message-sent-form @submit="onSubmit" class="mb-3" />
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
      return [...this.messages].sort((a, b) => b.claps - a.claps);
    },
  },

  methods: {
    onSubmit(form) {
      createMessage({
        author: form.sender,
        message: form.message,
      })
        .then((message) => {
          this.messages.push(message);
          form.success(message);
        })
        .catch((error) => {
          form.error(error.response.data.message);
        });
    },

    onClap(btn) {
      clapMessage(btn.message.id).then((info) => {
        btn.message.claps = info.count;
        btn.disabled = false;
      });
    },
  },
};
</script>
