<template>
  <div class="table" >
    <div class="table-relative" >
      <div class="table-title" >
        <h1 >Table</h1>
      </div>
      <div class="table-detail">
        <p>Drag and drop the image to move it. Images can be added from "index". Click on the image to see the options</p>
      </div>
      <div style="display:flex" :style="{'background-color':bgcolor}" class="table-data" id="outputdata" ref="outputdata">
        <div class="table-heading" >
          <div class="table-heading-item" v-for="(list,index) in tablelist" :style="{width: reverseEdge,height:reverseEdge,'background-color': reversedColor(index)}">
            <input type="text" class="table-heading-title" v-model="list.title" placeholder="Title" :style="{color:reversedTextColor(index)}">
            <textarea type="textarea" class="table-heading-subtitle" v-model="list.subtitle" placeholder="Sub Title":style="{color:reversedTextColor(index)}"></textarea>
          </div>
          <div class="table-heading-button" :style="{width: reverseEdge,height:reverseEdge}" v-show="editing" @click="createNewList">
            <!-- <div v-show="editing" class="table-heading-button-wall" @click="createNewList">
            </div> -->
            <p :style="{'line-height':reverseEdge,color:reversedTextColorBG }">+</p>
          </div>
        </div>
        <div style="width:100%;">
          <div v-for="(list,L) in tablelist" :key="list.no" >

            <draggable
            tag="div"
            class="table-list"
            :options="{animation:300,group:'ITEMS'}"
            :style={height:reverseEdge}
            >
              <div
              v-for="(item,I) in list.items"
              class="table-list-item"
              :key="item.id"
              :style="{width: reverseEdge,height:reverseEdge}"
              @click.stop="itemStatusJudge(item.id)"
              >
                <img :src="item.img" :style="{width: reverseEdge,height:reverseEdge}" class="item-img">
                <div class="item-option" v-if="itemstatus==item.id" >
                  <div class="item-delete" @click="itemDelete(L,I)" >
                    <img src="@/assets/del.png" alt=""  style="width:15px;height:15px;">
                  </div>
                  <div class="item-pic" @click="changeItemImg(L,I)" >
                    <img src="@/assets/pic.png" style="width:13px;height:13px;">
                  </div>
                </div>
              </div>
            </draggable>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
let i
let foo
var colorList=["DB3A34","FFC857"]
import draggable from 'vuedraggable'
let x,newlist
const defalist =[
  {no:1,title:"S",subtitle:"1~10",items:[]},
  {no:2,title:"A",subtitle:"10~100",items:[]},
  {no:3,title:"B",subtitle:"100~1000",items:[]},
]
function splitColor(c1,c2,times){
    var r1 = parseInt( c1.substr(1,2), 16 ) ;
    var g1 = parseInt( c1.substr(3,2), 16 ) ;
    var b1 = parseInt( c1.substr(5,2), 16 ) ;
    var r2 = parseInt( c2.substr(1,2), 16 ) ;
	  var g2 = parseInt( c2.substr(3,2), 16 ) ;
	  var b2 = parseInt( c2.substr(5,2), 16 ) ;
	  var minvalue=[Math.min(r1,r2),Math.min(g1,g2),Math.min(b1,b2)]
    var diff=[Math.max(r1,r2)-minvalue[0],Math.max(g1,g2)-minvalue[1],Math.max(b1,b2)-minvalue[2]]
    var delta=[Math.floor(diff[0]/times),Math.floor(diff[1]/times),Math.floor(diff[2]/times)]
    console.log(delta)
    var ans =[minvalue]
    var cl=["#"+minvalue[0].toString(16)+minvalue[1].toString(16)+minvalue[2].toString(16)]
    for (let i=1;i<times+1;i++){
        ans.push([ans[i-1][0]+delta[0],ans[i-1][1]+delta[1],ans[i-1][2]+delta[2]])
        cl.push("#"+ans[i][0].toString(16)+ans[i][1].toString(16)+ans[i][2].toString(16)
    )
    }
    return cl
}


function blackOrWhite ( hexcolor ) {
	var r = parseInt( hexcolor.substr(1,2), 16 ) ;
	var g = parseInt( hexcolor.substr(3,2), 16 ) ;
	var b = parseInt( hexcolor.substr(5,2), 16 ) ;

	return ( ( ( (r * 299) + (g * 587) + (b * 114) ) / 1000 ) < 128 ) ? "white" : "#222222" ;
}

export default {
  name:'Table',
  components: {
    draggable,
  },
  props:["edge","editing","colorset","C_img","bgcolor"],
  data(){
    return {
      tablelist:[
        {no:1,title:"S",subtitle:"1~10",items:[{img:require("../assets/a0.jpg"),id:1},{img:require("../assets/a1.jpg"),id:2},{img:require("../assets/a2.jpg"),id:3}]},
        {no:2,title:"A",subtitle:"10~100",items:[]},
        {no:3,title:"B",subtitle:"100~1000",items:[]},
      ],
      textcolor:"white",
      itemstatus:30,
      changeinfo:{no:0,id:0},
      edgediff:5,
      colorList:["#DB3A34","#ED8145","#FFC857"],
    }
  },
  methods:{
    mouseOverDisplayButton(){
      this.newListButtonStatus=!this.newListButtonStatus
      console.log("status change!")
    },
    createNewList(){
      x=this.tablelist.length+1
      newlist={no:x,title:"",subtitle:"",items:[]}
      this.tablelist.push(newlist)
      console.log(this.tablelist)
      this.colorList=splitColor("#DB3A34","#FFC857",this.tablelist.length-1)
    },
    itemDelete(no,id){
      this.tablelist[no].items.splice(id,1)
      console.log("s")
    },
    changeItemImg(nov,idv){
      this.changeinfo.no=nov
      this.changeinfo.id=idv
      this.$emit('reverse')
    },
    changeItemImgGET(imageing){
      console.log("dasdadasdsa")
      this.tablelist[this.changeinfo.no].items[this.changeinfo.id].img=imageing
    },
    itemStatusJudge(id){
      if(this.itemstatus==id){
        this.itemstatus=0
      }else{
        this.itemstatus=id
      }
    },
    resetTable(){
      for (let i=0;i<this.tablelist.length;i++){
        foo=this.tablelist[i].items.splice(0,this.tablelist[i].items.length)
        if (i>2){
          foo= this.tablelist.splice(i,1)
        }
      }
    },
  },
  computed:{
    reverseEdge(){
      return this.edge+"px"
    },
    reversedColor(){
      return function(number){
        switch (this.colorset){
          case 0:
            return "white";
          case 1:
            return "#222222";
          case 2:
            return this.colorList[number];
          case 3:
            return this.bgcolor
        }
      }
    },
    reversedTextColor(){
      return function(number){
        switch (this.colorset){
          case 0:
            return "#222222";
          case 1:
            return "white";
          case 2:
            return blackOrWhite(this.colorList[number]);
          case 3:
            return blackOrWhite(this.bgcolor)
          }
      }
    },
    reverseEdgeDiff(){
      return this.edgediff/2 + "px"
    },
    reversedTextColorBG(){
      return blackOrWhite(this.bgcolor)
    }
  },
}
</script>

<style scoped>
:focus{
  outline:none;
}
.table{
  position: absolute;
  top: 80px;
  left: calc(50% - 80px);
  transform: translateX(-50%);
  -webkit-transform: translateX(-50%);
  transition:0.4s;
}
.table-relative{
  position:relative;
}
.table-title{
  position:absolute;
  top:-60px;
  left:20px;
  display:flex;
}
.table-title h1{
  font-family: 'Inter', sans-serif;
  letter-spacing: -1.75px;
  font-size:45px;
  color:black;
  margin-right:10px;
}
.table-title p{
  font-family:'sans-serif';
  font-size:8px;
  color:#777777;
  text-align:left;
  margin:0;
}
.table-detail{
  position:absolute;
  bottom:-20px;
  left:20px;
  display:flex;
  transition:0.5s;
  transform: translateY(100%);
  -webkit-transform: translateY(100%);
}
.table-detail p{
  font-family:'sans-serif';
  font-size:15px;
  color:#777777;
  text-align:left;
}

.table-data{
  padding:30px 40px;
  border-radius: 20px;
}

.table-list{
  display:flex;
  width:100%;
}

.table-list-item{
  width:80px;
  height: 80px;
  position:relative;
}
.table-heading div:nth-child(1){
  border-top:1px solid #222222;
}
.table-heading-item{
  width: 80px;
  height: 80px;
  border: 1px solid #222222;
  position:relative;
  border-top:none;
  background-color:white;

}
.table-heading-title{
  position:absolute;
  width:100%;
  top:40%;
  left:50%;
  transform: translateX(-50%) translateY(-50%);
  text-align:center;
  font-size:30px;

}
.table-heading-subtitle{
  position:absolute;
  width:100%;
  top:55%;
  left:50%;
  transform: translateX(-50%);
  text-align:center;
  font-size:15px;
  resize:none;
  overflow:hidden;
}

.table-heading-button{
  position:relative;
  transition:0.5s;
  border-radius:20px;
}
.table-heading-button:hover{
  background-color:#3C91E6;
  transform:rotate(180deg);
}

.table-heading-button p{
  transition:0.5s;
  margin:auto;

  font-size:30px;
}
.item-option{
  top:0;
  right:0;
  width:20px;
  height:60px;
  position:absolute;
}
.item-delete{
  width:20px;
  height:20px;
  border-radius:50%;
  background-color:#222222;
  margin-bottom:3px;
}
.item-pic{
  width:20px;
  height:20px;
  margin-bottom:10px;
  border-radius:50%;
  background-color:#222222;
}
.item-img{
  object-fit: contain;

}
</style>
