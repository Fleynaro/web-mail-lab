<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <h1>Welcome to Your Vue.js App!</h1>
  <test-comp></test-comp>

  <div class="container">
    <ul class="nav nav-pills flex-column flex-sm-row py-3 bg-dark bg-gradient">
      <li class="nav-item">
        <a class="nav-link active" data-bs-toggle="tab" data-bs-target="#home" href="#">Active</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#">Link</a>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" data-bs-toggle="tab" data-bs-target="#contact" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another action</a></li>
        </ul>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" data-bs-toggle="tab" data-bs-target="#profile" type="button">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>

    <div class="tab-content" id="myTabContent">
      <div class="tab-pane fade show active" id="home">1</div>
      <div class="tab-pane" id="profile">2</div>
      <div class="tab-pane fade" id="contact">3</div>
    </div>

    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <img src="https://getbootstrap.com/docs/5.0/assets/brand/bootstrap-logo.svg" alt="" width="30" class="d-inline-block align-text-top" /> Navbar
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false"> Dropdown </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider" /></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
            </li>
          </ul>
          <form class="d-flex">
            <input class="form-control me-1" type="search" placeholder="Search" aria-label="Search" />
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>

    <form class="">
      <div class="form-check mb-3">
        <input type="checkbox" class="form-check-input is-invalid" id="validationFormCheck1">
        <label class="form-check-label" for="validationFormCheck1">Check this checkbox</label>
        <div class="invalid-feedback">Example invalid feedback text</div>
      </div>

      <div class="form-group">
          <label class="form-control-label">Name</label>
          <div class="input-group flex-wrap">
              <span class="input-group-addon"><span class="fa fa-lock"></span></span>
              <input name="name" class="form-control is-valid" type="text">
              <div class="invalid-feedback w-100">Custom error</div>
          </div>
      </div>
    </form>

    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col">
        <div class="card">
          <img class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="ard-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <img class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TestComp from './TestComp.vue';
import BsPopover from './BsPopover.vue';

export default {
  name: 'App',

  components: { TestComp, BsPopover },
};
</script>

<style scoped>
.container {
  max-width: 960px;
}
</style>
