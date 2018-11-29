<template>
  <div>
    <el-row>
      <el-col :md="14"><br/></el-col>
      <el-col :md="6">
        <div class="noSide">
          <div class="title">
            <h3>登录</h3>
          </div>
          <el-form ref="loginForm" :rules="rules" :model="form" label-width="80px">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="form.username"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input v-model="form.password" type="password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-col>
                <el-button type="primary" @click="submitForm('loginForm')">登录</el-button>
              </el-col>
            </el-form-item>
            <el-row>
              <el-col :md="12"><br/></el-col>
              <el-col :md="6"><el-button round @click="alert('that\'s too bad')">忘记密码？</el-button></el-col>
              <el-col :md="6"><el-button round @click="goRegister()">注册</el-button></el-col>
            </el-row>
          </el-form>
        </div>
      </el-col>
    </el-row>
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
    padding-right: 5%;
    padding-bottom: 5%;
    padding-top: 2%;
    border: 1px #b192e6 solid;
    border-radius: 3%;
    background-color: white;
    box-shadow: 4px 4px 4px  rgba(90, 18, 166, 0.35);
  }
</style>

<script>
export default {
  data() {
    return {
      form: {
        username: '',
        password: '',
        remember: false
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
            // console.log(this.$data.form);
            this.$http.post('/userlogin/', this.$data.form)
            .then(response => {
              console.log(response);
              if (response.data.status !== "ok") {
                this.$alert('用户名或密码错误', '登录失败', {
                  confirmButtonText: '确定',
                  callback: action => {
                    this.$router.go(0);
                  }
                });
              } else {
                this.$emit('change', this.form.username);
                this.$alert('即将返回原页面', '登录成功', {
                  confirmButtonText: '确定',
                  callback: action => {
                    this.$router.go(-1);
                  }
                });
              }
            })
            .catch(error => {
              console.log(error);
            });
          } else {
            console.log('error submit!!');
            return false;
          }
        });
    },
    goRegister() {
      this.$router.push('/register');
    }
  }
}
</script>
