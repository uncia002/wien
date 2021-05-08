<template>
  <div class="tmplist" :style="{right: reverseRight}">
    <h2 class="tmplist-h2">Tmp</h2>
    <div class="tmplist-relative">
      <draggable
      tag="div"
      :options="{animation:300,group:'ITEMS'}" style="-ms-overflow-style: none;
      scrollbar-width: none;"
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
    },

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
  height:85%;
  position: absolute;
  top: 60px;
}
.tmplist-relative{
  position:relative;
  overflow-y:scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.tmplist-relative::-webkit-scrollbar {
  display:none;
}
.tmplist-h2{
  position:absolute;
  padding-left:10px;
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
