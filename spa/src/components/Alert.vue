<template>
    <div v-if="type === 'loading'" class="alert alert-warning d-flex align-items-center mb-3" data-test="send-alert">
        <div class="spinner-border me-2"></div>
        <div class="text-muted">Загрузка...</div>
    </div>
    <div v-if="type === 'success'" class="alert alert-success mb-3" data-test="send-alert">
        <div class="text-muted">{{ message }}</div>
    </div>
    <div v-if="type === 'error'" class="alert alert-danger mb-3" data-test="send-alert">
        <div class="text-muted">{{ message }}</div>
    </div>
</template>

<script>
export default {
  name: 'Alert',

  data() {
    return {
      show: false,
      type: '',
      message: '',
    };
  },

  methods: {
    loading() {
      this.show = true;
      this.type = 'loading';
    },

    success(message) {
      this.message = message;
      this.show = true;
      this.type = 'success';
    },

    error(error) {
      this.message = error;
      this.show = true;
      this.type = 'error';
    },
  },
};
</script>

<style scoped>
.spinner-border {
    width: 1.5em;
    height: 1.5em;
}
</style>
