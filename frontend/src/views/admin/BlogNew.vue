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
            color="success"
            :disabled="!image"
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
    
    <v-form
      v-model="valid"
    >
      <v-row>
        <v-col
          cols="12"
          sm="6"
        >
          <v-text-field
            label="Title"
            placeholder="Title"
            v-model="blog.title"
            :rules="titleRules"
            required
            outlined
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          class="mavon-editor"
        >
          <mavon-editor 
            :toolbars="$config.markdownOption" 
            v-model="blog.content" 
            language="en" 
            ref="md"
            @imgAdd="imgAdd"
          />
        </v-col>
      </v-row>
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
      <v-row>
        <v-col>
          <v-switch
            v-model="blog.is_visible"
            :label="`is_visible: ${blog.is_visible.toString()}`"
          ></v-switch>
        </v-col>
      </v-row>
    </v-form>
    <v-btn
      v-on:click="create_blog()"
      :disabled="!valid || !blog.content"
      color="success"
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
      titleRules: [
        v => !!v || 'Password is required',
      ],
      blog: {
        content: "#### how to use mavonEditor in nuxt.js",
        title: "",
        tags: [],
        image_url: "",
        is_visible: false,
      },
      tags: [],
      image: null,
      valid: true,
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
            "Authorization": `Bearer ${this.$store.state.auth.token}`
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
            "Authorization": `Bearer ${this.$store.state.auth.token}`
          },
        }
        ).then(url => {
          console.log(url)
          this.$refs.md.$img2Url(pos, url.data.filepath);
        })
    },
    async get_tags() {
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/visible/`)
      .then(res => res.data.forEach(row => {
        this.tags.push({
          id: row.id,
          name: row.name,
        })
      }))
    },
    async create_blog() {
      await axios.post(`${process.env.VUE_APP_FAST_API_URL}/api/blogs/create_blog/`, {
        content: this.blog.content,
        title: this.blog.title,
        tags: this.blog.tags,
        image_url: this.blog.image_url,
        is_visible: this.blog.is_visible,
      },
      {
        headers: {
          "Authorization": `Bearer ${this.$store.state.auth.token}`,
        }
      })
      .then(res => {
        this.$store.dispatch("message", {
          content: "updated",
          type: "success",
          timeout: 3000
        })
        this.$router.push({name: 'blog_show', params: { blog_id: res.data.id }})
      })
      .catch(error => {
        console.log(error)
        this.$store.dispatch("message", {
          content: error,
          type: "error",
          timeout: 3000
        })
      })
    }
  },
  mounted() {
    this.get_tags()
  }
};
</script>
