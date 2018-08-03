<template>
  <div class="wrapper">
    <v-head></v-head>
      <div class="content">
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
        content: {
          backgroundImage: "url(" + require('../../../static/img/2.jpg') + ")",
          backgroundRepeat: "no-repeat",
          backgroundPosition: "left top",
          backgroundAttachment: "fixed",
          backgroundSize: "100%",
        },
      }
    },
    mounted: function () {
    },
    methods: {
    }
  }
</script>
