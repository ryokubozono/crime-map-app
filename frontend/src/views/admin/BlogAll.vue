<template>
  <v-container>
    <v-row>
      <v-col
        cols="12" md="12"
      >
        <v-card>
          <v-card-title>
            All Blog
            <v-spacer></v-spacer>
            <v-text-field
              v-model="blogSearch"
              append-icon="mdi-magnify"
              label="Blog Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :headers="blogHeaders"
            :items="blogs"
            item-key="id"
            class="elevation-1"
            :search="blogSearch"
            @click:row="onClickEvent" 
          >
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import axios from "axios";

export default {
  name: "BlogAll",
  data() {
    return {
      blogs: [],
      blogSearch: "",
      blogHeaders: [
        {
          text: 'id',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        {
          text: 'title',
          align: 'start',
          sortable: false,
          value: 'title',
        },
        {
          text: 'is_visible',
          align: 'start',
          sortable: false,
          value: 'is_visible',
        },
        {
          text: 'tags',
          align: 'start',
          sortable: false,
          value: 'tags.length',
        },
        {
          text: 'create',
          align: 'start',
          sortable: false,
          value: 'created_at',
        },
        {
          text: 'update',
          align: 'start',
          sortable: false,
          value: 'updated_at',
        },
      ]
    }
  },
  methods: {
    async get_blog_all() {
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/blogs/all/`
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
    onClickEvent(data) {
      this.$router.push({ name: 'blog_show', params: {blog_id: data.id}})
    },
  },
  computed: {
  },
  mounted() {
    this.get_blog_all()
  }
};
</script>
