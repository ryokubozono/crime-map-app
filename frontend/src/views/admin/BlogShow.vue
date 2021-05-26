<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn
          color="success"
          v-on:click="$router.push({name: 'blog_edit', params: {blog_id: blog_id}})"
        >
          edit
        </v-btn>
      </v-col>
    </v-row>  
    <v-row>
      <v-col>
        <v-btn
          v-on:click="$router.push({name: 'blog_all'})"
        >
          back
        </v-btn>
      </v-col>
    </v-row>  

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
          v-on:click="$router.push({name: 'tag_show', params: {tag_id: item.id}})"
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
          class="add-mavon-editor"
          v-model="blog.content" 
          language="en" 
          :subfield="false"
          :editable="false"
          :boxShadow="false"
          :toolbarsFlag="false"
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
  name: "BlogShow",
  data() {
    return {
      items: [],
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

        this.blog.title = res.data.title,
        this.blog.content = res.data.content,
        this.blog.image_url = res.data.image_url,
        res.data.tags.forEach(row => {
          this.blog.tags.push(row)
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
    dummy() {
      console.log('pass')
    },
  },
  computed: {

  },
  mounted() {
    this.get_blog()
  },
};
</script>
