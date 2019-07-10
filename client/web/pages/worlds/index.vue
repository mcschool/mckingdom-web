<template>
  <div class="container">
    <h1 class="title is-1">ワールド一覧</h1>
    <h1 class="title is-2"><nuxt-link :to="{ path: '/worlds/athletic' }">アスレチック</nuxt-link></h1>
    <p>一般の方が作ったアスレなど、多くの種類のアスレがあります。難しさは色々!</p>
    <h1 class="title is-2"><nuxt-link :to="{ path: '/worlds/pvp' }">PVP</nuxt-link></h1>
    <p>ひたすらプレイヤー同士で戦おう！PVPのトップに立つのは誰なのか...</p>
  </div>
</template>
<script>
export default {
  data() {
    const data = {}
    return {
      data: data,
    }
  },
  mounted: function() {
    console.log("mounted")
  },
  methods: {
    methodA: function() {
      alert("ボタンがクリックされたよ")
    },
  },
}
</script>
<style lang="scss" scoped>
.is-2 {
  margin-bottom: 0px;
  cursor: pointer;
  &:hover {
    color: cornflowerblue;
  }
}
p {
  margin-bottom: 30px;
}
</style>
