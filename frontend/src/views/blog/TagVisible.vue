<template>
  <v-container>
    <v-row
      justify="start"  
    >
      <v-col>
        <v-chip
          v-for="item in tags"
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
  </v-container>
</template>

<script>

import axios from "axios";

export default {
  name: "TagVisible",
  data() {
    return {
      tags: [],
    }
  },
  methods: {
    async get_tags_all() {
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/visible/`,
      )
      .then(res => {
        this.tags = res.data
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
    this.get_tags_all()
  }
};
</script>
