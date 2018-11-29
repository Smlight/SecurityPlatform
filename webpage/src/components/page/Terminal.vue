<template>
  <div class="wrapper">
    <div class="content">
      <el-breadcrumb>
        <el-breadcrumb-item :to="{ path: '/index' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/cves'}">CVE漏洞库</el-breadcrumb-item>
        <el-breadcrumb-item>网页终端</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
  </div>
</template>

<style>
.terminal {
  width: 66%;
  margin: auto;
}
</style>

<script>
import Terminal from './Xterm'
import WSSHClient from './ws'

export default {
  name: 'Terminal',
  props: ['username','server'],
  data() {
    return {
      charWidth: 6.2,
      charHeight: 15.2
    }
  },
  mounted() {
    this.connect();
  },
  computed: {
    options() {
      var res = JSON.parse(this.server);
      res['ispwd'] = 'true';
      res['username'] = this.username;
      res['secret'] = this.username;
      return res;
    }
  },
  methods: {
    openTerminal(options) {
      var client = new WSSHClient();
      var term = new Terminal({cols: 80, rows: 30, screenKeys: true, useStyle: true});
      term.on('data', function (data) {
        client.sendClientData(data);
      });
      term.open();
      term.write('Connecting...' + '\r\n');

      client.connect({
        onError: function (error) {
          term.write('Error: ' + error + '\r\n');
          console.debug('Error: '+error);
          alert('Error: '+error)
          term.destroy();
        },
        onConnect: function () {
          client.sendInitData(options);
          client.sendClientData('\r');
          console.debug('connection established');
          client.sendClientData(options.cmd + '\r\n');
        },
        onClose: function (e) {
          term.write("\rconnection closed")
          console.debug(e);
          term.destroy();
        },
        onData: function (data) {
          term.write(data);
        }
      })
    },
    connect() {
      this.openTerminal(this.options);
    }
  }
}
</script>