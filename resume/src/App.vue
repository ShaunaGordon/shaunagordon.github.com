<template>
  <div id="app">
    <header-section></header-section>
    <skills-section></skills-section>
  </div>
</template>

<script>
import HeaderSection from './components/sections/Header.vue'
import SkillsSection from './components/sections/Skills.vue'

export default {
  name: 'app',
  components: {
    HeaderSection,
    SkillsSection
  }
}
</script>

<style>
body {
    background-color: beige;
}
#app {
  font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h2 {
    font-size: 4rem;
}
</style>
