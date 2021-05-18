<template>
  <div>
    <v-form
      v-model="valid"
      v-on:submit.prevent="clickCreate"
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
        Create
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
    }
  },
  name: "TagNew",
  methods: {
    async clickCreate() {
      await axios.post(`${process.env.VUE_APP_FAST_API_URL}/api/tags/`, {
        name: this.tag.name
      })
    }
  }
};
</script>
