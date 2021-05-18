<template>
  <div>
    <v-form
      v-model="valid"
      v-on:submit.prevent="clickUpdate"
      class="pa-2"
      ref="form"
    >
      <v-text-field
        v-model="tag.name" 
        label="tag name"
        :rules="nameRules"
        required
      />
      <v-btn 
        type="submit"
        :disabled="!valid"
        color="primary"
        class="mx-2"
      >
        update
      </v-btn>
    </v-form >
  </div>
</template>

<script>

import axios from "axios";

export default {
  data() {
    return {
      nameRules: [
        v => !!v || 'tag name is required',
      ],
      tag: {},
      tag_id: '',
    }
  },
  name: "TagEdit",
  methods: {
    async get_tag() {
      this.tag_id = this.$route.params['tag_id']
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/${this.tag_id}`)
      .then(res => {
        this.tag = res.data
      })
    },
    async clickUpdate() {
      await axios.patch(`${process.env.VUE_APP_FAST_API_URL}/api/tags/${this.tag_id}`, {
        name: this.tag.name
      })
      .then(() => {
        this.tag = {},
        this.get_tag()
      })
    }
  },
  mounted() {
    this.get_tag()
  }
};
</script>
