<template>
  <div>
    input html here ...
    <button @click="methodA">ボタン</button>
  </div>
</template>
<script>
export default {
  data() {
    const data = {}
    return {
      data: data,
    }
  },
  mounted: function() {
    console.log()
  },
  methods: {
    methodA: function() {
      alert("ボタンがクリックされたよ")
    },
  },
}
</script>
<style lang="scss"></style>
