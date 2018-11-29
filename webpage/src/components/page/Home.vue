<template>
  <div class="wrapper">
    <div class="content">
      <el-breadcrumb>
        <el-breadcrumb-item>首页</el-breadcrumb-item>
      </el-breadcrumb>
      <div class="easyblock"><br></div>
      <el-input v-model="keyword" placeholder="输入关键词搜索" @change="remoteMethod()"></el-input>
      <div class="easyblock"><br></div>
      <el-table :data="CHAoptions" stripe style="width: 100%">
        <el-table-column prop="title" label="标题" width="">
        </el-table-column>
        <el-table-column prop="desc" label="描述" width="">
        </el-table-column>
        <el-table-column prop="year" label="年份" width="">
        </el-table-column>
        <el-table-column prop="game" label="比赛" width="">
        </el-table-column>
        <el-table-column prop="points" label="分值" width="">
        </el-table-column>
        <el-table-column prop="id" fixed="right" label="操作">
          <template slot-scope="scope">
            <el-button style="padding: 3px 0" type="text" @click="CHAIDviewMore(scope.row.id)">查看详情>></el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-button type="primary" @click="CHAviewMore()">查看更多<i class="el-icon-arrow-right el-icon--right"></i></el-button>
      <div class="easyblock"><br></div>
      <el-table :data="CVEoptions" stripe style="width: 100%">
        <el-table-column prop="cveid" label="CVE编号" width="">
        </el-table-column>
        <el-table-column prop="desc" label="描述" width="">
        </el-table-column>
        <el-table-column prop="year" label="披露日期" width="">
        </el-table-column>
        <el-table-column prop="component" label="本体程序" width="">
        </el-table-column>
        <el-table-column prop="version" label="版本" width="">
        </el-table-column>
        <el-table-column prop="severity" label="影响程度" width="">
        </el-table-column>
        <el-table-column prop="id" fixed="right" label="操作">
          <template slot-scope="scope">
            <el-button style="padding: 3px 0" type="text" @click="CVEIDviewMore(scope.row.cveid)">查看详情>></el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-button type="primary" @click="CVEviewMore()">查看更多<i class="el-icon-arrow-right el-icon--right"></i></el-button>
    </div>
  </div>
</template>

<style scoped>
.easyblock {
  line-height: 50px;
}
</style>

<script>
export default {
  data() {
    return {
      keyword: '',
      CHAlist: [],
      CVElist: [],
      loading: false,
      CHAnormallist: [],
      CVEnormallist: [],
    }
  },
  computed: {
    CHAoptions: function() {
      var res = this.CHAlist;
      for (var i in res) {
        if (res[i].desc.length > 90) {
          res[i].desc = res[i].desc.substr(0,90) + '......';
        }
      }
      return res;
    },
    CVEoptions: function() {
      var res = this.CVElist;
      for (var i in res) {
        if (res[i].desc.length > 90) {
          res[i].desc = res[i].desc.substr(0,90) + '......';
        }
      }
      return res;
    }
  },
  mounted() {
    this.$http.get('/api/challenges.json')
    .then(response => {
      if (false) {
        this.$alert('请检查网络', '获取失败', {
          confirmButtonText: '确定'
        });
      } else {
        this.CHAnormallist = response.data.results;
        this.CHAlist = this.CHAnormallist;
      }
    })
    .catch(error => {
      console.log(error);
    });
    this.$http.get('/api/cves.json')
    .then(response => {
      if (false) {
        this.$alert('请检查网络', '获取失败', {
          confirmButtonText: '确定'
        });
      } else {
        this.CVEnormallist = response.data.results;
        this.CVElist = this.CVEnormallist;
      }
    })
    .catch(error => {
      console.log(error);
    });
  },
  methods: {
      CHAIDviewMore(id) {
        this.$router.push('/challenges/' + id);
      },
      CHAviewMore() {
        this.$router.push('/challenges/');
      },
      CVEIDviewMore(id) {
        this.$router.push('/cves/' + id);
      },
      CVEviewMore() {
        this.$router.push('/cves/');
      },
      remoteMethod() {
        var query = this.keyword;
        if (query !== '') {
          this.loading = true;
          setTimeout(() => {
            this.loading = false;
            this.$http.post('/search/', {
              'keyword': query,
              'challenges': true,
              'cves': true,
            })
            .then(response => {
              console.log(response);
              if (response.data.status === "ok") {
                this.CHAlist = response.data.CHAlist;
                this.CVElist = response.data.CVElist;
              } else {
              }
            })
            .catch(error => {
              console.log(error);
            });
          }, 200);
        } else {
          this.CHAlist = this.CHAnormallist;
          this.CVElist = this.CVEnormallist;
        }
      }
  }
}
</script>
