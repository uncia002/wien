<template>
<div class="header">
  <div class="navbar">
  </div>
  <div class="editbar">

    <div class="editbar-button">
      <a>hjkhkjhk</a>
    </div>

  </div>
</div>
</template>

<script>
export default {
  name:'WienHeader',
}
</script>

<style scoped>
.header{
  width: 100%;
  height: 80px;
  position:fixed;
  display: flex;
  color: white;
  background-color: #111111;
}
.navbar{
  width: 100%;
  height: 40px;
  position: absolute;
  display: flex;
}
.editbar{
  width: 100%;
  height: 40px;
  padding: 0 10px;
  top: 40px;
  position: absolute;
  display: flex;
}
.editbar-button{
  height: 24px;
  margin: 7px;
  border: solid 1px white;
  border-radius: 5px;
}
.editbar-button a{
  padding: 0 14px;
  line-height: 24px;
}
</style>
