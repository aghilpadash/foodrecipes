<template>
  <main class="container my-5">
    <div class="row justify-content-between">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
      </div>
      <div class="col-md-5">
        <img v-if="!preview" class="img-fluid"
             style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);" :src="recipe.picture" alt="">
        <img v-else class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
             :src="preview" alt="">

      </div>
      <div class="col-md-5">
        <form @submit.prevent="submitRecipe">
          <div class="form-group text-right">
            <label for>نام دستور</label>
            <input type="text" class="form-control" v-model="recipe.name">
          </div>
          <div class="form-group text-right">
            <label for>مواد اولیه</label>
            <input v-model="recipe.ingredients" type="text" class="form-control">
          </div>
          <div class="form-group text-right">
            <label class="text-right" for>تصویر غذا</label>
            <input type="file" name="file" @change="onFileChange">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group text-right">
                <label for>درجه سختی</label>
                <select v-model="recipe.difficulty" class="form-control">
                  <option value="E">آسان</option>
                  <option value="M">متوسط</option>
                  <option value="H">سخت</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group text-right">
                <label for>
                  زمان آماده شدن
                  <small>(دقیقه)</small>
                </label>
                <input v-model="recipe.prep_time" type="number" class="form-control">
              </div>
            </div>
          </div>
          <div class="form-group mb-3 text-right">
            <label for>دستور پخت</label>
            <textarea v-model="recipe.prep_guide" class="form-control" rows="8"></textarea>
          </div>
          <input type="hidden" v-model="recipe.created_at">
          <button type="submit" class="btn btn-primary">ثبت</button>
        </form>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "ویرایش دستور پخت"
    }
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
      },
      preview: ""
    };
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.recipe.picture = files[0]
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitRecipe() {
      let editedRecipe = this.recipe
      if (editedRecipe.picture.name.indexOf("http://") !== -1) {
        delete editedRecipe["picture"]
      }
      const config = {
        headers: {"content-type": "multipart/form-data"}
      };
      let formData = new FormData();
      for (let data in editedRecipe) {
        formData.append(data, editedRecipe[data]);
      }
      try {
        let response = await this.$axios.$patch(`/recipes/${editedRecipe.id}/`, formData, config);
        this.$router.push("/recipes/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>
