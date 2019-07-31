<template>
  <div class="footer">
    <div class="container">
      <div>
        <nuxt-link :to="{ path: `/admin` }">コントロールパネル</nuxt-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.footer {
  margin-top: 30px;
  background: #383838;
  color: #ddd;
}
</style>
