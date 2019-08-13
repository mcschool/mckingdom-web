<template>
  <div class="footer">
    <div class="container">
      <div>
        <nuxt-link :to="{ path: `/admin` }">管理者</nuxt-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.footer {
  background: #383838;
  color: #ddd;
}
</style>
