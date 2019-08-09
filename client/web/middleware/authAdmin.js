export default async function({ app, store, $axios, redirect }) {
  if (!store.state.adminToken) {
    return redirect(301, "/admin/login")
  }
  try {
    await $axios.post("/api/admin/auth/auth")
  } catch (err) {
    app.$cookies.remove("auth.admin")
    return redirect(301, "/admin/login")
  }
}
