<template>
  <div>
    <PageHeader>Messages</PageHeader>
    <div class="columns">
      <div class="column is-3">
        <Box class="summary-box">
          <div><nuxt-link :to="{ path: './messages/new' }">メッセージを追加する</nuxt-link></div>
        </Box>
      </div>
    </div>
  </div>
</template>
<script>
import PageHeader from "~/components/admin/molecules/PageHeader/PageHeader"
import Box from "~/components/admin/molecules/Box/Box"
export default {
  layout: "admin",
  components: { PageHeader, Box },
}
</script>
<style lang="scss" scoped>
.summary-box {
  b {
    font-size: 24px;
    display: inline-block;
    margin-right: 5px;
  }
}
</style>
