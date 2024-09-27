<template>
  <section class="mt-5 text-center mx-auto">
    <h1 class="text-pink">Luxe Beauty</h1>
    <img class="img-fluid" :src="require('@/assets/img/fondo.jpg')" alt="" />
    <div class="mt-3" v-if="$route.path !== '/about'">
      <button
        type="button"
        class="btn btn-pink"
        v-for="category in categories"
        :key="category.id"
        @click="getCategoryId(category.id, category.name)"
      >
        {{ category.name }}
      </button>
      <hr />
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      categories: [],
      categoryId: null,
      categoryName: null,
    };
  },
  methods: {
    getCategoryId(categoryId, categoryName) {
      this.$emit("getCategoryId", categoryId, categoryName);
    },
  },
  mounted() {
    axios
      .get("http://localhost:8000/api/v1.0/categories/")
      .then((response) => {
        this.categories = response.data;
      })
      .catch((error) => {
        console.log("Error fetching categories", error);
      });
  },
};
</script>

<style>
button {
  margin-right: 5px;
}
button + button,
button:first-child {
  margin-left: 5px;
}

@media (max-width: 768px) {
  button {
    width: 100%;
    margin: 0 0 5px !important;
    box-sizing: border-box;
  }
}

.btn-pink {
  background-color: #ff69b4 !important;
  color: white !important;
}
</style>
