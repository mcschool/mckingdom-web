const pkg = require('./package')
const environment = process.env.NODE_ENV || "development"
const env = require(`./env.${environment}.js`)

console.log(env)

module.exports = {
  mode: 'universal',
  env: env,
  head: {
    htmlAttrs: {
      prefix: 'og: http://ogp.me/ns#'
    },
    titleTemplate: '%s - MCKINGDOM',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'MCKINGDOMはマインクラフトのマルチサーバーです。バージョンはある程度なんでもいけるはずです。MCはマインクラフトのMCではありません。' },
      { hid: 'og:site_name', property: 'og:site_name', content: 'MCKINGDOM' },
      { hid: 'og:type', property: 'og:type', content: 'website' },
      { hid: 'og:url', property: 'og:url', content: 'https://mc-kingdom.com' },
      { hid: 'og:title', property: 'og:title', content: 'MCKINGDOM' },
      { hid: 'og:description', property: 'og:description', content: 'MCKINGDOMはマインクラフトのマルチサーバーです。バージョンはある程度なんでもいけるはずです。MCはマインクラフトのMCではありません。' },
      { hid: 'og:image', property: 'og:image', content: 'https://mc-kingdom.com/hero.png' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href: 'https://use.fontawesome.com/releases/v5.6.1/css/all.css'},
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Viga&display=swap' }
    ],
  },
  loading: { color: '#fff' },
  css: [{ src: "~assets/scss/main.scss", lang: "scss" }],
  plugins: [
    '~/plugins/axios.js',
  ],
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    // Doc:https://github.com/nuxt-community/modules/tree/master/packages/bulma
    // '@nuxtjs/bulma',
    '@nuxtjs/pwa',
    ['cookie-universal-nuxt', { parseJSON: false }],
  ],
  router: {
    middleware: ["https"],
  },
  axios: {
    baseURL: env.baseURL,
    browserBaseURL: env.browserBaseURL,
    requestIntercepter: (config, { store }) => {
      if (store.state.token) {
        config.headers.common["Authorization"] = `Bearer ${store.state.token}`
      }
      return config
    }
  },
  build: {
    postcss: {
      preset: {
        features: {
          customProperties: false,
        },
      },
    },
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        if(!config.module) return
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/,
        })
      }
    },
  },
}
