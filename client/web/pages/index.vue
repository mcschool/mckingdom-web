<template>
  <section>
    <Hero :topics="topics" />
    <div class="summary">
      <div class="container">
        <h3>Summary</h3>
        <div class="columns">
          <div class="column is-2 is-offset-2">
            <div class="s-title">NOW</div>
            <div class="s-count">--</div>
          </div>
          <div class="column is-2">
            <div class="s-title">TOTAL</div>
            <div class="s-count">{{ totalPlayerCount }}</div>
          </div>
          <div class="column is-2">
            <div class="s-title">GAMES</div>
            <div class="s-count">--</div>
          </div>
          <div class="column is-2">
            <div class="s-title">MINI GAMES</div>
            <div class="s-count">--</div>
          </div>
        </div>
      </div>
    </div>
    <div class="games">
      <div class="container">
        <h3>Games</h3>
        <div class="columns game">
          <div class="column is-2"></div>
          <div class="column is-3">
            <img src="https://i.gzn.jp/img/2019/05/09/minecraft-classic-10th-anniversary/00.jpg" />
          </div>
          <div class="column is-5">
            <div class="game-title">アスレあります</div>
            <div class="game-description">総nコース(2019.08現在)。クリアランキング。難易度だいぶ高め。アスレ作りたい人募集中。</div>
            <div class="game-more">
              <nuxt-link :to="{ path: '/games/athletic' }" class="button is-primary is-outlined">くわしく <i class="fa fa-fw fa-arrow-right"></i></nuxt-link>
            </div>
          </div>
          <!--
          <div v-for="world in [0, 1, 2, 3]" :key="`world-${world}`" class="column is-3">
            <div>
              <img src="https://i.gzn.jp/img/2019/05/09/minecraft-classic-10th-anniversary/00.jpg" />
            </div>
          </div>
          -->
        </div>
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
      const data = await app.$axios.$get(`/api/web/pages/index`)
      return {
        topics: data.topics,
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
.games {
  background: #000;
  padding: 60px 0 90px;
  h3 {
    font-family: "Viga", cursive;
    font-size: 48px;
    margin-bottom: 20px;
    color: #aaa;
    text-align: center;
  }
  .game {
    .game-title {
      color: #eee;
      font-size: 32px;
      font-weight: bold;
    }
    .game-description {
      color: #aaa;
      font-size: 18px;
      margin: 10px 0 15px;
    }
    .button {
      background: transparent;
      &:hover {
        border-color: #eee;
        color: #eee;
      }
    }
  }
}
</style>
