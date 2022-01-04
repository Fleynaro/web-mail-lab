<template>
  <article class="card">
    <div class="card-body">
      <header class="card-title d-flex">
        <slot name="header" />
      </header>

      <div class="card-text">
        <slot name="main" />
      </div>

      <div class="d-flex">
        <slot name="footer" />
      </div>
    </div>
  </article>
</template>

<script>
export default {
  name: 'Card',
};
</script>

<style scoped></style>
