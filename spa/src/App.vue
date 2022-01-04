<template>
  <div class="d-flex flex-column bg-light min-vh-100">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand mx-auto" href="/">📨 Мини-почта 📨</a>
      </div>
    </nav>

    <main class="container flex-fill my-3">
      <router-view></router-view>
    </main>

    <footer class="bg-dark text-light py-3">
      <div class="container text-center">
        Лабораторная работа по курсу Web-программирования. Выполнено студентом Пуховым Николаем ПМИ-4
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style scoped>
.container {
  max-width: 960px;
}
</style>
