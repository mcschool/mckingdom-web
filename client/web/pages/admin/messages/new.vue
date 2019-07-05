<template>
  <div>
    <PageHeader>Create Message</PageHeader>
    <div class="columns">
      <div class="column is-6">
        <Box class="summary-box">
          <form @submit.prevent="submit">
            <div class="field">
              <label class="label" style="color: #fff;">ワールド</label>
              <div class="control">
                <input type="text" class="input" v-model="world" />
              </div>
            </div>
            <div class="field">
              <label class="label" style="color: #fff;">メッセージ</label>
              <div class="control">
                <input type="text" class="input" v-model="message" />
              </div>
            </div>
            <br />
            <div class="field">
              <button class="button">送信</button>
            </div>
          </form>
        </Box>
      </div>
    </div>
  </div>
</template>
<script>
import PageHeader from "~/components/admin/molecules/PageHeader/PageHeader"
import Box from "~/components/admin/molecules/Box/Box"
export default {
  layout: "admin",
  components: { PageHeader, Box },
  data() {
    return {
      world: "lobby",
      message: "メッセージ",
    }
  },
  methods: {
    async submit() {
      try {
        const response = await this.$axios.$post("http://localhost:5000/api/admin/messages", {
          world: this.world,
          message: this.message,
        })
        console.log("response", response)
      } catch (err) {
        console.log(err)
      }
    },
  },
}
</script>
<style lang="scss" scoped></style>
