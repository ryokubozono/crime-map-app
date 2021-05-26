<template>
  <div>
    <v-chip
        label
        text-color="black"
        class="ma-2"
    >
        <v-icon left>
        mdi-label
        </v-icon>
        {{ tag.name }}
    </v-chip>
    <v-row>
      <v-col
          v-for="blog in tag.blogs"
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
      tag: {},
      tag_id: '',
    }
  },
  methods: {
    async get_tag() {
      this.tag_id = this.$route.params['tag_id']
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/get_tag/${this.tag_id}/`)
      .then(res => {
        this.tag = res.data
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
    this.get_tag()
  }
};
</script>
