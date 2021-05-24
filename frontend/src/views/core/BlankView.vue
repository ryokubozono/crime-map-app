
<template>
  <v-main>
    <v-container
      class="pa-10"
      id="message"
    >
      <core-message />
    </v-container>
    
    <v-container
      class="pa-8"
    >
      <v-row>

        <v-col
          cols="12"
        >
          <router-view />
        </v-col>

      </v-row>

      <v-row>
        <v-col
          cols="12"
        >
          <core-footer />
        </v-col>
      </v-row>

    </v-container>

  </v-main>
</template>

<script>
  import CoreMessage from '@/views/core/Message.vue'

  export default {
    name: 'BlankView',

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