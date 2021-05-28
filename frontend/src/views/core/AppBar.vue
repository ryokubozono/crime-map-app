<template>
  <v-app-bar
    app
    color="red"
    clipped-left
    clipped-right
    :absolute="$vuetify.breakpoint.sm || $vuetify.breakpoint.xs"
  >

    <v-toolbar-title
      class="hidden-sm-and-down font-weight-light"
      v-text="'Crime Map'"
    />

    <v-spacer />

    <v-btn
      text
      v-on:click="$router.push({name: 'blog_visible'})"
    >
      blog
    </v-btn>
    <v-btn
      text
      v-on:click="$router.push({name: 'tag_visible'})"
    >
      tag
    </v-btn>

    <v-btn
      text
      v-on:click="$router.push({name: 'admin_index'})"
      v-if="$store.state.auth.token"
    >
      admin
    </v-btn>

    <v-spacer />

  </v-app-bar>
</template>

<script>


  export default {
    name: 'CoreAppBar',

    components: {
    },
    props: {
    },
    data: () => ({
    }),
    computed: {
    },
    methods: {
    },
  }
</script>
