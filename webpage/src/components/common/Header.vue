<template>

  <div class="header">
    <el-row>
      <el-col :md="5" :xs="24" :sm="24">
        <div class="logo">
          <img :src="logo" height="40" style="margin-top: 4%;">
        </div>
      </el-col>
      <el-col :md="13">
        <br/>
      </el-col>
      <el-col :md="3" :xs="20" :sm="20">
        <div class="user-info" style="float: right">
          <el-dropdown trigger="click" @command="handleCommand">
                <span class="el-dropdown-link">
                  <img class="user-logo" :src="imgUrl">
                  <span class="user-name"> {{username}} </span>
                </span>
            <el-dropdown-menu slot="dropdown" v-if="isLogin === true">
              <el-dropdown-item command="goInfo">用户信息修改</el-dropdown-item>
              <el-dropdown-item command="goLogout">退出</el-dropdown-item>
            </el-dropdown-menu>
             <el-dropdown-menu slot="dropdown" v-if="isLogin === false">
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
    /*width: 100%;*/
    height: 40px;
    font-size: 22px;
    /*line-height: 70px;*/
    color: #fff;
  }

  .header .logo {
    float: left;
    width: 250px;
    text-align: center;
  }

  .navbar {
    margin-top: 10px;
    /*width: 900px;*/
    background: #2E363F;
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
    border-radius: 50%;

  }

  .user-info .user-name {
    position: relative;
    /*margin-left: 7px;*/
  }

  .el-dropdown-menu__item {
    text-align: center;
  }

  .is-disabled {
    cursor: not-allowed;
  }

</style>

<script>

  export default {
    data() {
      return {
        username: '',
        imgUrl: '',
        activeIndex: '',
        isLogin: false,
        logo: './././static/img/logo.png',
      }
    },
    created: function () {
      this.getInfo();
    },
    updated: function () {
      this.getInfo();
    },

    methods: {
      getInfo() {
        this.$http.get('/getUserInfo/')
          .then(response => {
            console.log(response);
            if (response.data.msg === "0") {
              console.log("get info success");
              this.username = response.data.username;
              this.imgUrl = response.data.imgUrl;
               this.isLogin = true;
            }
            else if (response.data.msg === "1") {
              console.log("unlogin");
              this.imgUrl = response.data.imgUrl;
              this.isLogin = false;
            }
            else {
              this.$alert('请刷新重试', '获取用户信息失败', {
                confirmButtonText: '确定'
              });
            }
          })
          .catch(error => {
            console.log(error);
          });
      },
      isGuest(num) {
        if (this.username === '') {
          if (num === 'search') {
            return false;
          }
          else {
            return true;
          }
        }
      },
      handleCommand(command) {
        if (command === 'goInfo') {
          this.goInfo();
        }
        else if (command === 'goLogout') {
          this.goLogout();
        }
      },
      goInfo() {
//        this.$router.replace("/info");
        location.assign("/#/info");
      },
      goLogout() {
        this.$http.get('/logout/')
          .then(response => {
            console.log(response);
            if (response.data.msg === "0") {
              this.$alert('即将返回首页', '退出成功', {
                confirmButtonText: '确定'
              });
              location.assign("/#/login");
            }
            else if (response.data.msg === "1") {
              this.$alert('请重试', '退出失败', {
                confirmButtonText: '确定'
              });

            }
          })
      }
    },
  }
</script>
