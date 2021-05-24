<template>
  <v-app>
    <core-app-bar />
    <blog-view />
  </v-app>
</template>

<script>
  import CoreAppBar from '@/views/core/AppBar.vue'
  import BlogView from '@/views/core/BlogView.vue'

  export default {
    name: 'BlogIndex',

    components: {
      CoreAppBar,
      BlogView,
    },

    data: () => ({
      expandOnHover: false,
    }),
  }
</script>