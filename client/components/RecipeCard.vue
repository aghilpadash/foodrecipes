<template>
  <div class="card recipe-card">
    <img :src="recipe.picture" class="card-img-top cover" alt="">
    <div class="card-body">
      <h5 class="card-title text-right">{{ recipe.name }}</h5>
      <p class="card-text text-right">
        <strong>درجه سختی:</strong> {{ recipe.difficulty }}
      </p>
      <p class="card-text text-right">
        <strong>زمان پخت:</strong> {{ recipe.prep_time }} دقیقه
      </p>
      <div class="action-buttons text-center">
        <nuxt-link :to="`/recipes/${recipe.id}/`" class="btn btn-sm btn-success">مشاهده</nuxt-link>
        <nuxt-link :to="`/recipes/${recipe.id}/edit/`" class="btn btn-sm btn-primary">ویرایش</nuxt-link>
        <button @click="onDelete(recipe.id)" class="btn btn-sm btn-danger">حذف</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["recipe", "onDelete"]
};
</script>

<style>
.recipe-card {
  box-shadow: 0 1rem 1.5rem rgba(0, 0, 0, .6);
}

img {
  width: 300px;
  height: 200px;
  object-fit: contain;
}
</style>
