<template>
  <v-container>
    <v-row>
      <v-col
        cols="12" md="12"
      >
        <v-card>
          <v-card-title>
            All Tag
            <v-spacer></v-spacer>
            <v-text-field
              v-model="tagSearch"
              append-icon="mdi-magnify"
              label="Tag Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-data-table
            :headers="tagHeaders"
            :items="tags"
            item-key="id"
            class="elevation-1"
            :search="tagSearch"
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
  name: "TagAll",
  data() {
    return {
      tags: [],
      tagSearch: "",
      tagHeaders: [
        {
          text: 'id',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        {
          text: 'name',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        {
          text: 'is_visible',
          align: 'start',
          sortable: false,
          value: 'is_visible',
        },
        {
          text: 'blogs',
          align: 'start',
          sortable: false,
          value: 'blogs.length',
        },
      ]
    }
  },
  methods: {
    async get_tags_all() {
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/all/`,
      {
        headers: {
          "Authorization": `Bearer ${this.$store.state.auth.token}`,
        }
      }
      )
      .then(res => {
        res.data.forEach(tag => {
          this.tags.push(tag)
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
      this.$router.push({ name: 'tag_show', params: {tag_id: data.id}})
    },
  },
  computed: {
  },
  mounted() {
    this.get_tags_all()
  }
};
</script>
