<template>
  <div class="admin--wrapper">
    <div class="side--menu">
      <Sidebar />
    </div>
    <div class="main--content">
      <div class="g--nav">
        ナビ
      </div>
      <nuxt />
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
</style>
<style lang="scss" scoped>
.admin--wrapper {
  .side--menu {
    position: fixed;
    width: 240px;
  }
  .main--content {
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
  }
}
</style>
