<template>
<div class="header">
  <div class="navbar">
    <h5>Wienのろご</h5>
  </div>
  <div class="editbar">
    <div class="editbar-tool hint--top-right" aria-label="EDIT / PICTURE" >
      <div class="tool-editing" @click="editing=!editing, $emit('reversedEditing',editing)">
        <img src="@/assets/edit.png" class="icon"  :class="{'icon-t':editing,'icon-f':!editing}">
        <img src="@/assets/sc.png" class="icon" :class="{'icon-t':!editing,'icon-f':editing}">
      </div>
    </div>
    <div class="editbar-tool hint--top" aria-label="BACKCOLOR">
      <label for="bgcolor-input" name="bgcolor-select" style="display:flex" >
        <div class="bgcolor-material" :style="{ 'background-color': bgColor}">
        </div>
        <input id="bgcolor-input" maxlength='7' type="text" class="bgcolor-input" v-model="bgColor" @keyup.enter="$emit('reverseBgcolor',bgColor)">
      </label>
    </div>
    <div class="editer-slider hint--top" aria-label="ITEMSIZE">
      <p style="color:white;line-height:31px;margin-right:5px;">size</p>
      <v-slider
      v-model="edge"
      max="150"
      min="80"
      step="10"
      color="white"
      @change="$emit('reverseEdge',edge)"
      ></v-slider>
    </div>
    <div class="editer-headercolor">
      <select v-model="selectedcolorset" id="selectHeadColor" @change="$emit('reverseColorSet',selectedcolorset)">
        <option v-for="colorset in colorsets" :value="colorset.value">{{ colorset.state}}</option>
      </select>
      <label for="selectHeadColor">
        <img src="@/assets/detail.png" class="headercolor-detail">
      </label>
    </div>
    <div class="editbar-tool hint--top-left" aria-label="未実装" id="how">
      <a style="color:white;text-decoration: none;" href="#">How to use?</a>
    </div>
    <div class="editbar-tool" id="git">
      <a href="https://github.com/uncia002/wien" style="color:white;text-decoration: none;">Github</a>
    </div>
    <div class="editbar-tool" style="padding:0 10px;background-color:#6B717E;">
      <a  style="color:white;text-decoration: none;" @click="outputImg">Output</a>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name:'WienHeader',
  props:["resultState"],
  data(){
    return{
      bgColor: "#202020",
      edge:80,
      colorsets: [
          { state: 'White', value: 0 },
          { state: 'Black', value: 1 },
          { state: 'Tier', value: 2 }
        ],
      selectedcolorset:0,
      editing:true,
      dlurl:undefined,
    }
  },
  methods:{
    outputImg(){
        this.editing=false;
        this.$emit('reversedEditing',this.editing);
        this.$nextTick(function(){
          html2canvas(document.getElementById("outputdata")).then(function(canvas){
            var result = document.getElementById("resultscreen")
            result.innerHTML = ''
            result.appendChild(canvas);
            console.log(result.outerWidth)
  			  });
          this.$emit('toTrue');
        });

    }
  }
}
</script>

<style scoped>
:focus{
  outline: none;
}

.header{
  width: 100%;
  height: 80px;
  position:fixed;
  display: flex;
  color: white;
  background-color: #222222;
}
.navbar{
  width: 100%;
  height: 40px;
  position: absolute;
  display: flex;
}
.navbar h5{
  font-size:20px;
  margin:auto auto auto 20px;
}
.editbar{
  width: 100%;
  height: 40px;
  padding: 0 10px;
  top: 40px;
  position: absolute;
  display: flex;
}
.editbar-tool{
  height: 24px;
  margin: 7px 20px 7px 7px;
  border-radius:5px;
}

.bgcolor-material{
  width:10px;
  height:10px;
  margin:6px 10px 0 0;
  border-radius:50%;
}
.bgcolor-input{
  color:white;
  width:70px;
  transition: 0.3s;
}
.bgcolor-input:focus{
  border-bottom:solid 1px #ffffff;
}

.editer-slider{
  width:200px;
  margin:3px 0;
  display:flex;
}
.editer-headercolor{
  height:40px;
  width:75px;
  padding-top:5px;
  position:relative;
  margin-right:10px;
}
select{

  -webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
	padding: 7px 30px 7px 10px;
	font-size: 93%;
	line-height: 100%;
	border-radius: 5px;
	border: none;
	background-repeat: no-repeat;
	background-size: 12px 10px;
	background-position: right 10px center;
  color:white;
}
select::-ms-expand {
  display: none;
}
option{
  color: black;
  padding:3px 7px 3px 2px;

}


.tool-editing{
  position:relative;
  margin-right:20px;
}
.icon{
  transition:0.5s;
  position:absolute;
}
.icon-t{
  width:20px;
  height:20px;
  top:0;
  left:0;
}
.icon-f{
  width:10px;
  heihgt:10px;
  top:13px;
  left:18px;
}
.headercolor-detail{
  width:16px;
  height:12px;
  position:absolute;
  top:15px;
  left:60px;
}
#how{
  background-color:#6B717E;
  padding:0 10px;
}
#git{
  background-color:#6B717E;
  padding:0 10px;
}
</style>
