<template>
  <div class="side-menu">
    <div class="brand">MC KINGDOM</div>
    <div class="menu">
      <h3>Main</h3>
      <ul>
        <li :class="{ active: this.$route.path === '/admin' }"><nuxt-link :to="{ path: '/admin' }">Dashboard</nuxt-link></li>
        <li :class="{ active: this.$route.path.match(/\/admin\/players/) }"><nuxt-link :to="{ path: '/admin/players' }">プレーヤー</nuxt-link></li>
        <li :class="{ active: this.$route.path.match(/\/admin\/login\/histories/) }"><nuxt-link :to="{ path: '/admin/login/histories' }">ログイン履歴</nuxt-link></li>
        <li :class="{ active: this.$route.path.match(/\/admin\/topics/) }"><nuxt-link :to="{ path: '/admin/topics' }">お知らせ</nuxt-link></li>
        <li :class="{ active: this.$route.path.match(/\/admin\/messages/) }"><nuxt-link :to="{ path: '/admin/messages' }">メッセージ</nuxt-link></li>
        <li :class="{ active: this.$route.path.match(/\/admin\/worlds/) }"><nuxt-link :to="{ path: '/admin/worlds' }">ワールド</nuxt-link></li>
        <li :class="{ active: this.$route.path.match(/\/admin\/settings/) }"><nuxt-link :to="{ path: '/admin/settings' }">設定</nuxt-link></li>
      </ul>
      <h3>Games</h3>
      <ul>
        <li :class="{ active: this.$route.path.match(/\/admin\/games\/athletic/) }"><nuxt-link :to="{ path: '/admin/games/athletic' }">アスレ</nuxt-link></li>
        <li :class="{ active: this.$route.path.match(/\/admin\/games\/pvp/) }"><nuxt-link :to="{ path: '/admin/games/pvp' }">PVP</nuxt-link></li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.side-menu {
  display: flex;
  flex-direction: column;
  height: 100vh;
  .brand {
    height: 46px;
    font-weight: 700;
    padding: 10px;
    border-bottom: solid 1px #333;
  }
  .menu {
    flex: 1;
    height: 100%;
    overflow-y: auto;
    padding: 20px;
    h3 {
      font-size: 12px;
      color: rgba(255, 255, 255, 0.4);
    }
    ul {
      margin-bottom: 10px;
      li {
        a {
          position: relative;
          display: block;
          padding: 10px 10px 10px 24px;
          color: #96989c;
          transition: all 0.4s ease;
          &:hover {
            color: #e25985;
          }
          &:before {
            content: "";
            position: absolute;
            left: 0;
            top: 22px;
            display: block;
            width: 12px;
            border-bottom: solid 1px #96989c;
            transition: all 0.4s ease;
          }
          &:hover:before {
            width: 18px;
            border-color: #e25985;
          }
        }
        &.active a {
          color: #e25985;
          font-weight: bold;
          &:before {
            width: 18px;
            border-color: #e25985;
          }
        }
      }
    }
  }
}
</style>
