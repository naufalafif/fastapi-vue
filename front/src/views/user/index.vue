<template>
  <div class="app-container">

    <router-link to="/user/add">
      <el-button type="primary" style='margin-bottom:10px' round>
        <i class="el-icon-plus"></i>
        add new user
      </el-button>
    </router-link>
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.$index + 1 }}
        </template>
      </el-table-column>
      <el-table-column label="Email">
        <template slot-scope="scope">
          {{ scope.row.email }}
        </template>
      </el-table-column>
      <el-table-column label="Name">
        <template slot-scope="scope">
          <span>{{ scope.row.full_name }}</span>
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="Super User" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.is_superuser | statusIcon }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="Active" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.is_active | statusIcon }}
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="Avatar" width="200">
        <template slot-scope="scope">
          <el-image 
            style="width: 25px; height: 25px"
            :src="scope.row.avatar" >
          </el-image>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/users'

export default {
  filters: {
    statusIcon(status) {
      const statusMap = {
        true: '✅',
        false: '❌'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList().then(response => {
        this.list = response
        this.listLoading = false
      })
    }
  }
}
</script>
