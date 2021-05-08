<template>
<div class="toolbar">
  <div name="bgcolor">
    <h5>背景色</h5>
    <div class="tool hint--top" aria-label="BACKCOLOR">
      <label for="bgcolor" style="display:flex" >
        <div class="bgcolor-material" :style="{ 'background-color': bgColor}">
        </div>
        <input id="bgcolor" maxlength='7' type="text" class="bgcolor-input" v-model="bgColor" @keyup.enter="$emit('reverseBgcolor',bgColor)"
        placeholder="#202020">
      </label>
    </div>
  </div>
  <div name="headcolor">
    <h5>ヘッドの背景色</h5>
    <div class="tool">
        <select v-model="selectedcolorset" id="headcolor" @change="$emit('reverseColorSet',selectedcolorset)" class="headcolor-select">
          <option v-for="colorset in colorsets" :value="colorset.value">{{ colorset.state}}</option>
        </select>
        <label for="headcolor">
        <img src="@/assets/detail.png" class="headcolor-icon">
        </label>
    </div>
  </div>
  <div name="boxsize">
    <h5>アイテムの大きさ</h5>
    <div class="tool" style="width:170px;margin-left: 22px;">
      <v-slider
      v-model="edge"
      max="150"
      min="80"
      step="10"
      color="white"
      @change="$emit('reverseEdge',edge)"
      ></v-slider>
    </div>
  </div>
  <div name="callpreset">
    <h5>プリセットを呼び出す</h5>
    <div class="tool" style="margin-left:30px;">
      <label for="callpreset-input" name="bgcolor-select" style="display:flex" >
        <input id="callpreset-input" maxlength='9' type="text" class="bgcolor-input" v-model="presetcode" @keyup.enter="applyPreset" placeholder="presetname">
      </label>
    </div>
  </div>
  <div name="createpreset" class="tool-button" @click="$emit('toTrueCreatePresetState')">
    <h5>プリセットを作る</h5>
  </div>
  <div name="generate"　class="tool-button" @click="outputImg">
    <h5>画像をジェネレート</h5>
  </div>
  <div class="">
    <a href="https://github.com/uncia002/wien">ヘルプ</a>
  </div>
  <div class="" >
    <a href="https://github.com/uncia002/wien">Github</a>
  </div>
</div>
</template>

<script>
export default {
  name:'Toolbar',
  data(){
    return{
      bgColor: "#202020",
      edge:80,
      colorsets: [
          { state: 'White', value: 0 },
          { state: 'Black', value: 1 },
          { state: 'Tier', value: 2 },
          { state: 'Background　Color' ,value: 3}
        ],
      selectedcolorset:3,
      editing:true,
      dlurl:undefined,
      presetcode:""
    }
  },
  methods:{
    applyPreset(){
      this.$emit('clearData')
      this.$emit('downloadPreset',this.presetcode)
    },
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

    },
  }
}
</script>

<style scoped>
:focus{
  outline: none;
}
a{
text-decoration: none;
color: white;
}

.toolbar{
  position:absolute;
  width: 250px;
  height: 100%;
  background-color: #202020;
  padding: 20px 20px;
  text-align: left;
  color: white;

}
.tool{
  height: 35px;
  font-size: 20px;
  margin: 8px 0;
  margin-bottom: 20px;
}
.tool-button{
  width:190px;
  height:35px;
  margin:25px 8px;
  background-color:white;
  color:black;
  line-height: 35px;
  text-align: center;
}
.bgcolor-material{
  width:10px;
  height:10px;
  margin:11px 10px;
  border-radius:50%;
}
.bgcolor-input{
  color:white;
  height: 30px;
  width:150px;
  transition: 0.3s;
  border-bottom:solid 1px #ffffff;
}

.headcolor-select{
  padding: 7px 30px 7px 10px;
  margin-left:22px;
  width:140px;
	font-size: 93%;
	line-height: 100%;
	border: none;
  color:white;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}
.headcolor-select::-ms-expand {
  display: none;
}
.headcolor-select option{
  color: white;
  background-color:#202020;
  padding:3px 7px 3px 2px;
}
.headcolor-icon{
  width:16px;
  height:12px;
}

</style>
