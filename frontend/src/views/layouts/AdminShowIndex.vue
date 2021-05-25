<template>
  <v-app>
    <admin-drawer />
    <blog-right-drawer />
    <core-app-bar />
    <admin-view />
  </v-app>
</template>

<script>
  import CoreAppBar from '@/views/core/AppBar.vue'
  import AdminView from '@/views/core/AdminView.vue'
  import AdminDrawer from '@/views//core/AdminDrawer.vue'
  import BlogRightDrawer from '@/views//core/BlogRightDrawer.vue'

  export default {
    name: 'AdminShowIndex',

    components: {
      CoreAppBar,
      AdminView,
      AdminDrawer,
      BlogRightDrawer,
    },

    data: () => ({
      expandOnHover: false,
    }),
  }
</script>