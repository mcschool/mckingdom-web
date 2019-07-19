<template>
  <div>
    <PageHeader>PVP</PageHeader>
    <div class="columns">
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>64</b>courses</div>
          <div>コース数</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>32</b>completed</div>
          <div>総クリア数</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>23d 23:00:00</b></div>
          <div>TotalTime</div>
        </Box>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <section>
          <div>Total Kills</div>
        </section>
      </div>
      <div class="column">
        <section>
          <div>Kill Streaks</div>
        </section>
      </div>
    </div>
  </div>
</template>
<script>
import Box from "~/components/admin/molecules/Box/Box"
import PageHeader from "~/components/admin/molecules/PageHeader/PageHeader"
export default {
  layout: "admin",
  components: { PageHeader, Box },
}
</script>
<style lang="scss" scoped></style>
