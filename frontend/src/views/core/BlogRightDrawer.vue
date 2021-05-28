<template>
  <v-navigation-drawer
    app
    mobile-breakpoint="960"
    clipped
    right
  >
    <blog-index-list />
  </v-navigation-drawer>
</template>

<script>
import BlogIndexList from "@/views/core/BlogIndexList";

export default {
  name: 'BlogRightDrawer',
  components: {
    BlogIndexList
  }
  
}
</script>
