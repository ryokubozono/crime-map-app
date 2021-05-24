<template>
  <v-app>
    <core-app-bar />
    <blank-view />
  </v-app>
</template>

<script>
  import CoreAppBar from '@/views/core/AppBar.vue'
  import BlankView from '@/views/core/BlankView.vue'

  export default {
    name: 'BlankIndex',

    components: {
      CoreAppBar,
      BlankView,
    },

    data: () => ({
      expandOnHover: false,
    }),
  }
</script>