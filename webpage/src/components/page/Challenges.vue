<template>
	<div style="width: 80%; margin: auto;">
		<h1> welcome to challenges </h1>
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
			<el-table-column fixed="right" label="操作" width="100">
				<template slot-scope="scope">
					<el-button style="padding: 3px 0" type="text" @click="">查看详情>></el-button>
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
</template>

<style scoped>
.demo-table-expand {
	font-size: 0;
}
.demo-table-expand label {
	width: 90px;
	color: #99a9bf;
}
.demo-table-expand .el-form-item {
	margin-right: 0;
	margin-bottom: 0;
	width: 50%;
}
.text {
	font-size: 14px;
}

.item {
	margin-bottom: 18px;
}

.clearfix:before, .clearfix:after {
	display: table;
	content: "";
}
.clearfix:after {
	clear: both
}
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
		}
	},
	computed: {
		options: function() {
			return this.list;
		}
	},
	mounted: function() {
		this.$http.get('/api/challenges.json')
		.then(response => {
			console.log(response);
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