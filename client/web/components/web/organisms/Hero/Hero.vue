<template>
  <div class="hero">
    <div class="container">
      <div class="side-contents">
        <div class="brand">MC<br />KINGDOM</div>
        <div class="server-address">mckd.me:80</div>
        <div class="news">
          <div class="news-title">Topics</div>
          <ul class="news-list">
            <li v-for="topic of topics" :key="`topic-${topic.id}`">{{ dateFormat(topic.createdAt) }}: {{ topic.title }}</li>
          </ul>
        </div>
      </div>
      <div class="bg-image">
        <img src="/hero.png" />
      </div>
    </div>
  </div>
</template>
<script>
import moment from "moment"
export default {
  props: {
    topics: {
      type: Array,
      required: true,
    },
  },
  methods: {
    dateFormat(date) {
      const d = moment(date)
      return d.format("L")
    },
  },
}
</script>
<style lang="scss" scoped>
.hero {
  color: #fff;
  height: 660px;
  background: #000;
  .container {
    width: 100%;
    height: 100%;
    padding-top: 60px;
    .side-contents {
      position: relative;
      z-index: 10;
      .brand {
        font-family: "Viga", cursive;
        font-size: 100px;
        line-height: 1;
      }

      .server-address {
        font-family: "Viga", cursive;
        font-size: 60px;
        line-height: 1;
        margin-top: 20px;
        margin-bottom: 40px;
      }

      .news {
        .news-title {
          margin-bottom: 10px;
        }
      }
    }
    .bg-image {
      position: absolute;
      right: 0;
      bottom: 0px;
      padding: 50px 0 50px 460px;
      height: 100%;
      img {
        height: 100%;
        object-fit: cover;
        opacity: 0.3;
      }
    }
  }
}
</style>
