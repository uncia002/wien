<template>
  <div class="table">
    <div class="table-heading" >
      <div class="table-heading-item" v-for="list in tablelist">
        <input type="text" name="" v-model="list.title">
        <input type="text" name="" v-model="list.subtitle">
      </div>
      <div class="table-heading-button">
        <div v-show="editing" class="table-heading-button-wall" @click="createNewList">
          <img src="../assets/plus.png" class="table-heading-button-img">
        </div>
      </div>
    </div>
    <div class="" >
      <draggable
      v-for="list in tablelist"
      class="table-list"
      group="item"
      :options="{animation:300}"
      :key="list.no">

      <div
      v-for="item in list.items"
      class="table-list-item"
      :img="item.img"
      :key="item.id"
      >
      <img :src="item.img" style="width:80px;height:80px;">
    </div>
  </draggable>

    </div>
  </div>
</template>

<script>
import draggable from 'vuedraggable'
let x,newlist
export default {
  name:'Table',
  components: {
    draggable,
  },
  data(){
    return {
      tablelist:[
        {no:1,title:"S",subtitle:"1~100",items:[{img:"",id:1},{img:"",id:2},{img:"",id:3}]},
        {no:2,title:"A",subtitle:"100~1000",items:[{img:"",id:4},{img:"",id:5},{img:"",id:6}]},
        {no:3,title:"B",subtitle:"1000~10000",items:[{img:"",id:7},{img:"",id:8},{img:"",id:9},{img:"",id:17}]},
      ],
      editing:true,
    }
  },
  methods:{
    mouseOverDisplayButton(){
      this.newListButtonStatus=!this.newListButtonStatus
      console.log("status change!")
    },
    createNewList(){
      x=this.tablelist.length+1
      newlist={no:x,items:[]}
      this.tablelist.push(newlist)
      console.log(this.tablelist)
    }
  }
}
</script>

<style scoped>
.table{
  position: absolute;
  top: 120px;
  left: calc(50% - 80px);
  transform: translateX(-50%);
  -webkit- transform: translateX(-50%);
  margin: auto;
  display: flex;
}
.table-list{
  display:flex;
}

.table-list-item{
  width:80px;
  height: 80px;
}
.table-heading div:nth-child(1){
  border-top:1px solid black;
}
.table-heading-item{
  width: 80px;
  height: 80px;
  border: 1px solid black;
  border-top:none;
  background-color:white;
}
.table-heading-button{
  position:relative;

  transition: 0.5s;
}
.table-heading-button-wall{
  width:20px;
  height: 20px;
  top:-10px;
  left:29px;
  position:absolute;
  background-color: #121212;
  border-radius:50%;
}
.table-heading-button-img{
  width:15px;
  height:15px;
  margin-top:1.5px;

}
</style>
