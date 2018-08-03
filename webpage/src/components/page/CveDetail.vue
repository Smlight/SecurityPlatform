<template>
  <div class="wrapper">
    <v-head></v-head>
	<div class="content">
		<h1> welcome to {{ id }} </h1>
	</div>
  </div>
</template>

<style scoped>

</style>

<script>
import vHead from '@/components/common/Header';

export default {
    components: {
      vHead,
    },
	data() {
		return {
			id: null,
		}
	},
	methods: {

	},
	computed: {

	},
	created: function() {
		this.id = this.$route.params.id;
	},
	mounted: function() {

	}
}

</script>