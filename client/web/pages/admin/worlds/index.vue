<template>
  <div>
    <PageHeader>Worlds</PageHeader>
    <div>
      <div style="margin-bottom: 15px;">
        <nuxt-link :to="{ path: `/admin/worlds/new` }"><i class="fa fa-plus"></i> ワールドを追加する</nuxt-link>
      </div>
      <Box>
        <table class="table is-dark is-fullwidth">
          <thead>
            <tr>
              <th style="width: 60px;"></th>
              <th style="width: 40px;">ID</th>
              <th>ワールド名</th>
              <th>ログイン数</th>
              <th>ワールド説明</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="world of worlds" :key="`world-${world.id}`">
              <td><nuxt-link :to="{ path: `/admin/worlds/${world.id}` }">編集</nuxt-link></td>
              <td>{{ world.id }}</td>
              <td>{{ world.name }}</td>
              <td>{{ world.login_count }}</td>
              <td>{{ world.description }}</td>
            </tr>
          </tbody>
        </table>
      </Box>
    </div>
  </div>
</template>
<script>
import PageHeader from "~/components/admin/molecules/PageHeader/PageHeader"
import Box from "~/components/admin/molecules/Box/Box"
export default {
  layout: "admin",
  components: { PageHeader, Box },
  async asyncData({ app }) {
    try {
      const { worlds } = await app.$axios.$get(`http://localhost:5000/api/admin/worlds`)
      return {
        worlds: worlds,
      }
    } catch (err) {
      console.log(err)
    }
  },
}
</script>
<style lang="scss" scoped>
.table {
  background: transparent;
  thead {
    th,
    td {
      color: #96989c;
    }
    th {
      border-color: rgba(0, 0, 0, 0.2);
    }
  }
  tbody {
    td {
      color: #96989c;
      border-color: rgba(0, 0, 0, 0.2);
    }
  }
}
</style>
