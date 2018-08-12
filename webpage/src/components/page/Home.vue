<template>
  <div class="wrapper">
      <div class="content">
          <h1> Welcome to Home </h1>
    <el-table :data="CHAoptions" stripe style="width: 100%">
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
          <el-button style="padding: 3px 0" type="text" @click="CHAviewMore(scope.row.id)">查看详情>></el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-table :data="CVEoptions" stripe style="width: 100%">
      <el-table-column prop="cveid" label="CVE编号" width="">
      </el-table-column>
      <el-table-column prop="desc" label="描述" width="">
      </el-table-column>
      <el-table-column prop="dtime" label="披露日期" width="">
      </el-table-column>
      <el-table-column prop="program" label="本体程序" width="">
      </el-table-column>
      <el-table-column prop="version" label="版本" width="">
      </el-table-column>
      <el-table-column prop="difficulty" label="利用难度" width="">
      </el-table-column>
      <el-table-column prop="id" fixed="right" label="操作">
        <template slot-scope="scope">
          <el-button style="padding: 3px 0" type="text" @click="CVEviewMore(scope.row.cveid)">查看详情>></el-button>
        </template>
      </el-table-column>
    </el-table>
      </div>
  </div>
</template>

<style scoped>
</style>

<script>
export default {
  data() {
    return {
      CHAlist: [],
      CVElist: [],
      loading: false,
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
      // console.log(response);
      if (false) {
        this.$alert('请检查网络', '获取失败', {
          confirmButtonText: '确定'
        });
      } else {
        this.CHAlist = response.data.results;
      }
    })
    .catch(error => {
      console.log(error);
    });
    this.$http.get('/api/cves.json')
    .then(response => {
      console.log(response);
      if (false) {
        this.$alert('请检查网络', '获取失败', {
          confirmButtonText: '确定'
        });
      } else {
        this.CVElist = response.data.results;
      }
    })
    .catch(error => {
      console.log(error);
    });
  },
  methods: {
      CVEviewMore(id) {
        // console.log(id);
        this.$router.push('/cves/' + id);
      },
      CHAviewMore(id) {
        // console.log(id);
        this.$router.push('/challenges/' + id);
      }
  }
}
</script>
