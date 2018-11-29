<template>
  <div id="app">
    <v-head @change='updateInfo' :username='username'/>
    <router-view @change='updateInfo' @serverup='updateServer' :username='username' :server='server'/>
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
	mounted() {
		this.$http.get('/getuserinfo/')
		.then(response => {
            if (response.data.status === "ok") {
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
		},
		updateServer(msg) {
			this.server = JSON.stringify(msg);
		}
	}
}
</script>

