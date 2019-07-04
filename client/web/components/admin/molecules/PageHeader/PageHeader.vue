<template>
  <div class="page--header">
    <h1><slot /></h1>
    <ul class="bread">
      <li><i class="fa fa-th-large" /></li>
      <li><slot /></li>
    </ul>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.page--header {
  margin-bottom: 15px;
}
h1 {
  font-size: 20px;
  margin-bottom: 5px;
  font-weight: 700;
}
.bread {
  display: flex;
  li {
    &:after {
      content: "/";
      padding: 0 10px;
      font-size: 12px;
      position: relative;
      top: -2px;
    }
    &:last-child:after {
      content: "";
    }
  }
}
</style>
