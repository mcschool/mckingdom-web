<template>
  <div class="side-menu">
    <div class="brand">MC KINGDOM</div>
    <div class="menu">
      <h3>Main</h3>
      <ul>
        <li>
          <nuxt-link :to="{ path: '/admin' }">Dashboard</nuxt-link>
        </li>
        <li>
          <nuxt-link :to="{ path: '/admin/players' }">Players</nuxt-link>
        </li>
        <li>
          <nuxt-link :to="{ path: '/admin/login/histories' }">LoginHistory</nuxt-link>
        </li>
        <li>
          <nuxt-link :to="{ path: '/admin/messages' }">Messages</nuxt-link>
        </li>
        <li>
          <nuxt-link :to="{ path: '/admin/settings' }">Settings</nuxt-link>
        </li>
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
      }
    }
  }
}
</style>
