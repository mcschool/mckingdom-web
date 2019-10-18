<template>
  <div>
    <PageHeader>Players</PageHeader>
    <div class="columns">
      <div class="column is-3">
        <Box class="summary-box">
          <div>
            <b>{{ thisWeekPlayerCount }}</b>
            users
          </div>
          <div>今週のログイン</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div>
            <b>{{ thisMonthPlayerCount }}</b>
            users
          </div>
          <div>今月のログイン</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div>
            <b>{{ totalPlayerCount }}</b>
            users
          </div>
          <div>TotalUsers</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div>
            <b>{{ bounceBackPlayerCount }}</b>
            users
          </div>
          <div>直帰Users</div>
        </Box>
      </div>
    </div>
    <div>
      <Box>
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>ID</th>
              <th>name</th>
              <th>UUID</th>
              <th>login</th>
              <th>最終ログイン</th>
              <th>初回アクセス</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="player of players" :key="`player-${player.id}`">
              <td>{{ player.id }}</td>
              <td>{{ player.name }}</td>
              <td>{{ player.uuid }}</td>
              <td>{{ player.login_count }}</td>
              <td>{{ dateFormat(player.last_login_at) }}</td>
              <td>{{ dateFormat(player.created_at) }}</td>
            </tr>
          </tbody>
        </table>
      </Box>
    </div>
  </div>
</template>
<script>
import moment from "moment"
import PageHeader from "~/components/admin/molecules/PageHeader/PageHeader"
import Box from "~/components/admin/molecules/Box/Box"
export default {
  layout: "admin",
  components: { PageHeader, Box },
  async asyncData({ app }) {
    try {
      const { players } = await app.$axios.$get(`/api/admin/players`)
      const data = await app.$axios.$get(`/api/admin/players/loginInfo`)
      console.log("pppp", data)
      return {
        players: players,
        totalPlayerCount: data.all,
        thisMonthPlayerCount: data.thisMonth,
        thisWeekPlayerCount: data.thisWeek,
        bounceBackPlayerCount: data.bounceBack,
      }
    } catch (err) {
      console.log(err)
    }
  },
  methods: {
    dateFormat: function(date) {
      const d = moment(date)
      d.add(-9, "hours")
      return d.format("YYYY-MM-DD HH:mm:ss")
    },
  },
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
