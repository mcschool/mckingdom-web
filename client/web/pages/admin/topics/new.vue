<template>
  <div>
    <PageHeader>Create Topics</PageHeader>
    <div class="columns">
      <div class="column is-3">
        <Box class="summary-box">
          <form></form>
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
<style lang="scss" scoped></style>
