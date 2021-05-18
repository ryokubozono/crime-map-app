<template>
  <div>
    <v-form
      ref="form"
    >
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-file-input
            show-size
            v-model="image"
          ></v-file-input>
        </v-col>
        <v-col
          cols="12"
          sm="6"
        >
          <v-btn
            v-on:click="upload_image()"
          >
            upload
          </v-btn>     
        </v-col>
      </v-row>
    </v-form>
    <v-row>
      <v-col
        cols="12"
        sm="6"
      >
        <v-img
          v-if="blog.image_url"
          max-height="150"
          max-width="250"
          :src="blog.image_url"
        ></v-img>
      </v-col>
    </v-row>
    
    <v-form>
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Title"
            placeholder="Title"
            v-model="blog.title"
            outlined
          ></v-text-field>
        </v-col>
      </v-row>

      <mavon-editor 
        :toolbars="$config.markdownOption" 
        v-model="blog.content" 
        language="en" 
        ref="md"
        @imgAdd="imgAdd"
      />

      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-select
            v-model="blog.tags"
            :items="tags"
            item-text="name"
            item-value="id"
            label="Select"
            multiple
            chips
            hint="What are the target regions"
            persistent-hint
          ></v-select>
        </v-col>
      </v-row>
    </v-form>
    <v-btn
      v-on:click="create_blog()"
    >
      create
    </v-btn>
    {{blog}}
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "BlogNew",
  data() {
    return {
      blog: {
        content: "#### how to use mavonEditor in nuxt.js",
        title: "",
        tags: [],
        image_url: "",
      },
      tags: [],
      image: null,
    }
  },
  methods: {
    upload_image() {
        var formdata = new FormData();
        formdata.append('image', this.image);
        axios.post(`${process.env.VUE_APP_FAST_API_URL}/api/files/uploadfile/`, 
        formdata,
        {
          headers: { 
            'Content-Type': 'multipart/form-data',
          },
        }
        ).then(url => {
          this.$refs.form.reset()
          this.blog.image_url = url.data.filepath
        })
    },
    imgAdd(pos, $file){
        var formdata = new FormData();
        formdata.append('image', $file);
        axios.post(`${process.env.VUE_APP_FAST_API_URL}/api/files/uploadfile/`, 
        formdata,
        {
          headers: { 
            'Content-Type': 'multipart/form-data',
          },
        }
        ).then(url => {
          console.log(url)
          this.$refs.md.$img2Url(pos, url.data.filepath);
        })
    },
    async get_tags() {
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/`)
      .then(res => res.data.forEach(row => {
        this.tags.push({
          id: row.id,
          name: row.name,
        })
      }))
    },
    async create_blog() {
      await axios.post(`${process.env.VUE_APP_FAST_API_URL}/api/blogs/`, {
        content: this.blog.content,
        title: this.blog.title,
        tags: this.blog.tags,
        image_url: this.blog.image_url,
      })
      .then(res => {
        this.$router.push({name: 'blog_edit', params: { blog_id: `${res.data.id}` }})
      })
    }
  },
  mounted() {
    this.get_tags()
  }
};
</script>
