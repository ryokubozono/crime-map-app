
<template>
  <v-main>

    <v-container
      class="pa-10"
      id="message"
    >
      <core-message />
    </v-container>
<v-container fluid>

            <router-view />
            </v-container>
          <core-footer />




  </v-main>

</template>

<script>
  import CoreMessage from '@/views/core/Message.vue'

  export default {

    name: 'AdminView',
    data: () => ({
    }),
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