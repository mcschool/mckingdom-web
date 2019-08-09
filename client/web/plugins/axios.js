export default function({ $axios, store }) {
  $axios.onRequest(config => {
    if (store.state.adminToken) {
      config.headers.common["X-Admin-Token"] = `${store.state.adminToken}` //eslint-disable-line
    }
    return config
  })
}
