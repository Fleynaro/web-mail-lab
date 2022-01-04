<template>
  <button class="btn" @click="$emit('clap')">
    👏🏻 <span data-test="clap-count">{{ message.claps }}</span>
  </button>
</template>

<script>
export default {
  name: 'MessageClapBtn',

  props: {
    message: {
      type: Object,
      required: true,
    },
  },

  emits: ['clap'],
};
</script>

<style scoped></style>
