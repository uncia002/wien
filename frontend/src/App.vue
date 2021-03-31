<template>
  <div id="app">
    <WienHeader/>
    <Table/>
    <Tmplist/>
    <!-- <Upload/> -->
  </div>
</template>

<script>
import WienHeader from './components/WienHeader.vue'
import Table from './components/Table.vue'
import Tmplist from './components/Tmplist.vue'
import Upload from './components/Upload.vue'
export default {
  name: 'App',
  components:{
    'WienHeader':WienHeader,
    'Table':Table,
    'Tmplist':Tmplist,
    'Upload':Upload
  }
}
</script>

<style>
html,body{
  margin: 0;
  height: 100%;
  overflow-y:hidden
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: relative;
  height: 100%;
  width:100%;
}
</style>
