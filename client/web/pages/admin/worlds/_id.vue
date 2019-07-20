<template>
  <div>
    <PageHeader>{{ world.name }}</PageHeader>
    <div class="columns">
      <div class="column is-6">
        <Box>
          <form @submit.prevent="update" class="form">
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
  async asyncData({ app, params }) {
    const worldId = params.id
    try {
      const { world } = await app.$axios.$get(`http://localhost:5000/api/admin/worlds/${worldId}`)
      const newWorld = Object.assign({}, world)
      return {
        world: world,
        newWorld: newWorld,
      }
    } catch (err) {
      console.log(err)
    }
  },
  methods: {
    update() {
      console.log(this.newWorld)
      const worldId = this.newWorld.id
      try {
        this.$axios.put(`http://localhost:5000/api/admin/worlds/${worldId}`, this.newWorld)
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
