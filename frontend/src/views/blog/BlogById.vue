<template>
  <v-container>

    <v-row
      justify="start"  
    >
      <v-col>
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
      </v-col>
    </v-row> 

    <v-row>
      <v-col
        class="mavon-editor"
      >
        <mavon-editor 
          v-model="blog.content" 
          language="en" 
          :subfield="false"
          :editable="false"
          :toolbarsFlag="false"
          :boxShadow="false"
          defaultOpen="preview"
          previewBackground="#fff"
          :imageClick="dummy"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import axios from "axios";

export default {
  name: "BlogById",
  data() {
    return {
      blog_id: '',
      blog: {
      },
    }
  },
  methods: {
    async get_blog() {
      this.blog_id = this.$route.params['blog_id']
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/blogs/get_blog/${this.blog_id}/`
      )
      .then(res => {
        if (res.data == null || res.data.is_visible == false) {
          this.$router.push({name: 'not_found'})
        }
        this.blog = res.data
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
    dummy() {
      console.log('pass')
    },
  },
  computed: {
  },
  mounted() {
    this.get_blog()
  }
};
</script>
