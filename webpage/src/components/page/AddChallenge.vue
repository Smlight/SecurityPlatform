<template>
  <div class="noSide">
    <div class="title">
      <h3>添加ctf题目</h3>
    </div>
    <el-form ref="addchaForm" :rules="rules" :model="form" label-width="120px">
      <el-form-item label="题目名称" prop="title">
        <el-input type="text" v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="题目描述" prop="desc">
        <el-input type="textarea" rows="6" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item label="年份" prop="year">
        <el-input type="number" v-model.number="form.year"></el-input>
      </el-form-item>
      <el-form-item label="比赛名" prop="game">
        <el-input type="text" v-model="form.game"></el-input>
      </el-form-item>
      <el-form-item label="二进制文件" prop="filepath">
        <el-input type="file" v-model="form.filepath"></el-input>
      </el-form-item>
      <el-form-item label="分值" prop="points">
        <el-input type="number" v-model.number="form.points"></el-input>
      </el-form-item>
      <el-form-item label="docker仓库地址" prop="docker_repo">
        <el-input type="text" v-model="form.docker_repo"></el-input>
      </el-form-item>
      <el-form-item label="vagrant镜像地址" prop="vagrant_box">
        <el-input type="text" v-model="form.vagrant_box"></el-input>
      </el-form-item>
      <el-form-item label="利用代码" prop="poc">
        <el-input type="textarea" rows="6" v-model="form.poc"></el-input>
      </el-form-item>
      <el-form-item label="参考资料" prop="references">
        <el-input type="text" v-model="form.references"></el-input>
      </el-form-item>
      <el-form-item>
        <el-col :md="10" :push="2">
          <el-button type="primary" @click="submitForm('addchaForm')">添加</el-button>
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
  padding-right: 5%;
  padding-bottom: 5%;
  padding-top: 2%;
  border: 1px #b192e6 solid;
  border-radius: 3%;
  background-color: white;
  box-shadow: 4px 4px 4px rgba(90, 18, 166, 0.35);
  width: 80%;
}
.form-area {
  width: 99.5%;
  height: 160px;
}
</style>

<script>
import axios from 'axios'
import getCookie from '@/main'

export default {
  data() {
    return {
      form: {
        title: '',
        desc: '',
        year: '',
        game: '',
        filepath: null,
        points: null,
        docker_repo: '',
        vagrant_box: '',
        poc: '',
        references: ''
      },
      rules: {
        title: [
        { required: true, message: '请输入题目名称', trigger: 'change' }
        ],
        desc: [
        { required: true, message: '请输入题目描述', trigger: 'change' }
        ],
        year: [
        { type: 'number', min: 1700, max: 2018, message: '请输入合理的年份', trigger: 'change' }
        ],
        game: [
        ],
        filepath: [
        { required: true, message: '请上传二进制文件', trigger: 'change' }
        ],
        points: [
        { type: 'number', message: '请输入合理的分数', trigger: 'change' }
        ],
        docker_repo: [
        ],
        vagrant_box: [
        ],
        poc: [
        ],
        references: [
        ]
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
            var fileElement = this.$refs[formName].$el[4];//sorry for the hardcode
            axios({
              url: '/api/challenges/',
              method: 'post',
              data: this.$data.form,
              transformRequest: [function (data) {
                var formData = new FormData();
                for (var i in data) formData.append(i, data[i]);
                  formData.append('file', fileElement.files[0]);
                for(var pair of formData.entries()) {
                 console.log(pair[0]+ ': '+ pair[1]); 
               }
               return formData;
             }],
             headers: {
              'Content-Type': 'multipart/form-data',
              'X-CSRFToken': getCookie('csrftoken')
            }
          })
            .then(response => {
              console.log(response);
              if (response.status == '201') {
                this.$alert('已添加该CTF赛题', '上传成功', {
                  confirmButtonText: '确定',
                  callback: action => {
                    this.$router.go(0);
                  }
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
  },
  computed: {
  },
  mounted () {
  }
}
</script>