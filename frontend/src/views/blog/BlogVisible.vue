<template>
  <div>

    <v-row>
      <v-col
          v-for="blog in blogs"
          sm="6"
          md="4"
          v-bind:key="blog.title"
      >

        <v-card
          class="mx-auto"
          max-width="344"
          v-on:click="$router.push({name: 'blog_by_id', params: {blog_id: blog.id}})"
        >
          <v-img
            v-if="blog.image_url"
            height="200px"
            :src="blog.image_url"
          ></v-img>
          <v-card-title>
            {{blog.title}}
          </v-card-title>
          <v-card-actions>
            <v-chip
              v-for="item in blog.tags"
              :key="item.name"  
              label
              text-color="black"
              class="ma-2"
              v-on:click="$router.push({name: 'blogs_tag', params: {tag_id: item.id}})"
            >
              <v-icon left>
                mdi-label
              </v-icon>
              {{ item.name }}
            </v-chip>
          </v-card-actions>
        </v-card>

      </v-col>
    </v-row>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "BlogVisible",
  data() {
    return {
      blogs: [],
    }
  },
  methods: {
    async get_blog_all() {
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/blogs/visible/`
      )
      .then(res => {
        res.data.forEach(blog => {
          this.blogs.push(blog)
        })
      })
      .catch(error => {
        console.log(error)
        this.$store.dispatch("message", {
          content: error,
          type: "error",
          timeout: 3000
        })
      })
    },
  },
  computed: {
  },
  mounted() {
    this.get_blog_all()
  }
};
</script>
