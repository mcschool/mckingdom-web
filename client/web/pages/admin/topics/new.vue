<template>
  <div>
    <PageHeader>Create Topics</PageHeader>
    <div class="columns">
      <div class="column is-4">
        <Box class="summary-box">
          <form @submit.prevent="submit">
            <div class="field">
              <label class="label" style="color: #fff;">タイトル</label>
              <div class="control">
                <input type="text" class="input" v-model="title" required />
              </div>
            </div>
            <div class="field">
              <label class="label" style="color: #fff;">内容</label>
              <div class="control">
                <input type="text" class="input" v-model="body" />
              </div>
            </div>
            <div class="field">
              <label class="label" style="color: #fff;">ImagePath</label>
              <div class="control">
                <input type="text" class="input" v-model="imagePath" />
              </div>
            </div>
            <div class="field">
              <label class="label" style="color: #fff;">ImagePath</label>
              <div class="select">
                <select v-model="isPublished">
                  <option value="false">下書き</option>
                  <option value="true">公開</option>
                </select>
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
      title: "",
      body: "",
      image_path: "",
      isPublished: false,
    }
  },
  methods: {
    async submit() {
      try {
        await this.$axios.post(`/api/admin/topics`, {
          title: this.title,
          body: this.body,
          imagePath: this.imagePath,
          is_published: Boolean(this.isPublished),
        })
        this.$router.push(`/admin/topics`)
      } catch (err) {
        console.log(err)
      }
    },
  },
}
</script>
<style lang="scss" scoped></style>
