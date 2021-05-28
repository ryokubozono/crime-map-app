<template>
<div>
  <v-main>
    <v-container
      class="pa-10"
      id="message"
    >
      <core-message />
    </v-container>

      <router-view />

  </v-main>
  <core-footer />
</div>
</template>

<script>
  import CoreMessage from '@/views/core/Message.vue'

  export default {
    name: 'BlogView',

    components: {
      CoreMessage,
      CoreFooter: () => import('./Footer'),
    },
  }
</script>

<style lang="css">
#message{
  position: fixed;
  bottom: -20px;
  z-index: 999;
}
</style>