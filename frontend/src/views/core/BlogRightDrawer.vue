<template>
  <v-navigation-drawer
    app
    mobile-breakpoint="960"
    clipped
    right
  >
    <v-list
      dense
    >
      <v-list-item-group
        active-class="deep-purple--text text--accent-4"
      >
        <v-list color="transparent">
          <v-list-item
            v-for="item in items"
            :key="item.to"
            :href="item.to"
          >
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
import axios from "axios";

export default {
  name: 'BlogRightDrawer',
  data: () => ({
    items: [],
    blog_id: '',
    blog: {
      content: "",
      title: "",
      tags: [],
      image_url: "",
    },
  }),
  methods: {
    async get_blog() {
      this.blog_id = this.$route.params['blog_id']
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/blogs/get_blog/${this.blog_id}/`
      )
      .then(res => {

        this.blog.title = res.data.title,
        this.blog.content = res.data.content,
        this.blog.image_url = res.data.image_url,
        res.data.tags.forEach(row => {
          this.blog.tags.push(row)
        })
        let lines = res.data.content.split(/\r?\n/);

        lines.forEach(line => {
          if (line.slice( 0, 1 ) == '#' && line.slice(-2) == 'a>') {
            
            this.items.push({
              label: line.match(/\[(.+)\]/)[1],
              to: line.match(/\((.+)\)/)[1],
            })
          }
        })
      })
    },
  },
  mounted() {
    this.get_blog()
  },
  
}
</script>
