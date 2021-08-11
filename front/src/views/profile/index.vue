<template>
  <div class="app-container" >
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="Avatar">
        <el-upload
          action="#"
          :http-request="handleUpload"
          :on-change="handleChange"
          :file-list="fileList"
          :auto-upload="true">
          <el-image :src="form.avatarUrl" style="width: 100px; height: 100px" fit="cover" lazy></el-image>
          <el-button type="primary" icon="el-icon-edit" style="margin-left:10px" circle></el-button>
          <div slot="tip" class="el-upload__tip">jpg/png files with a size less than 500kb</div>
        </el-upload>
      </el-form-item>
      <el-form-item label="Name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="Email">
        <el-input v-model="form.email" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Update</el-button>
        <el-button @click="onCancel">Cancel</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>

import { UploadFile } from '@/api/utils'
import { GetCurrentUserInfo, UpdateCurrentUserInfo } from '@/api/user'

export default {
  data() {
    return {
      form: {
        name: '',
        email: '',
        avatarUrl: 'https://cdn.pixabay.com/photo/2016/11/18/23/38/child-1837375_960_720.png',
      },
      fileList: []
    }
  },
  created(){
    GetCurrentUserInfo().then(res => {
      this.form.name = res.full_name;
      this.form.email = res.email;
      this.form.avatarUrl = res.avatar
    })
  },
  methods: {
    onSubmit() {
      let requestBody = {
        full_name: this.form.name,
        email: this.form.email,
        avatar: this.form.avatarUrl
      }
      console.log(requestBody)
      UpdateCurrentUserInfo(requestBody).then(res => {
        this.$message('updated!')
      }).catch(err => {

        this.$message({
          message: err,
          type: 'warning'
        })
      })
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    },
    handleChange(file, fileList) {
      this.fileList = [file];
    },
    handleUpload(file){
      console.log(file)
      let formData = new FormData();
      formData.append('file', file.file);
      UploadFile(formData).then(res => {
        this.form.avatarUrl = res.url
      })
      return true
    }
  }
}
</script>

<style scoped>
.line{
  text-align: center;
}

.el-form {
  max-width: 460px;
}
</style>

