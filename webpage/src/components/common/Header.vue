<template>
  <div class="header">
    <el-row>
      <el-col :md="5" :xs="24" :sm="24">
        <div class="logo">
          <img :src="logo" height="40" style="margin-top: 4%;">
        </div>
      </el-col>
      <el-col :md="13"><br/></el-col>
      <el-col :md="3" :xs="20" :sm="20">
        <div class="user-info" style="float: right">
          <el-dropdown trigger="click" @command="handleCommand">
                <span class="el-dropdown-link">
                  <img class="user-logo" :src="imgUrl">
                </span>
            <el-dropdown-menu slot="dropdown" v-if="username !== ''">
              <el-dropdown-item command="goInfo">{{ username }}</el-dropdown-item>
              <el-dropdown-item command="goLogout">退出</el-dropdown-item>
            </el-dropdown-menu>
             <el-dropdown-menu slot="dropdown" v-if="username === ''">
              <el-dropdown-item command="goLogin">登录</el-dropdown-item>
              <el-dropdown-item command="goRegister">注册</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-col>
    </el-row>
    <div class="hidden-md-and-up"><hr></div>
  </div>
</template>

<style scoped>
  .header {
    position: relative;
    box-sizing: border-box;
    width: 100%;
    font-size: 22px;
    /*line-height: 70px;*/
    color: #fff;
  }

  .header .logo {
    float: left;
    width: 250px;
    text-align: center;
  }

  .user-info {
    /*float: right;*/
    /*padding-right: 50px;*/
    font-size: 16px;
    color: #fff;
  }

  .user-info .el-dropdown-link {
    position: relative;
    display: inline-block;
    /*padding-left: 50px;*/
    /*color: #4758ff;*/
    color: white;
    cursor: pointer;
    vertical-align: middle;
  }

  .user-info .user-logo {
    /*position: absolute;*/
    /*left: 0;*/
    /*top: 10px;*/
    padding-top: 10px;
    width: 50px;
    height: 50px;

  }

  .user-info .user-name {
    position: relative;
    /*margin-left: 7px;*/
  }

  .el-dropdown-menu__item {
    text-align: center;
  }

</style>

<script>
export default {
  name: 'Header',
  props: ['username'],
  data() {
    return {
      imgUrl: '/static/img/avatar.png',
      logo: '/static/img/logo.png',
    }
  },
  mounted() {
  },
  updated() {
  },
  methods: {
    handleCommand(command) {
      if (command === 'goLogin') {
        this.goLogin();
      } else if (command === 'goInfo') {
        this.goInfo();
      } else if (command === 'goRegister') {
        this.goRegister();
      } else {
        this.goLogout();
      }
    },
    goLogin() {
      this.$router.push('/login');
    },
    goRegister() {
      this.$router.push('/register');
    },
    goInfo() {
      this.$router.push('/info');
    },
    goLogout() {
      this.$http.get('/userlogout/')
      .then(response => {
        if (response.data.status === "ok") {
          this.$emit('change','');
          this.$router.go(0);
        } else {
          this.$alert('请重试', '退出失败', {
            confirmButtonText: '确定'
          });
        }
      })
    }
  },
}
</script>
