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
      </div>
    </draggable>
    <label for="input_newimg">
      <div class="tmplist-newimgbtn">
        <a >+</a>
      </div>
    </label>
    <input @change="setImage" type="file" name="image" accept="image/*" id="input_newimg">
  </div>
</template>

<script>
import draggable from 'vuedraggable'
export default {
  name:'Tmplist',
  components: {
    draggable,
  },
  data(){
    return {

      tmplist:[
        {img:"",id:10},{img:"",id:11},{img:"",id:12},
      ]

    }
  }
}
</script>

<style>
.tmplist{
  width: 80px;
  position: absolute;
  top: 120px;
  right: 20px;
  margin: auto;
}
.tmplist-item{
  width:80px;
  height: 80px;
  background-color:#232323;
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
