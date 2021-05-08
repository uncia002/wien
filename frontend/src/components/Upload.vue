<template>
<div class="filter" @click.self="closeWindow">
  <div class="upload">
    <div class="upload-title">
      <h2 v-show="state==1">Edit.</h2>
      <h2 v-show="state==3">CreatePreset.</h2>
    </div>

    <input  type="file" name="image" accept="image/*"   @change="setImage" id="upload-inputimg" >
    <label v-if="imgSrc==''" class="upload-label" for="upload-inputimg">
      <div class="upload-input">
        <a>追加 / トリミングする画像をアップロード</a>
      </div>
    </label>
    <div
    v-if="imgSrc !== ''"
    class="l_cropper_container"
    >
      <vue-cropper
      ref="cropper"
      :guides="true"
      :view-mode="2"
      drag-mode="crop"
      :auto-crop-area="0.5"
      :min-container-width="350"
      :min-container-height="350"
      :background="true"
      :rotatable="false"
      :src="imgSrc"
      alt="Source Image"
      :img-style="{ 'width': '500px', 'height': '350px' }"
      :aspect-ratio="targetWidth / targetHeight"
      >
      </vue-cropper>
    </div>
    <div  @click="cropImage" v-if="imgSrc !== ''" class="upload-trimbutton">
      <a> Push</a>
    </div>
    <div class="presetList" v-if="state==3">
      <div class="presetList-item" v-for="(item,index) in presetlist" :key="item.img">
        <img :src="item" style="width: 70px;height:70px;object-fit: contain;">
        <div class="item-delete" @click="presetlist.splice(index,1)" >
          <img src="@/assets/del.png" alt=""  style="width:15px;height:15px;">
        </div>
      </div>
    </div>
    <div v-if="state==3" class="upload-presetname">
      <label for="presetname-input" style="display:flex" >
        <div class="presetname">
          <p>PresetName:</p>
          <input id="presetname-input" maxlength='15' type="text" class="presetname-input" v-model="presetname">
        </div>
      </label>
    </div>
    <div v-if="state==3" @click="postPreset" class="upload-presetbutton">
      <a>Create!</a>
    </div>
    <img :src="rev" alt="">
  </div>
</div>
</template>

<script>
import VueCropper from 'vue-cropperjs'
import 'cropperjs/dist/cropper.css'
export default {
  components: {
    VueCropper
  },
  props:["tmplist","changeimgstatus","state"],
  data () {
    return {
      targetWidth: 1,
      targetHeight: 1,
      imgSrc: '',
      cropImg:'',
      cntId:13,
      presetlist:[],
      presetname:'',
      rev:undefined,
    }
  },
  methods: {
    setImage (event) {
      console.log("aaaaaaaaawwwwwwwwwww")
      const file = event.target.files[0];
      console.log(file)
      if (!file.type.includes('image/')) {
        alert('Please select an image file');
        return;
      }
      if (typeof FileReader === 'function') {
        const reader = new FileReader();
        reader.onload = event => {
          this.imgSrc = event.target.result
        }
        reader.readAsDataURL(file)
        console.log("shaoooooooooooooo")
      } else {
        alert('Sorry, FileReader API not supported')
      }
    },
    cropImage () {
      this.cropImg = this.$refs.cropper.getCroppedCanvas().toDataURL()
      if (this.changeimgstatus==true){
        var tmpimg=this.cropImg
        this.$emit('changeImg',tmpimg);
      }
      else{
        if(this.state==1){
          var s={img:this.cropImg,id:this.cntId}
          this.tmplist.push(s)
        }else{
          this.presetlist.push(this.cropImg)
        }
      }
      this.imgSrc=''
      this.cropImg=''
      this.filename=''

    },
    closeWindow(){
      window.console.log("close itemEdit");
      this.imgSrc=""
      this.$emit('close');
    },
    rotate() {
      // guess what this does :)
      this.$refs.cropper.rotate(90);
    },
    postPreset(){
      let postlist=[]
      const type='image/png'
      for (let i=0;i<this.presetlist.length;i++){
        let bin = atob(this.presetlist[i].replace(/^.*,/, ''));
        let buffer = new Uint8Array(bin.length);
        for (let j = 0; j < bin.length; j++) {
            buffer[j] = bin.charCodeAt(j);
        }
        let image_file = new File([buffer.buffer],this.presetname+i+".png", {type:type});
        postlist.push(image_file)
        this.rev=image_file
        console.log(this.rev)
      }
      let config = {
        headers: {
          'content-type': 'multipart/form-data'
        }
      };
      let URL='http://127.0.0.1:8000/upload/'+this.presetname
      let data = new FormData()
      for (let k=0;k<postlist.length;k++){
        data.append('file'+k,postlist[k])
      }
      data.append('number',postlist.length)
     this.axios
     .post(URL,data,config)
     .then(res => {
       console.log('success')

       this.$emit('close');
     }).catch(error => {
       new Error(error)
       alert('未入力データがあります。')
     })
    }

  }
}
</script>

<style scoped>
  ::-webkit-scrollbar {
      width: 2px;
      height:6px;
  }

  /*スクロールバーの軌道*/
  ::-webkit-scrollbar-track {
    background-color:white;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .1);
  }

  /*スクロールバーの動く部分*/
  ::-webkit-scrollbar-thumb {
    background-color: rgba(0, 0, 50, .5);
    border-radius: 10px;
    box-shadow:0 0 0 1px rgba(255, 255, 255, .3);
  }
:focus{
  outline: none;
}
.filter{
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
}
.upload{
  width:640px;
  height:590px;
  position: relative;
  top: 15px;
  left: calc(50% - 80px);
  transform: translateX(-50%);
  -webkit-transform: translateX(-50%);
  background-color:white;
  border-radius: 10px;
  border: 2px solid black;
  box-shadow: 10px 10px 10px rgba(0,0,0,0.6);
}
.upload-title{
  width:600px;
  margin:15px 0;
  text-align:left;
  padding-left:25px;
}

.upload-input{
  width:250px;
  height:30px;
  background-color:#121212;
  line-height:30px;
}
.upload-label{
  position:absolute;
  top:50%;
  left:50%;
  transform: translateX(-50%) translateY(-50%);
  -webkit-transform: translateX(-50%) translateY(-50%);
}
a{
  font-size:6px;
  color:white;
}
#upload-inputimg{
  display:none;
}
.upload-title h2 {
  font-size: 40px;


}
.upload-trimbutton{
  position:absolute;
  top:400px;
  left:550px;
  width:50px;
  height:30px;
  margin-top:5px;
  padding:2px 5px;
  background-color:#121212;
  color:white;
}
.l_cropper_container {
  width: 500px;
  height: 350px;
  position:absolute;
  top: 80px;
  left: 30px;
  border: 1px solid gray;
}
.presetList{
  position:absolute;
  top:450px;
  height:76px;
  width:570px;
  left:30px;
  display:flex;
  overflow:scroll;
}
.presetList-item{
  position:relative;
}
.item-delete{
  position:absolute;
  top:0;
  right:0;
  width:20px;
  height:20px;
  border-radius:50%;
  background-color:#222222;
}
.upload-presetname{
  position:absolute;
  top:535px;
  left:30px;
  height:20px;
  color:black;
  font-size:20px;
}
.presetname{
  display:flex;
}
.presetname-input{
  height:30px;
  width:140px;
  transition: 0.3s;
  border-bottom:solid 1px #AAAAAA;
  margin-left:10px;
}
.presetname-input:focus{
  border-bottom:solid 1px #222222;
}
.upload-presetbutton{
  position:absolute;
  top:535px;
  left:525px;
  height:30px;
  color:black;
  font-size:20px;
  background-color:#222222;
  padding:0 20px;
}
.upload-presetbutton a{
  line-heihgt:30px;
}
</style>
