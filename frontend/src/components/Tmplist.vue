<template>
  <div class="tmplist" :style="{right: reverseRight}">
    <div class="tmplist-relative">
      <h2 class="tmplist-h2">Index</h2>
      <draggable
      tag="div"
      :options="{animation:300,group:'ITEMS'}"
      >
        <div
        v-for="item in tmplist"
        class="tmplist-item"
        :img="item.img"
        :key="item.id"
        :style="{width: reverseEdge,height:reverseEdge}"
        >
          <img :src="item.img" :style="{width: reverseEdge,height:reverseEdge}">
        </div>
      </draggable>
      <div @click="reverse" class="tmplist-newimgbtn" :style="{width: reverseEdge,height:reverseEdge}">
        <p style="color:#202020">+</p>
      </div>

    </div>


  </div>
</template>

<script>
import draggable from 'vuedraggable'
function blackOrWhite ( hexcolor ) {
	var r = parseInt( hexcolor.substr( 1, 2 ), 16 ) ;
	var g = parseInt( hexcolor.substr( 3, 2 ), 16 ) ;
	var b = parseInt( hexcolor.substr( 5, 2 ), 16 ) ;

	return ( ( ( (r * 299) + (g * 587) + (b * 114) ) / 1000 ) < 128 ) ? "white" : "black" ;
}

export default {
  name:'Tmplist',

  components: {
    draggable,
  },
  props:["tmplist","edge","bgcolor"],
  data(){
    return {
    }
  },
  methods:{
    reverse(){
      this.$emit('reverse')
    }
  },
  computed:{
    reverseEdge(){
      return this.edge+"px"
    },
    reverseRight(){
      return (this.edge-80)+20+"px"
    },
    reversedTextColorBG(){
      return blackOrWhite(this.bgcolor)
    }
  }
}
</script>

<style scoped>
.tmplist{
  width: 80px;
  position: absolute;
  top: 60px;
  z-index:2;
}
.tmplist-relative{
  position:relative;
}
.tmplist-h2{
  position:absolute;
  top:-35px;
  left:0;
  font-family: 'Inter', sans-serif;
  letter-spacing: -1.75px;
  font-size:30px;
  color:black;
}

.tmplist-item{
  width:80px;
  height: 80px;
}
.tmplist-newimgbtn {
  width:80px;
  height:80px;
  font-size:50px;
}
.tmplist-newimgbtn p{
  margin:auto;
  font-size:30px;
}
label{
}
input{
  display:none;
}

</style>
