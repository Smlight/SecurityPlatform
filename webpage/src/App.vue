<template>
  <div id="app">
    <v-head @change='updateInfo' :username='username'/>
    <router-view @change='updateInfo' @serverup='updateServer' :username='username'/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.content {
  width: 80%;
  margin: auto;
}
</style>

<script>
import vHead from '@/components/common/Header';

export default {
	name: 'App',
	components: {
	  vHead,
	},
	data() {
		return {
			username: '',
			server: ''
		}
	},
	mouted() {
		this.$http.get('/getuserinfo/')
		.then(response => {
            console.log(response);
            if (response.data.status === "ok") {
            	console.log("success");
            	this.username = response.data.user;
            } else {
            	console.log(response.data.status);
            }
        })
		.catch(error => {
			console.log(error);
		});
	},
	methods: {
		updateInfo(msg) {
			this.username = msg;
			console.log('App: Recvied!' + msg);
		},
		updateServer(msg) {
			this.server = msg;
			console.log('App: Recvied!' + msg);
		}
	}
}
</script>

