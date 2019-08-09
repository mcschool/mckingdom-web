<template>
  <div class="admin--wrapper">
    <div class="side--menu">
      <Sidebar />
    </div>
    <div class="main--container">
      <div class="g--nav">
        <div class="left">
          ナビ
        </div>
        <div class="right">
          <a @click="logout">ログアウト</a>
        </div>
      </div>
      <div class="main--content">
        <nuxt />
      </div>
    </div>
  </div>
</template>
<script>
import Sidebar from "~/components/admin/organisms/Sidebar/Sidebar"
export default {
  middleware: "authAdmin",
  components: { Sidebar },
  methods: {
    logout() {
      if (window.confirm("ログアウトしますか？")) {
        this.$cookies.remove("auth.admin")
        window.location.href = ""
      }
    },
  },
}
</script>
<style lang="scss">
.admin--wrapper {
  height: 100%;
  background: #212529;
  color: #a4a8ae;
  min-height: 100vh;
}
a {
  color: #a4a8ae;
}
a:hover {
  color: #b4b8be;
}
.admin--wrapper {
  .side--menu {
    position: fixed;
    width: 240px;
  }
  .main--container {
    padding-left: 250px;
    height: 200vh;
    padding-top: 50px;
    .g--nav {
      position: fixed;
      top: 0;
      display: flex;
      background: #212529;
      width: calc(100% - 255px);
      border-bottom: solid 1px #333;
      padding: 15px;
      .left {
        flex: 1;
      }
      .right {
        flex: 1;
        text-align: right;
      }
    }
    .main--content {
      padding: 10px 15px;
    }
  }
}
</style>
