<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <h1>Welcome to Your Vue.js App!</h1>
  <test-comp></test-comp>

  <bs-popover title="Hello Popover" content="This is my content for the popover!" trigger="hover">
    <button class="btn btn-danger">Hover for popover</button>
  </bs-popover>
</template>

<script>
import TestComp from './TestComp.vue';
import BsPopover from './BsPopover.vue';

export default {
  name: 'App',

  components: { TestComp, BsPopover },
};
</script>
