<template>
  <main class="container my-5">
    <div class="row justify-content-between">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
      </div>
      <div class="col-md-5">
        <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="recipe.picture"
          alt
        >
      </div>
      <div class="col-md-5">
        <div class="recipe-details">
          <h4 class="text-right">مواد اولیه</h4>
          <p class="text-right">{{ recipe.ingredients }}</p>
          <h4 class="text-right">زمان پخت ⏱</h4>
          <p class="text-right">{{ recipe.prep_time }} دقیقه</p>
          <h4 class="text-right">سطح سختی</h4>
          <p class="text-right">{{ recipe.difficulty }}</p>
          <h4 class="text-right">دستور پخت</h4>
          <textarea class="form-control text-right" rows="10" v-html="recipe.prep_guide" disabled/>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "مشاهده دستور غذایی"
    };
  },
  async asyncData({$axios, params}) {
    try {
      let recipe = await $axios.$get(`/recipes/${params.id}`);
      return {recipe};
    } catch (e) {
      return {recipe: []};
    }
  },
  data() {
    return {
      recipe: {
        name: "",
        picture: "",
        ingredients: "",
        difficulty: "",
        prep_time: null,
        prep_guide: ""
      }
    };
  }
};
</script>

<style scoped>
</style>
