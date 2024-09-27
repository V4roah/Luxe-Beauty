<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
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
            <router-link class="nav-link active" aria-current="page" to="/"
              >Inicio</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/about"
              >Acerca de Nosotros</router-link
            >
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Buscar..."
            aria-label="Search"
          />
          <button class="btn btn-outline-pink" type="submit">Buscar</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script setup></script>

<style>
.btn-outline-pink {
  color: #ff69b4 !important;
  border: 2px solid #ff69b4 !important;
  background-color: transparent !important;
}

.btn-outline-pink:hover {
  background-color: #ff69b4 !important;
  color: white !important;
}
</style>
