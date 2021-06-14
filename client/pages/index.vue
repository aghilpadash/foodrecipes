<template>
  <header>
    <div class="text-box text-center">
      <h1>دوست داری غذای ایرانی بپزی؟</h1>
      <p class="mt-3">یه عالمه دستور پخت برات آماده کردیم ❤️</p>
      <nuxt-link class="btn btn-outline btn-large btn-info" to="/recipes">
        بزن بریم  <span class="ml-2">&larr;</span>
      </nuxt-link>
    </div>
  </header>
</template>

<script>
export default {
  head() {
    return {
      title: "دستور پخت غذاهای ایرانی | صفحه اصلی"
    };
  },
};
</script>

<style>
header {
  min-height: 100vh;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.9),
      rgba(0, 0, 0, 0.4)
    ),
    url("/images/food.jpg");
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 35%;
  width: 100%;
  text-align: center;
  font-size: 18px;
  color: #fff;
}
.text-box h1 {
  font-family: Shabnam,serif;
  font-size: 5rem;

}
.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>
