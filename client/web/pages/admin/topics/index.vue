<template>
  <div>
    <PageHeader>Topics</PageHeader>
    <div class="columns">
      <div class="column is-3">
        <Box class="summary-box">
          <div><nuxt-link :to="{ path: './topics/new' }">お知らせを追加する</nuxt-link></div>
        </Box>
      </div>
    </div>
    <div>
      <Box>
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>ID</th>
              <th>タイトル</th>
              <th>公開</th>
              <th>公開日時</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="topic of topics" :key="`topic-${topic.id}`">
              <td>{{ topic.id }}</td>
              <td>{{ topic.title }}</td>
              <td>{{ topic.is_published }}</td>
              <td>{{ topic.published_at }}</td>
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
      const { topics } = await app.$axios.$get(`/api/admin/topics`)
      return {
        topics: topics,
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
