<template>
  <div>
    {{blogs}}
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
