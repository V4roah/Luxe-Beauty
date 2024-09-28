<template>
  <div class="container">
    <NavBarComponent @getSearchText="search" />

    <NavigationComponent @getCategoryId="categoryId" />

    <div class="mb-3" v-if="categoryReceived">
      <h3>
        Productos de la categoria <strong>{{ categoryReceived }}</strong>
      </h3>
      <button class="btn btn-lg btn-warning" @click="resetFilter">
        Mostrar todos los productos
      </button>
      <div
        class="alert alert-warning mt-3"
        role="alert"
        v-if="filteredProducts.length === 0"
      >
        Lamentablemente no existe productos para la categorias
        <strong>{{ categoryReceived }}</strong>
      </div>
    </div>

    <div class="mb-3" v-if="searchTextRule">
      <h3>
        Productos con el texto <strong>{{ searchTextRule }}</strong>
      </h3>
      <button class="btn btn-lg btn-warning" @click="resetFilter">
        Mostrar todos los productos
      </button>
      <div
        class="alert alert-warning mt-3"
        role="alert"
        v-if="filteredProducts.length === 0"
      >
        Lamentablemente no existe productos para el texto
        <strong>{{ searchTextRule }}</strong>
      </div>
    </div>

    <div>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="product in filteredProducts" :key="product.id">
          <div class="card text-center">
            <img
              :src="product.image"
              class="card-img-top"
              alt="Imagen de {{product.name}}"
            />
            <div class="card-body">
              <h5 class="card-title">{{ product.name }}</h5>
              <h6 class="card-subtitle mb-2 text-body-secondary">
                {{ product.category_name }}
              </h6>
              <p class="card-text">{{ product.description }}</p>
            </div>
            <div class="card-footer text-danger">
              PRECIO: ${{ Math.floor(product.price) }} - Por
              {{ product.price_type_description }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import NavigationComponent from "@/components/NavigationComponent.vue";
import NavBarComponent from "@/components/NavBarComponent.vue";

import { ref, onMounted } from "vue";

const allProducts = ref([]);
const filteredProducts = ref([]);
const categoryReceived = ref(null);
const searchTextRule = ref(null);

const search = (searchText) => {
  categoryReceived.value = null;
  searchTextRule.value = searchText;

  if (searchText) {
    filteredProducts.value = allProducts.value.filter((product) => {
      const productName = product.name.toLowerCase();
      const productDescription = product.description.toLowerCase();
      const searchTerm = searchText.toLowerCase();
      return (
        productName.includes(searchTerm) ||
        productDescription.includes(searchTerm)
      );
    });
  } else {
    filteredProducts.value = allProducts.value;
  }
};

const categoryId = (categoryId, categoryName) => {
  searchTextRule.value = null;
  categoryReceived.value = categoryName;
  if (categoryId) {
    filteredProducts.value = allProducts.value.filter(
      (product) => product.category === categoryId
    );
  } else {
    filteredProducts.value = allProducts.value;
  }
};

const resetFilter = () => {
  categoryReceived.value = null;
  searchTextRule.value = null;
  filteredProducts.value = allProducts.value;
};
onMounted(() => {
  axios
    .get("http://localhost:8000/api/v1.0/products/")
    .then((response) => {
      allProducts.value = response.data;
      filteredProducts.value = allProducts.value;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>

<style>
.card {
  border: 2px solid gray !important;
}
</style>
