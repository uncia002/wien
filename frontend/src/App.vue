<template>
  <v-app>
    <div id="app" >
      <WienHeader
      :resultState="resultState"
      @reverseBgcolor="bgColor=$event"
      @reverseEdge="edge=$event"
      @reversedEditing="editing=$event"
      @reverseColorSet="colorset=$event"
      @toTrue="resultState=true"/>

      <div class="main">
        <Table ref="table" :edge="edge" :editing="editing" :colorset="colorset" :bgcolor="bgColor" @reverse="uploadState=true,changeimgstatus=true" />
        <Tmplist v-show="editing" :edge="edge" :tmplist="tmplist" :bgcolor="bgColor" @reverse="uploadState=true"/>
        <Upload v-show="uploadState" :tmplist="tmplist" :changeimgstatus="changeimgstatus" :C_img="C_img"
        @close="uploadState=false,changeimgstatus=false" @changeImg="C_img=$event,changeImg()"/>
        <Result v-show="resultState" @close="resultState=false"/>
      </div>
    </div>
  </v-app>
</template>

<script>

import WienHeader from './components/WienHeader.vue'
import Table from './components/Table.vue'
import Tmplist from './components/Tmplist.vue'
import Upload from './components/Upload.vue'
import Result from './components/Result.vue'
export default {
  name: 'App',
  components:{
    'WienHeader':WienHeader,
    'Table':Table,
    'Tmplist':Tmplist,
    'Upload':Upload,
    'Result':Result,
  },
  data(){
    return {
      uploadState:false,
      resultState:false,
      tmplist:[
      ],
      bgColor: "#202020",
      edge:80,
      editing:true,
      colorset:0,
      changeimgstatus:false,
      C_img:"",
    }
  },
  methods:{
    changeImg(){
      this.changeimgstatus=false
      this.uploadState=false
      this.$refs.table.changeItemImgGET(this.C_img)
    }
  }
}
</script>

<style>
html,body{
  margin: 0;
  height: 100%;
  overflow-y:hidden;
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
  background-color:white;
}
.main{
  position: relative;
  margin-top:80px;
  height: calc(100% - 80px);
  width:100%;
}

</style>
