<template>
  <div class="app-container" >
    <el-form ref="form" :rules="rules" :model="form" label-width="120px">
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
      <el-form-item label="Name" prop="name" required>
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="Email" prop="email" required>
        <el-input v-model="form.email" />
      </el-form-item>
      <el-form-item label="Password" prop="pass" required>
        <el-input type="password" v-model="form.pass" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Confirm" prop="checkPass" required>
        <el-input type="password" v-model="form.checkPass" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="Active">
        <el-switch
          v-model="form.is_active">
        </el-switch>
      </el-form-item>
      <el-form-item label="Super User">
        <el-switch
          v-model="form.is_superuser">
        </el-switch>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Add</el-button>
        <el-button @click="onCancel">Cancel</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>

import { UploadFile } from '@/api/utils'
import { AddUser } from '@/api/users'

export default {
  data() {
      let validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please input the password'));
        } else {
          if (this.form.checkPass !== '') {
            this.$refs.form.validateField('checkPass');
          }
          callback();
        }
      };
      let validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Please input the password again'));
        } else if (value !== this.form.pass) {
          callback(new Error('Two inputs don\'t match!'));
        } else {
          callback();
        }
      };
    return {
      form: {
        is_active: true,
        is_superuser: false,
        pass: '',
        checkPass: '',
        name: '',
        email: '',
        avatarUrl: 'https://cdn.pixabay.com/photo/2016/11/18/23/38/child-1837375_960_720.png',
      },
      rules: {
        name: [
          { required: true }
        ],
        email: [
          { required: true }
        ],
        pass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ]
      },
      fileList: []
    }
  },
  methods: {
    onSubmit() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          let requestBody = {
            full_name: this.form.name,
            email: this.form.email,
            avatar: this.form.avatarUrl,
            is_active: this.form.is_active,
            is_superuser: this.form.is_superuser,
            password: this.form.pass
          }
          console.log(requestBody)
          AddUser(requestBody).then(res => {
            this.$message('added!')
            this.$refs.form.resetFields()
          })
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm() {
      this.form = {
        is_active: false,
        is_superuser: false,
        pass: '',
        checkPass: '',
        name: '',
        email: '',
        avatarUrl: 'https://cdn.pixabay.com/photo/2016/11/18/23/38/child-1837375_960_720.png',
      }
    },
    onCancel() {
      this.resetForm()
      this.$refs.form.clearValidate()
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

