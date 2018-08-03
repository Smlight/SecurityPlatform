<template>
	<div class="noSide">
		<div class="title">
			<h3>添加ctf题目</h3>
		</div>
		<el-form ref="addchaForm" :rules="rules" :model="form" label-width="120px">
			<el-form-item label="题目名称" prop="title">
				<el-input v-model="form.title"></el-input>
			</el-form-item>
			<el-form-item label="题目描述" prop="desc">
				<textarea v-model="form.desc" class="form-area"></textarea>
			</el-form-item>
			<el-form-item label="年份" prop="year">
				<el-input type="number" v-model="form.year"></el-input>
			</el-form-item>
			<el-form-item label="比赛名" prop="game">
				<el-input v-model="form.game"></el-input>
			</el-form-item>
			<el-form-item label="二进制文件" prop="file">
				<el-input type="file" id="file" v-model="form.file"></el-input>
			</el-form-item>
			<el-form-item label="难度" prop="difficulty">
				<el-input type="number" v-model="form.difficulty"></el-input>
			</el-form-item>
			<el-form-item label="docker仓库地址" prop="docker_repo">
				<el-input v-model="form.docker_repo"></el-input>
			</el-form-item>
			<el-form-item label="vagrant镜像地址" prop="vagrant_box">
				<el-input v-model="form.vagrant_box"></el-input>
			</el-form-item>
			<el-form-item label="利用代码" prop="poc">
				<textarea v-model="form.poc" class="form-area"></textarea>
			</el-form-item>
			<el-form-item label="参考资料" prop="references">
				<el-input v-model="form.references"></el-input>
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
  	margin: 5% auto;
    /*margin-top: 5%;*/
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

export default {
	data() {
		return {
	        form: {
	        	title: '',
	        	desc: '',
	        	year: '',
	        	game: '',
	        	file: null,
	        	difficulty: null,
	        	docker_repo: '',
	        	vagrant_box: '',
	        	poc: '',
	        	references: ''
	        },
	        rules: {
	        	title: [
           			{required: true, message: '请输入题目名称', trigger: 'blur'}
	        	],
	        	desc: [
	        	],
	        	year: [
	        	],
	        	game: [
	        	],
	        	file: [
           			{required: true, message: '请上传二进制文件', trigger: 'blur'}
	        	],
	        	difficulty: [
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
            axios({
			  url: '/api/challenges/',
			  method: 'post',
			  data: this.$data.form,
			  transformRequest: [function (data) {
			  	var ndata = new FormData();
			  	for (var i in data) {
			  		ndata.append(i, data[i]);
			  	}
			  	ndata['file']=document.getElementById('file').files[0];
			  	console.log(ndata);
			  	return ndata;
			  }],
			  headers: {
			    'Content-Type': 'multipart/form-data'
			  }
			})
          } else {
            // console.log('error submit!!');
            return false;
          }
        });
      },
	},
	computed: {
	},
	mounted: function() {
	}
}
</script>