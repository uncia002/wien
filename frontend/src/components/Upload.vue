<template>
<div class="filter" @click.self="closeWindow">
  <div class="upload">
    <div class="upload-title">
      <h2>Edit.</h2>
    </div>

    <input  type="file" name="image" accept="image/*"   @change="setImage" id="upload-inputimg" >
    <label v-if="imgSrc==''" class="upload-label" for="upload-inputimg"><div class="upload-input">
      <a>追加 / トリミングする画像をアップロード</a>
    </div></label>
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
      <div  @click="cropImage" v-if="imgSrc !== ''" class="upload-trimbutton">
        <a> Push</a>
      </div>
    </div>
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
  props:["tmplist","changeimgstatus"],
  data () {
    return {
      targetWidth: 1,
      targetHeight: 1,
      imgSrc: '',
      cropImg:'',
      cntId:13,
    }
  },
  methods: {
    setImage (event) {
      const file = event.target.files[0];
      if (!file.type.includes('image/')) {
        alert('Please select an image file');
        return;
      }
      if (typeof FileReader === 'function') {
        const reader = new FileReader();
        reader.onload = event => {
          this.imgSrc = event.target.result
          //
          //this.$refs.cropper.replace(event.target.result);
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
        this.imgSrc=''
        this.cropImg=''
        this.filename=''
        this.$emit('changeImg',tmpimg);
      }
      else{
        var s={img:this.cropImg,id:this.cntId}
        this.cntId++
        this.tmplist.push(s)
        this.imgSrc=''
        this.cropImg=''
        this.filename=''
      }

    },
    closeWindow(){
      window.console.log("close itemEdit");
      this.$emit('close');
    },
    rotate() {
      // guess what this does :)
      this.$refs.cropper.rotate(90);
    }
  }
}
</script>

<style scoped>
.filter{
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
}
.upload{
  width:600px;
  height:500px;
  position: relative;
  top: 40px;
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
</style>
