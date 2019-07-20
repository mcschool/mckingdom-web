<template>
  <div>
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
html {
  font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}
</style>
