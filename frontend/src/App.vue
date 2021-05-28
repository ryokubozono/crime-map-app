<template>
  <router-view/>
</template>

<script>

import 'mavon-editor/dist/css/index.css';

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style>
.mavon-editor{
  z-index: 1;
}
.add-mavon-editor{
  border: solid 0px;
}
:target:before {
    content: "";
    display: block;
    height: 100px;
    margin: -100px 0 0;
}
html {
    scroll-behavior: smooth;
}
</style>