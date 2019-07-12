<template>
  <div class="modal admin is-active">
    <div @click="close" class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"><slot name="header">Modal</slot></p>
        <button class="delete" aria-label="close" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <slot name="body">content ...</slot>
      </section>
      <footer class="modal-card-foot">
        <slot name="footer">
          <button class="button is-success" @click="callback">Save changes</button>
          <button class="button" @click="close">Cancel</button>
        </slot>
      </footer>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    close: {
      type: Function,
      required: true,
    },
    callback: {
      type: Function,
      required: false,
    },
  },
}
</script>
<style lang="scss" scoped>
.modal-card {
  background: #282b2f;
  border-radius: 4px;
  .modal-card-head {
    background: transparent;
    border-bottom: solid 1px #2f3338;
    .modal-card-title {
      color: #a5a8ad;
      font-size: 18px;
      font-weight: bold;
    }
  }
  .modal-card-body {
    background: transparent;
    .label {
      color: #a5a8ad;
    }
  }
  .modal-card-foot {
    background: transparent;
    border-top: solid 1px #2f3338;
    text-align: right;
    justify-content: flex-end;
    .button {
      border-radius: 50px;
    }
  }
}
</style>
