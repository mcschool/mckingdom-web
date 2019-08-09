<template>
  <div class="login-container admin">
    <div class="prev">
      <nuxt-link :to="{ path: '/' }"><i class="fa fa-arrow-left"></i> 戻る</nuxt-link>
    </div>
    <form @submit.prevent="login" class="form">
      <div class="field">
        <label class="label">LoginID</label>
        <input class="input" v-model="loginId" />
      </div>
      <div class="field">
        <label class="label">Password</label>
        <input class="input" v-model="password" />
      </div>
      <br />
      <div class="field">
        <button class="button is-primary is-outlined">ログイン</button>
      </div>
    </form>
  </div>
</template>
<script>
export default {
  layout: "admin_login",
  data() {
    return {
      loginId: "",
      password: "",
    }
  },
  head() {
    return {
      title: "管理者ログイン",
    }
  },
  fetch({ store, redirect }) {
    if (store.state.adminToken) {
      redirect("/admin")
    }
  },
  methods: {
    async login() {
      try {
        const res = await this.$axios.$post(`/api/admin/auth/login`, {
          loginId: this.loginId,
          password: this.password,
        })
        this.$cookies.set("auth.admin", res.token)
        window.location.href = "/admin"
      } catch (err) {
        console.log(err)
      }
    },
  },
}
</script>
<style lang="scss" scoped>
.login-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  .prev {
    position: fixed;
    left: 30px;
    top: 30px;
    a {
      color: #a5a8ad;
    }
  }
  .form {
    width: 320px;
    .label {
      color: #a5a8ad;
    }
  }
}
</style>
