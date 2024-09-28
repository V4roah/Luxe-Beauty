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
        @click="getCategory(category.id, category.name)"
      >
        {{ category.name }}
      </button>
      <hr />
    </div>
  </section>
</template>

<script setup>
import axios from "axios";
import { ref, defineEmits, onMounted } from "vue";

const categories = ref([]);
const categoryId = ref(null);
const categoryName = ref(null);

const emit = defineEmits(["getCategoryId"]);

const getCategory = (id, name) => {
  emit("getCategoryId", id, name);
};

onMounted(() => {
  axios
    .get("http://localhost:8000/api/v1.0/categories/")
    .then((response) => {
      categories.value = response.data;
    })
    .catch((error) => {
      console.log("Error fetching categories", error);
    });
});
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
