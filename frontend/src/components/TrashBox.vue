<template>
  <div class="trashbox" >
    <div class="" style="position:relative;width:100%;height:100%;">
      <draggable
      tag="div"
      :options="{animation:300,group:'ITEMS'}"
      class="trash-draggable"
      @end="clear"
      >
        <div
        v-for="item in trash"
        class="trash-item"
        :key="item.id"
        >
        </div>
      </draggable>

    </div>


  </div>
</template>

<script>
import draggable from 'vuedraggable'
export default {
  name:'TrashBox',
  components: {
    draggable,
  },
  props:["editing"],
  data(){
    return {
      trash:[
      ],
    }
  },
  methods:{
    clear(evt){
      this.trash=[]
      console.log(evt)
      // var del=document.getElementByClass("delitem")
      evt.remove()
    }
  },

}
</script>

<style scoped>
.trashbox{
  width: 50px;
  height:100%;
  position: absolute;
  right: 0;
  margin: auto;
  z-index:2;
  background-color:#404040;
}
.trash-draggable{
  width:50px;
  height:100%;
}
.trash-item{
  width:20px;
  height:20px;
}
</style>
