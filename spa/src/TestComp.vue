<template>
  <span style="color: red">{{ message }} ({{ reversedMessage }})</span>
  <button @click="changeMessage">Change Message</button>

  <div class="mb-3">
    <div class="alert alert-success">Сообщение отправлено</div>
  </div>

  <button class="btn btn-primary" data-bs-target="#collapseTarget" data-bs-toggle="collapse">Bootstrap collapse</button>
  <div class="collapse py-2" id="collapseTarget">This is the toggle-able content!</div>
</template>

<script>
export default {
  name: 'TestComp',

  data() {
    return {
      message: 'Hello Vue!',
    };
  },

  computed: {
    reversedMessage() {
      return this.message.split('').reverse().join('');
    },
  },

  methods: {
    changeMessage() {
      this.message = 'Hello World!';
    },
  },
};
</script>
