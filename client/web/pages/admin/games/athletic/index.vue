<template>
  <div>
    <PageHeader>Athletic</PageHeader>
    <div class="columns">
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>64</b>courses</div>
          <div>コース数</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>32</b>completed</div>
          <div>総クリア数</div>
        </Box>
      </div>
      <div class="column is-3">
        <Box class="summary-box">
          <div><b>23d 23:00:00</b></div>
          <div>TotalTime</div>
        </Box>
      </div>
    </div>
    <section>
      <h3>
        コース
        <a @click="addModal.isOpen = !addModal.isOpen"><i class="fa fa-plus"></i> 新しいコースを追加</a>
      </h3>
      <Box>
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th style="width: 60px;">ID</th>
              <th style="width: 100px;">コースNo</th>
              <th>コース名</th>
              <th style="width: 80px;">難易度</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="course of courses" :key="`course-${course.id}`">
              <td>{{ course.id }}</td>
              <td>{{ course.course_no }}</td>
              <td>{{ course.name }}</td>
              <td>{{ course.difficulty }}</td>
            </tr>
          </tbody>
        </table>
      </Box>
    </section>
    <Modal v-if="addModal.isOpen" :close="closeAddModal" :callback="createCourse">
      <template #header>
        新しいコースを追加
      </template>
      <template #body>
        <form>
          <div class="field">
            <label class="label">コース名</label>
            <input type="text" class="input" v-model="newCourse.name" />
          </div>
          <div class="field">
            <label class="label">画像パス</label>
            <input type="text" class="input" v-model="newCourse.image_path" />
          </div>
          <div class="field">
            <label class="label">説明文</label>
            <textarea class="textarea" rows="4" v-model="newCourse.description"></textarea>
          </div>
          <div class="field">
            <label class="label">コースno</label>
            <input type="number" class="input" v-model="newCourse.courseNo" style="width: 100px;" />
          </div>
          <div class="field">
            <label class="label">Difficulty</label>
            <div class="select">
              <select v-model="newCourse.difficulty">
                <option v-for="difficulty in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" :key="`difficulty-${difficulty}`">
                  {{ difficulty }}
                </option>
              </select>
            </div>
          </div>
        </form>
      </template>
    </Modal>
  </div>
</template>
<script>
import PageHeader from "~/components/admin/molecules/PageHeader/PageHeader"
import Box from "~/components/admin/molecules/Box/Box"
import Modal from "~/components/admin/molecules/Modal/Modal"
export default {
  layout: "admin",
  components: { PageHeader, Box, Modal },
  data() {
    return {
      addModal: {
        isOpen: false,
      },
      newCourse: {
        name: null,
        description: null,
        image_path: null,
        courseNo: null,
        difficulty: 1,
      },
    }
  },
  async asyncData({ app }) {
    try {
      const { courses } = await app.$axios.$get(`/api/admin/athletic_courses`)
      console.log(courses)
      return {
        courses: courses,
      }
    } catch (err) {
      console.log(err)
    }
  },
  methods: {
    closeAddModal() {
      this.addModal.isOpen = false
    },
    async createCourse() {
      try {
        const data = await this.$axios.post("http://localhost:5000/api/admin/athletic_courses", {
          name: this.newCourse.name,
          description: this.newCourse.description,
          course_no: this.newCourse.courseNo,
          difficulty: this.newCourse.difficulty,
        })
        console.log(data)
      } catch (err) {
        console.log(err)
      }
      this.addModal.isOpen = false
    },
  },
}
</script>
<style lang="scss" scoped>
.table {
  background: transparent;
  thead {
    th,
    td {
      color: #96989c;
    }
    th {
      border-color: rgba(0, 0, 0, 0.2);
    }
  }
  tbody {
    td {
      color: #96989c;
      border-color: rgba(0, 0, 0, 0.2);
    }
  }
}
</style>
