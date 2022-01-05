<template>
  <form class="card border-secondary send-form" @submit="onSubmit" data-test="send-form">
    <fieldset :disabled="disabled">
      <legend class="card-header h5 border-secondary bg-dark text-light">📩 Отправить письмо</legend>
      <div class="card-body">
        <alert ref="alert" />

        <div class="mb-3">
          <label for="sender" class="form-label">От кого:</label>
          <input id="sender" name="sender" v-model="sender" class="form-control" type="text" placeholder="Имя отправителя" />
        </div>
        <div class="mb-3">
          <label for="message" class="form-label">Сообщение:</label>
          <textarea id="message" name="message" v-model="message" class="form-control" placeholder="Текст сообщения"></textarea>
        </div>
        <div class="d-flex">
          <button class="btn btn-outline-success ms-auto">✏️ Отправить</button>
        </div>
      </div>
    </fieldset>
  </form>
</template>

<script>
import Alert from './Alert.vue';

export default {
  name: 'MessageSentForm',

  components: { Alert },

  data() {
    return {
      sender: '',
      message: '',
      disabled: false,
    };
  },

  emits: ['submit'],

  methods: {
    onSubmit(e) {
      e.preventDefault();
      this.$refs.alert.loading();
      this.disabled = true;
      this.$emit('submit');
    },

    success(newMessage) {
      this.$refs.alert.success('Сообщение отправлено');
      this.disabled = false;
      this.sender = '';
      this.message = '';
    },

    error(error) {
      this.$refs.alert.error(`${error}`);
      this.disabled = false;
    },
  },
};
</script>

<style scoped></style>
