<template>
  <v-app>
    <blog-drawer />
    <core-app-bar />
    <blog-view />
  </v-app>
</template>

<script>
  import CoreAppBar from '@/views/core/AppBar.vue'
  import BlogView from '@/views/core/BlogView.vue'
  import BlogDrawer from '@/views/core/BlogDrawer.vue'

  export default {
    name: 'BlogIndex',

    components: {
      CoreAppBar,
      BlogView,
      BlogDrawer,
    },

    data: () => ({
      expandOnHover: false,
    }),
  }
</script>