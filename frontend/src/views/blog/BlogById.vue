<template>
  <v-container>
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
        content: "",
        title: "",
        tags: [],
        image_url: "",
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
        this.blog.title = res.data.title,
        this.blog.content = res.data.content,
        this.blog.image_url = res.data.image_url,
        res.data.tags.forEach(row => {
          this.blog.tags.push(row.id)
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
    this.get_blog()
  }
};
</script>
