<template>
  <div>
    <PageHeader>ワールドデータ作成</PageHeader>
    <div class="columns">
      <div class="column is-6">
        <Box>
          <form @submit.prevent="submit" class="form">
            <div class="field">
              <label class="label">name <span style="color: red;">*</span></label>
              <input type="text" class="input" v-model="newWorld.name" />
            </div>
            <div class="field">
              <label class="label">description</label>
              <textarea class="textarea" v-model="newWorld.description"></textarea>
            </div>
            <div class="field">
              <label class="label">image path</label>
              <input type="text" class="input" v-model="newWorld.image_path" />
            </div>
            <br />
            <div class="field">
              <button class="button is-primary">保存</button>
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
    const newWorld = {
      name: null,
      description: null,
      image_path: null,
    }
    return {
      newWorld: newWorld,
    }
  },
  methods: {
    async submit() {
      try {
        const data = await this.$axios.post(`http://localhost:5000/api/admin/worlds`, this.newWorld)
        console.log(data)
        alert("追加しました")
        this.$router.push("/admin/worlds")
      } catch (err) {
        console.log(err)
      }
    },
  },
}
</script>
<style lang="scss" scoped>
.form {
  .label {
    color: #96989c;
  }
}
</style>
