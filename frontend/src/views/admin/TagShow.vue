<template>
  <v-container>
    <v-row>
      <v-col>
        name: {{tag.name}}
      </v-col>
    </v-row>  
    <v-row>
      <v-col>
        is_visible: {{tag.is_visible}}
      </v-col>
    </v-row>  
    <v-row>
      <v-col>
        <v-btn
          color="success"
          v-on:click="$router.push({name: 'tag_edit', params: {tag_id: tag_id}})"
        >
          Edit Tag
        </v-btn>
      </v-col>
    </v-row>  
    <v-row>
      <v-col>
        <v-btn
          v-on:click="$router.push({name: 'tag_all'})"
        >
          back
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12" md="12"
      >
        <v-card>
          <v-card-title>
            Tagged Blog
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
            :items="tag.blogs"
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
  data() {
    return {
      tag: {
        name: "",
        is_visible: false,
      },
      tag_id: '',
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
      ]
    }
  },
  name: "TagShow",
  methods: {
    async get_tag() {
      this.tag_id = this.$route.params['tag_id']
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/get_tag/${this.tag_id}/`)
      .then(res => {
        this.tag = res.data
      })
    },
    onClickEvent(data) {
      this.$router.push({ name: 'blog_show', params: {blog_id: data.id}})
    },
  },
  mounted() {
    this.get_tag()
  }
};
</script>
