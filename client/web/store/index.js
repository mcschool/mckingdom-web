export const state = () => ({
  adminToken: "",
})

export const mutations = {
  setAdminToken(state, token) {
    state.adminToken = token
  },
}

export const actions = {
  nuxtServerInit({ commit }) {
    const authAdmin = this.$cookies.get("auth.admin")
    if (authAdmin) {
      commit("setAdminToken", authAdmin)
    }
  },
}
