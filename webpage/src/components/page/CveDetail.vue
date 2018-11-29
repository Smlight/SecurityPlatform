<template>
	<div class="wrapper">
		<div class="content">
			<el-breadcrumb>
				<el-breadcrumb-item :to="{ path: '/index' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/cves'}">CVE漏洞库</el-breadcrumb-item>
				<el-breadcrumb-item>{{ CVE.cveid }}</el-breadcrumb-item>
			</el-breadcrumb>
			<div>
				<h2>{{ CVE.cveid }}	</h2>
				<h3>漏洞描述			</h3>
				<div class="text">
					{{ CVE.desc }}
				</div>
				<h3>披露年份			</h3>
				<div class="text">
					{{ CVE.year }}
				</div>
				<h3>漏洞本体程序及版本</h3>
				<div class="text">
					{{ CVE.component }} {{ CVE.version }}
				</div>
				<h3>影响程度			</h3>
				<div class="text">
					{{ CVE.severity }}
				</div>
				<h3>Docker仓库地址	</h3>
				<div class="text">
					{{ CVE.docker_repo }}
				</div>
				<h3>Vagrant镜像地址	</h3>
				<div class="text">
					{{ CVE.vagrant_box }}
				</div>
				<h3>poc				</h3>
				<div class="text">
					{{ CVE.poc }}
				</div>
				<h3>参考资料			</h3>
				<div class="text item">
					<a :href="CVE.cveid">{{ CVE.references }}</a>
				</div>
			</div>
			<el-button type="primary" @click="goDeploy()">自动部署</el-button>
		</div>
	</div>
</template>

<style scoped>
  .text {
    font-size: 1.2em;
  }

  .item {
    margin-bottom: 18px;
  }
</style>

<script>
export default {
	name: 'CVE Detail',
    props:['username'],
	data() {
		return {
			CVE: {
				cveid: null,
			},
			// CVE: {
	  //           "cveid": "CVE-2004-2167",
	  //           "desc": "Multiple buffer overflows in LaTeX2rtf 1.9.15, and possibly other versions, allow remote attackers to execute arbitrary code via (1) the expandmacro function, and possibly (2) Environments and (3) TranslateCommand.",
	  //           "year": "2004",
	  //           "component": "LaTeX2rtf",
	  //           "version": "1.9.15",
	  //           "severity": 3,
	  //           "docker_repo": "anonymous2018/cve-2004-2167",
	  //           "vagrant_box": null,
	  //           "poc": "a",
	  //           "references": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-2167"
		 //    }
		}
	},
	methods: {
		goDeploy() {
			if (this.username == '') {
				this.$router.push('/login');
			} else {
				this.$http.post('/deploy/', {
					cveid: this.$data.CVE.cveid
				})
				.then(response => {
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
		this.CVE.cveid = this.$route.params.id;
	},
	mounted() {
		this.$http.get('/api/cves/' + this.CVE.cveid + '.json')
		.then(response => {
			if (false) {
				this.$alert('请检查网络', '获取失败', {
					confirmButtonText: '确定'
				});
			} else {
				this.CVE = response.data;
			}
		})
		.catch(error => {
			console.log(error);
		});
	}
}

</script>