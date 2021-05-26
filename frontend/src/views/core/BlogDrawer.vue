
<template>
  <v-navigation-drawer
    app
    mobile-breakpoint="960"
    clipped
  >
    <v-list
      nav
      dense
    >
      <v-list-item-group
        active-class="deep-purple--text text--accent-4"
      >
        <v-list color="transparent">
          <v-list-item
            v-for="item in items"
            :key="item.to"
            link
            v-on:click="$router.push({name: item.to})"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>
                {{item.label}}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script>

  export default {

    name: 'BlogDrawer',
    data: () => ({
      items: [
        {
          label: 'Blogs',
          to: 'blog_visible',
          icon: 'mdi-image-edit',
        },
        {
          label: 'Tags',
          to: 'tag_visible',
          icon: 'mdi-image-edit',
        },
      ],
    }),
  }
</script>
