<template>
  <v-app>
    <blog-drawer />
    <blog-right-drawer />
    <core-app-bar />
    <blog-view />
  </v-app>
</template>

<script>
  import CoreAppBar from '@/views/core/AppBar.vue'
  import BlogView from '@/views/core/BlogView.vue'
  import BlogDrawer from '@/views/core/BlogDrawer.vue'
  import BlogRightDrawer from '@/views/core/BlogRightDrawer.vue'

  export default {
    name: 'BlogShowIndex',

    components: {
      CoreAppBar,
      BlogView,
      BlogDrawer,
      BlogRightDrawer,
    },

    data: () => ({
      expandOnHover: false,
    }),
  }
</script>