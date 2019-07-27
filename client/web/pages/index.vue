<template>
  <section>
    <Hero />
    <div style="margin-bottom: 30px;">
      <div class="container" style="margin-bottom: 30px;">
        <div style="text-align: center;">＼ 今{{ nowPlayingPlayerCount }}人が遊んでいて、今までに{{ totalPlayerCount }}人が遊びました。 ／</div>
      </div>
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
      title: "MCKINGDOM - マインクラフトマルチサーバー",
    }
  },
  async asyncData({ app }) {
    try {
      const res1 = await app.$axios.$get(`/api/web/players/loginStatus`)
      const nowPlayingPlayerCount = res1.now
      const res2 = await app.$axios.$get(`/api/web/players/all`)
      const totalPlayerCount = res2.players
      return {
        nowPlayingPlayerCount: nowPlayingPlayerCount,
        totalPlayerCount: totalPlayerCount,
      }
    } catch (err) {
      console.log(err)
    }
  },
}
</script>

<style lang="scss" scoped></style>
