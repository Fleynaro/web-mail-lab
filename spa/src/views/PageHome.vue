<template>
  <messages-list :messages="[{ author: 'test', message: 'some text', claps: 1 }]" />
</template>

<script>
import MessagesList from '../components/MessagesList.vue';

export default {
  name: 'PageHome',

  components: { MessagesList },
};
</script>

<style scoped>

</style>
