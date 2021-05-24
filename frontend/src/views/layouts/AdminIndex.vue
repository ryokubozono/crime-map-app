<template>
  <v-app>
    <admin-drawer />
    <core-app-bar />
    <admin-view />
  </v-app>
</template>

<script>
  import CoreAppBar from '@/views/core/AppBar.vue'
  import AdminView from '@/views/core/AdminView.vue'
  import AdminDrawer from '../core/AdminDrawer.vue'

  export default {
    name: 'AdminIndex',

    components: {
      CoreAppBar,
      AdminView,
      AdminDrawer,
    },

    data: () => ({
      expandOnHover: false,
    }),
  }
</script>