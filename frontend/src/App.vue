<template>
  <v-app>
    <div id="app" >
      <WienHeader
      @reversedEditing="editing=$event"
      @clearData='clearData'
      @downloadPreset='downloadPreset'
      @toTrue="state=2"
      @toTrueCreatePresetState="state=3"/>

      <div class="main">
        <Table ref="table" :edge="edge" :editing="editing" :colorset="colorset" :bgcolor="bgColor" @reverse="state=1,changeimgstatus=true" />
        <Tmplist ref="tmplist" v-show="editing" :edge="edge" :tmplist="tmplist" :bgcolor="bgColor" @reverse="state=1"/>
        <Upload v-show="state==1||state==3"
        :tmplist="tmplist"
        :changeimgstatus="changeimgstatus"
        :C_img="C_img"
        :state="state"
        @close="state=0,changeimgstatus=false" @changeImg="C_img=$event,changeImg()"/>
        <Result v-show="state==2" @close="state=0"
        @reversedEditing="editing=true"/>
        <Toolbar
        @reverseBgcolor="bgColor=$event"
        @reverseColorSet="colorset=$event"
        @reverseEdge="edge=$event"
        @clearData='clearData'
        @downloadPreset='downloadPreset'
        @toTrue="state=2"
        @toTrueCreatePresetState="state=3"
        @reversedEditing="editing=$event"
        />
      </div>
    </div>
  </v-app>
</template>

<script>
let tmp=[]
import WienHeader from './components/WienHeader.vue'
import Table from './components/Table.vue'
import Tmplist from './components/Tmplist.vue'
import Upload from './components/Upload.vue'
import Result from './components/Result.vue'
import Toolbar from './components/Toolbar.vue'
export default {
  name: 'App',
  components:{
    'WienHeader':WienHeader,
    'Table':Table,
    'Tmplist':Tmplist,
    'Upload':Upload,
    'Result':Result,
    'Toolbar':Toolbar,
  },
  data(){
    return {
      //idle:0,upload:1,result:2,CreatePreset:3 状態（モード）
      state:0,
      tmplist:[
      ],
      bgColor: "#202020",
      edge:80,
      editing:true,
      colorset:3,
      changeimgstatus:false,
      C_img:"",
      jsonurlset:undefined,
      currentid:0
    }
  },
  methods:{
    changeImg(){
      this.changeimgstatus=false
      this.state=0
      this.$refs.table.changeItemImgGET(this.C_img)
    },
    clearData(){
      this.$refs.table.resetTable()
      this.tmplist.splice(0,this.tmplist.length)
      this.currentid=0
    },
    downloadPreset(get_key){

      const URL = 'http://127.0.0.1:8000/download/'+get_key;
      this.axios
        .get(URL)
        .then( response => {this.jsonurlset = response.data
        console.log(this.jsonurlset)
        let j=undefined
        for (let i=0;i<this.jsonurlset.imgset.length;i++){
          tmp.push(this.jsonurlset.imgset[i])
        }
        this.downloadImage()
      })
    },

    downloadImage(){
      console.log(tmp)
      for (let k=0;k<tmp.length;k++){
        this.axios
        .get(tmp[k],{responseType: "arraybuffer"})
        .then(response => {
          // this.tmplist.push(window.URL.createObjectURL(response.data))
          const prefix = `data:${response.headers["content-type"]};base64,`;
          const base64 = new Buffer(response.data, "binary").toString("base64");
          this.tmplist.push({img:prefix+base64,id:k})

        })
      }
      this.currentid=k
      tmp=[]

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
  position: relative;
  height: 100%;
  width:100%;
  background-color:white;
}
.main{
  position: relative;
  margin-top:40px;
  height: calc(100% - 40px);
  width:100%;
}

</style>
