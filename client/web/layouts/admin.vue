<template>
  <div class="admin--wrapper">
    <div class="side--menu">
      <Sidebar />
    </div>
    <div class="main--container">
      <div class="g--nav">
        ナビ
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
  components: { Sidebar },
}
</script>
<style>
html {
  height: 100%;
  background: #212529;
}
body {
  background: #212529;
  height: 100vh;
  color: #a4a8ae;
}
a {
  color: #a4a8ae;
}
a:hover {
  color: #b4b8be;
}
</style>
<style lang="scss" scoped>
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
      background: #212529;
      width: 100%;
      border-bottom: solid 1px #333;
      padding: 10px;
    }
    .main--content {
      padding: 10px 15px;
    }
  }
}
</style>
