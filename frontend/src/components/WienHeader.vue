<template>
<div class="header">
  <div class="navbar">
    <h5>Wien</h5>
  </div>
</div>
</template>

<script>
export default {
  name:'WienHeader',
  data(){
    return{
    }
  },
}
</script>

<style scoped>
:focus{
  outline: none;
}

.header{
  width: 100%;
  height: 40px;
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
</style>
