<template>
  <div class="container">
    <h1 class="title is-1">McKingDomServer</h1>
    <h2 class="title is-2">Welcome to McKingDomServer's page</h2>
    <h3 @click="methodA" class="title is-4">Discordについて</h3>
    <p v-if="discord">McKingDomサーバーには専用のDiscordサーバーがあります。入るか入らないかは任意です。入りたい場合は下のURLをクリックしてください。</p>
    <h3 @click="methodA" class="title is-4">主な内容 ~アスレ編~</h3>
    <p v-if="athletic">約20個のアスレがあるワールドでは、一般のお客様が作ってくれたアスレがたくさんあります。ぜひ挑戦してみてください。</p>
    <h3 @click="methodA" class="title is-4">サーバー全体の方針??</h3>
    <p v-if="policy">McKingDomサーバーでは、来てくれた方々との交流を大切にして、一般の方目線で運営をしています。今後の発展にご協力お願いいたします。</p>
  </div>
</template>
<script>
export default {
  data() {
    const data = {}
    return {
      data: data,
      discord: false,
      athletic: false,
      policy: false,
    }
  },
  mounted: function() {
    console.log("mounted")
  },
  methods: {
    methodA: function() {
      if (this.discord === false) {
        this.discord = true
        this.athletic = true
        this.policy = true
      } else {
        this.discord = false
        this.athletic = false
        this.policy = false
      }
    },
  },
}
</script>
<style lang="scss" scoped>
.is-4 {
  margin-bottom: 0px;
  cursor: pointer;
  &:hover {
    color: cornflowerblue;
  }
}
p {
  margin-bottom: 30px;
  color: black;
}
</style>
