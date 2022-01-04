<template>
  <article class="card">
    <div class="card-body">
        <header class="card-title">
            <slot name="header"/>
        </header>
        
        <div class="card-text">
            <slot name="main"/>
        </div>

        <slot name="footer"/>
    </div>
</article>

</template>

<script>
export default {
  name: 'Card'
};
</script>

<style scoped>

</style>
