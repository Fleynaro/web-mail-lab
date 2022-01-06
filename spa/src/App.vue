<template>
  <div class="d-flex flex-column bg-light min-vh-100">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <router-link :to="`/`" class="navbar-brand mx-auto">📨 Мини-почта 📨</router-link>
      </div>
    </nav>

    <main class="container flex-fill my-3">
      <div class="alert alert-secondary mb-3">
        <div class="text-muted"><a href="/labs/mail">Перейти</a> в традиционный Web</div>
      </div>

      <router-view v-slot="{ Component }">
        <keep-alive max="1">
          <component :is="Component" />
        </keep-alive>
      </router-view>
    </main>

    <footer class="bg-dark text-light py-3">
      <div class="container text-center">Лабораторная работа по курсу Web-программирования. Выполнено студентом Пуховым Николаем ПМИ-4</div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>
