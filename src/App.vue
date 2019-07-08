<template>
  <div class="app" >
    <Form></Form>
  </div>
</template>

<script>
import Form from './components/Form.vue'

export default {
  name: 'app',
  components: {
    Form
  }
}
</script>
<style scoped>
.app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  align-content: center;
  justify-content: center;
  vertical-align: middle;
  display: flex;
  height: 100vh;
  background: #454545;
  background-image: url('Blur-2.png')
}
</style>
<style>
</style>
