<template>
  <div class="wrapper">
	<div class="content">
      <el-breadcrumb>
        <el-breadcrumb-item :to="{ path: '/index' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>CVE漏洞库</el-breadcrumb-item>
      </el-breadcrumb>
		<el-table :data="options" stripe style="width: 100%">
			<el-table-column prop="cveid" label="CVE编号" sortable>
			</el-table-column>
			<el-table-column prop="desc" label="描述" width="">
			</el-table-column>
			<el-table-column prop="year" label="披露年份" sortable>
			</el-table-column>
			<el-table-column prop="component" label="本体程序" width="">
			</el-table-column>
			<el-table-column prop="version" label="版本" width="">
			</el-table-column>
			<el-table-column prop="severity" label="影响程度" sortable>
			</el-table-column>
			<el-table-column prop="id" fixed="right" label="操作">
				<template slot-scope="scope">
					<el-button style="padding: 3px 0" type="text" @click="viewMore(scope.row.cveid)">查看详情>></el-button>
				</template>
			</el-table-column>
		</el-table>
		<div>
			<el-pagination
			@size-change="handleSizeChange"
			@current-change="handleCurrentChange"
			:current-page="currentPage"
			:page-sizes="pageSizes"
			:page-size="pageSize"
			layout="total, sizes, prev, pager, next, jumper"
			:total="llen">
			</el-pagination>
		</div>
	</div>
  </div>
</template>

<style scoped>

</style>

<script>
export default {
	data() {
		return {
			list: [],
			llen: 0,
			loading: false,
			currentPage: 1,
			pageSizes: [20, 50, 100],
			pageSize: 50,
		}
	},
	methods: {
		handleSizeChange(val) {
			console.log(`每页 ${val} 条`);
			this.pageSize = val;
		},
		handleCurrentChange(val) {
			console.log(`当前页: ${val}`);
			this.currentPage = val;
		},
    	viewMore(id) {
    		// console.log(id);
    		this.$router.push('/cves/' + id);
    	}
	},
	computed: {
		options: function() {
			var res = this.list;
			for (var i in res) {
				if (res[i].desc.length > 50) {
					res[i].desc = res[i].desc.substr(0,50) + '......';
				}
			}
			return res;
			return [
		        {
		            "cveid": "CVE-2004-2167",
		            "desc": "Multiple buffer overflows in LaTeX2rtf 1.9.15, and possibly other versions, allow remote attackers to execute arbitrary code via (1) the expandmacro function, and possibly (2) Environments and (3) TranslateCommand.",
		            "year": "2004",
		            "component": "LaTeX2rtf",
		            "version": "1.9.15",
		            "severity": 3,
		            "docker_repo": "anonymous2018/cve-2004-2167",
		            "vagrant_box": null,
		            "poc": "a",
		            "references": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-2167"
		        }
		    ];
		}
	},
	mounted () {
		this.$http.get('/api/cves.json', {
		    params: {
		      page: this.currentPage
		    }
		})
		.then(response => {
			if (false) {
				this.$alert('请检查网络', '获取失败', {
					confirmButtonText: '确定'
				});
			} else {
				this.list = response.data.results;
				this.llen = response.data.count;
			}
		})
		.catch(error => {
			console.log(error);
		});
	}
}
</script>