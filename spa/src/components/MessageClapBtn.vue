<template>
  <button class="btn" @click="onClick" :disabled="disabled">
    👏🏻 <span data-test="clap-count">{{ message.claps }}</span>
  </button>
</template>

<script>
export default {
  name: 'MessageClapBtn',

  data() {
    return {
      disabled: false,
    };
  },

  props: {
    message: {
      type: Object,
      required: true,
    },
  },

  emits: ['clap'],

  methods: {
    onClick(e) {
      e.preventDefault();
      this.disabled = true;
      this.$emit('clap', this);
    },
  },
};
</script>
