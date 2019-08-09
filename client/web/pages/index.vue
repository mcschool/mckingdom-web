<template>
  <section>
    <Hero />
    <div class="summary">
      <div class="container">
        <h3>Summary 1.5</h3>
        <div class="columns">
          <div class="column is-2 is-offset-2">
            <div class="s-title">NOW</div>
            <div class="s-count">{{ nowPlayingPlayerCount }}</div>
          </div>
          <div class="column is-2">
            <div class="s-title">TOTAL</div>
            <div class="s-count">{{ totalPlayerCount }}</div>
          </div>
          <div class="column is-2">
            <div class="s-title">GAMES</div>
            <div class="s-count">10</div>
          </div>
          <div class="column is-2">
            <div class="s-title">MINI GAMES</div>
            <div class="s-count">20</div>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="container">
        <div style="text-align: center; font-size: 32px; margin-bottom: 10px;">ゲーム</div>
        <div class="columns">
          <div v-for="world in [0, 1, 2, 3]" :key="`world-${world}`" class="column">
            <div>
              <img src="https://i.gzn.jp/img/2019/05/09/minecraft-classic-10th-anniversary/00.jpg" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="container">
        <div>お知らせ</div>
      </div>
    </div>
  </section>
</template>

<script>
import Hero from "~/components/web/organisms/Hero/Hero"
export default {
  layout: "web",
  components: {
    Hero,
  },
  head() {
    return {
      titleTemplate: null,
      title: "MCKINGDOM - マインクラフトマルチサーバー",
    }
  },
  data() {
    return {
      nowPlayingPlayerCount: 1,
      totalPlayerCount: 2,
    }
  },
  async asyncData({ app }) {
    try {
      // const res1 = await app.$axios.get(`/api/web/players/loginStatus`)
      await app.$axios.get(`/api/health`)
      // console.log("res", res1)
      /*
      const nowPlayingPlayerCount = res1.now
      const res2 = await app.$axios.$get(`/api/web/players/all`)
      const totalPlayerCount = res2.players
      */
      return {
        nowPlayingPlayerCount: 1,
        totalPlayerCount: 2,
      }
    } catch (err) {
      console.log("err", err)
    }
  },
}
</script>

<style lang="scss" scoped>
.summary {
  text-align: center;
  color: #aaa;
  padding: 60px 0;
  h3 {
    font-family: "Viga", cursive;
    font-size: 48px;
    margin-bottom: 20px;
  }
  .s-title {
    font-family: "Viga", cursive;
    font-size: 24px;
  }
  .s-count {
    font-family: "Viga", cursive;
    font-size: 48px;
    color: #fff;
  }
}
</style>
