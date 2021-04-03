<template>
  <div class="tmplist">

    <draggable
    group="item"
    :options="{animation:300}"
    >
      <div
      v-for="item in tmplist"
      class="tmplist-item"
      :img="tmplist.img"
      :id="tmplist.id"
      >
      <img :src="item.img" style="width:80px;height:80px;">
      </div>
    </draggable>
    <div @click="reverse" class="tmplist-newimgbtn">
      <a>+</a>
    </div>


  </div>
</template>

<script>
import draggable from 'vuedraggable'
export default {
  name:'Tmplist',
  components: {
    draggable,
  },
  props:["uploadState","tmplist"],
  data(){
    return {
    }
  },
  methods:{
    reverse(){
      this.$emit('reverse')
    }
  }
}
</script>

<style scoped>
.tmplist{
  width: 80px;
  position: absolute;
  top: 120px;
  right: 20px;
  margin: auto;
  z-index:2;
}
.tmplist-item{
  width:80px;
  height: 80px;
}
.tmplist-newimgbtn {
  width:80px;
  height:80px;
  font-size:50px;
  line-height:80px;
}
.tmplist-newimgbtn a{
}
label{
}
input{
  display:none;
}

</style>
