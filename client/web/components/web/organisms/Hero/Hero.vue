<template>
  <div class="hero">
    <div class="image-wrapper">
      <div class="filter"></div>
      <div class="hero-contents">
        <div class="server-name">MCKINGDOM</div>
        <div class="server-address">mckd.me:80</div>
      </div>
      <img src="/hero.png" />
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.hero {
  padding: 30px;
  .image-wrapper {
    position: relative;
    .filter {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 10;
      background: rgba(0, 0, 0, 0.6);
    }
    .hero-contents {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 11;
      text-align: center;
      .server-name {
        font-size: 100px;
        color: #fff;
      }
      .server-address {
        font-size: 100px;
        color: #fff;
      }
    }
  }
}
</style>
