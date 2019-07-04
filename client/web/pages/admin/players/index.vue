<template>
  <div>
    <PageHeader>Players</PageHeader>
    <div class="columns">
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>32</b>users</div>
          <div>今週のログイン</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>64</b>users</div>
          <div>今月のログイン</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>64</b>users</div>
          <div>TotalUsers</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>64</b>users</div>
          <div>直帰Users</div>
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
