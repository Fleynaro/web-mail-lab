<template>
<card>
    <template v-slot:header>
        {{message.author}}
    </template>
    <template v-slot:main>
        {{message.message}}
    </template>
    <template v-slot:footer>
        {{message.claps}}
    </template>
</card>
</template>

<script>
import Card from './Card.vue';

export default {
  name: 'MessagesListItem',

  components: { Card },

  props: {
    message: {
      type: Object,
      required: true
    }
  },

  emits: ['clap'],
};
</script>

<style scoped>

</style>
