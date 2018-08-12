<template>
  <div class="wrapper">
	<div class="content">
		<h1> Welcome to Challenges </h1>
		<el-table :data="options" stripe style="width: 100%">
			<el-table-column prop="title" label="标题" width="">
			</el-table-column>
			<el-table-column prop="desc" label="描述" width="">
			</el-table-column>
			<el-table-column prop="year" label="年份" width="">
			</el-table-column>
			<el-table-column prop="game" label="比赛" width="">
			</el-table-column>
			<el-table-column prop="difficulty" label="难度" width="">
			</el-table-column>
			<el-table-column prop="id" fixed="right" label="操作">
				<template slot-scope="scope">
					<el-button style="padding: 3px 0" type="text" @click="viewMore(scope.row.id)">查看详情>></el-button>
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
			pageSizes: [20, 50, 100, 200],
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
    		this.$router.push('/challenges/' + id);
    	}
	},
	computed: {
		options: function() {
			var res = this.list;
			for (var i in res) {
				if (res[i].desc.length > 90) {
					res[i].desc = res[i].desc.substr(0,90) + '......';
				}
			}
			return res;
		}
	},
	mounted () {
		this.$http.get('/api/challenges.json', {
		    params: {
		      page: this.currentPage
		    }
		})
		.then(response => {
			// console.log(response);
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

