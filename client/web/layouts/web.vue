<template>
  <div class="web-wrap">
    <GlobalNav />
    <nuxt />
    <Footer />
  </div>
</template>
<script>
import GlobalNav from "~/components/web/organisms/GlobalNav/GlobalNav"
import Footer from "~/components/web/organisms/Footer/Footer"
export default {
  components: { GlobalNav, Footer },
}
</script>
<style>
*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}
.web-wrap {
  min-height: 100vh;
  background: #282828;
}
</style>
