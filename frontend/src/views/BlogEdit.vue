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
      <v-text-field
        label="Title"
        placeholder="Title"
        v-model="blog.title"
        outlined
      ></v-text-field>
    </v-form>
    <mavon-editor :toolbars="$config.markdownOption" v-model="blog.content" language="en" />
    <v-form>
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
      v-on:click="update_blog()"
    >
      update
    </v-btn>
    {{blog}}
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "TestId",
  data() {
    return {
      blog_id: '',
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
    async get_tags() {
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/`)
      .then(res => res.data.forEach(row => {
        this.tags.push({
          id: row.id,
          name: row.name,
        })
      }))
    },
    async get_blog() {
      this.blog_id = this.$route.params['blog_id']
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/blogs/${this.blog_id}`
      )
      .then(res => {
        this.blog.title = res.data.title,
        this.blog.content = res.data.content,
        this.blog.image_url = res.data.image_url,
        res.data.tags.forEach(row => {
          this.blog.tags.push(row.id)
        })
      })
    },
    async update_blog() {
      await axios.patch(`${process.env.VUE_APP_FAST_API_URL}/api/blogs/${this.blog_id}`, {
        content: this.blog.content,
        title: this.blog.title,
        tags: this.blog.tags,
        image_url: this.blog.image_url,
      })
      .then(() => {
        this.blog.tags = []
        this.get_blog()
      })
    }
  },
  mounted() {
    this.get_blog()
    this.get_tags()
  }
};
</script>
