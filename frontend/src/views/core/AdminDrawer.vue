
<template>

            <v-navigation-drawer
              app
              v-model="drawer"
              mobile-breakpoint="960"
              clipped

            >
              <v-list
                nav
                dense
              >
                <v-list-item-group
                  v-model="group"
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

    name: 'AdminDrawer',
    data: () => ({
      items: [
        {
          label: 'user',
          to: 'user',
          icon: 'mdi-image-edit',
        },
        {
          label: 'add tag',
          to: 'tag_new',
          icon: 'mdi-image-edit',
        },
        {
          label: 'all tag',
          to: 'tag_all',
          icon: 'mdi-image-edit',
        },
        {
          label: 'add blog',
          to: 'blog_new',
          icon: 'mdi-image-edit',
        },
        {
          label: 'all blog',
          to: 'blog_all',
          icon: 'mdi-image-edit',
        },
      ],
      drawer: true,
    }),
  }
</script>
