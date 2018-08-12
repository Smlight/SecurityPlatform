<template>
  <div class="wrapper">
	<div class="content">
		<h1> Welcome to ChallengeDetail </h1>
		<div>
	        <div class="text item">
	          标题			{{ Challenge.title }}
	        </div>
	        <div class="text item">
	          描述			{{ Challenge.desc }}
	        </div>
	        <div class="text item">
	          年份			{{ Challenge.year }}
	        </div>
	        <div class="text item">
	          比赛			{{ Challenge.game }}
	        </div>
	        <div class="text item">
	          文件			{{ Challenge.file }}
	        </div>
	        <div class="text item">
	          难度			{{ Challenge.difficulty }}
	        </div>
	        <div class="text item">
	          Docker仓库地址		{{ Challenge.docker_repo }}
	        </div>
	        <div class="text item">
	          Vagrant镜像地址	{{ Challenge.vagrant_box }}
	        </div>
	        <div class="text item">
	          poc				{{ Challenge.poc }}
	        </div>
	        <div class="text item">
	          参考资料			{{ Challenge.references }}
	        </div>
        </div>
        <el-button type="primary" @click="goDeploy()">goDeploy</el-button>
	</div>
  </div>
</template>

<style scoped>
  .text {
    font-size: 2em;
  }

  .item {
    margin-bottom: 18px;
  }
</style>

<script>
export default {
	name: 'Challenge Detail',
    props:['username'],
	data() {
		return {
			Challenge: {
				id: null,
			}
		}
	},
	methods: {
		goDeploy() {
			console.log(this.username);
			if (this.username == '') {
				this.$router.push('/login');
			} else {
				this.$http.post('/deploychallenge/', this.$data.Challenge.id)
				.then(response => {
					console.log(response);
					if (response.data.status === "ok") {
						this.$emit('serverup',response.data.server);
						this.$router.push('/terminal');
					} else {
						this.$alert('Something Happened!', 'Failed', {
							confirmButtonText: '确定',
							callback: action => {
								this.$router.push('/index');
							}
						});
					}
				})
				.catch(error => {
					console.log(error);
				});
			}
		}
	},
	computed: {

	},
	created() {
		this.Challenge.id = this.$route.params.id;
	},
	mounted() {
		this.$http.get('/api/challenges/' + this.Challenge.id + '.json')
		.then(response => {
			console.log(response);
			if (false) {
				this.$alert('请检查网络', '获取失败', {
					confirmButtonText: '确定'
				});
			} else {
				this.Challenge = response.data;
			}
		})
		.catch(error => {
			console.log(error);
		});
	}
}

</script>