<template>
<div class="filter" @click.self="closeWindow">
  <div class="result" >
    <div class="result-title">
      <h2>Result.</h2>
    </div>
    <div class="" id="resultscreen" >

    </div>
  </div>
</div>
</template>

<script>
export default {
  props:[],
  data () {
    return {
    }
  },
  methods: {
    closeWindow(){
      console.log("close itemEdit");
      this.$emit('close');
    },
  },
}
</script>

<style scoped>
.filter{
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
}
.result{
  padding:10px 10px;
  position: relative;
  top: 40px;
  left: 50%;
  transform: translateX(-50%);
  -webkit-transform: translateX(-50%);
  background-color:white;
  border-radius: 10px;
  border: 2px solid black;
  box-shadow: 10px 10px 10px rgba(0,0,0,0.6);
}
.result-title{
  text-align:left;
  padding-left:25px;
}
</style>
