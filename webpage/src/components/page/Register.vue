<template>
  <div class="noSide register">
    <div class="title">
      <h3>注册</h3>
    </div>
    <el-form ref="registerForm" :rules="rules" :model="form" label-width="80px">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="form.password" type="password"></el-input>
      </el-form-item>
      <el-form-item label="重复密码" prop="checkPass">
        <el-input v-model="form.checkPass" type="password"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item>
        <el-col :md="10" :push="2">
          <el-button type="primary" @click="submitForm('registerForm')">注册</pre></el-button>
        </el-col>
        <el-col :md="10" :push="2">
          <el-button type="danger" @click="resetForm('registerForm')">重置</pre></el-button>
        </el-col>
      </el-form-item>
    </el-form>
  </div>
</template>

<style scoped>
  .title {
    /*top:50%;*/
    /*width:100%;*/
    /*margin-top: -230px;*/
    margin-bottom: 10%;
    text-align: center;
    font-size: 30px;
    color: rgb(72, 106, 106);
  }

  .noSide {
    margin: auto;
    margin-top: 5%;
    padding: 1%;
    padding-right: 2%;
    border: 1px #b192e6 solid;
    border-radius: 3%;
    background-color: white;
    box-shadow: 4px 4px 4px rgba(90, 18, 166, 0.35);
  }

  .register {
    width: 30%;
  }
</style>

<script>
  
  export default {
    data() {
      var validatePass2 = (rule, value, callback) => {
        if (value !== this.form.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };

      var validateEmail = (rule, value, callback) => {
        if (!/^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$/.test(value)) {
          callback(new Error('邮箱格式有误'));
        } else {
          callback();
        }
      };
      return {
        form: {
          is_active: true,
          username: '',
          password: '',
          checkPass: '',
          email: ''
        },
        rules: {
          username: [
            { required: true, message: '请输入用户名', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '请输入密码', trigger: 'blur' },
            { min: 6, max: 16, message: '长度应在 6 到 18 个字符', trigger: 'blur' }
          ],
          checkPass: [
            { required: true, message: '请再次输入密码', trigger: 'blur' },
            { validator: validatePass2, trigger: 'blur' }
          ],
          email: [
            { required: true, message: '请输入邮箱', trigger: 'blur' },
            { validator: validateEmail, trigger: 'blur' }
          ]
        }
      }
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$http.post('/api/users/', this.$data.form)
              .then(response => {
                if (response.status == "201") {
                  this.$alert('即将进入首页', '注册成功', {
                    confirmButtonText: '确定',
                    callback: action => {
                      this.$router.push('/index');
                    }
                  });
                } else {
                  this.$alert('发生错误', '注册失败', {
                    confirmButtonText: '确定'
                  });
                }
              })
              .catch(error => {
                console.log(error);
              });
          } else {
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>
