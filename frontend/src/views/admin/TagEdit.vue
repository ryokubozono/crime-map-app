<template>
  <div>
    <v-form
      v-model="valid"
      v-on:submit.prevent="clickUpdate"
      class="pa-2"
      ref="form"
    >
      <v-row>
        <v-col>
          <v-text-field
            v-model="tag.name" 
            label="tag name"
            :rules="nameRules"
            required
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-switch
            v-model="tag.is_visible"
            :label="`is_visible: ${tag.is_visible.toString()}`"
          ></v-switch>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn 
            type="submit"
            :disabled="!valid"
            color="success"
            class="mx-2"
          >
            update
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
            class="mx-2"
            v-on:click="$router.push({name: 'tag_show', params: {tag_id: tag_id}})"
          >
            back
          </v-btn>
        </v-col>
      </v-row>
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
      tag: {
        name: "",
        is_visible: false,
      },
      tag_id: '',
    }
  },
  name: "TagEdit",
  methods: {
    async get_tag() {
      this.tag_id = this.$route.params['tag_id']
      await axios.get(`${process.env.VUE_APP_FAST_API_URL}/api/tags/get_tag/${this.tag_id}/`)
      .then(res => {
        this.tag = res.data
      })
    },
    async clickUpdate() {
      await axios.patch(`${process.env.VUE_APP_FAST_API_URL}/api/tags/update_tag/${this.tag_id}/`, {
        name: this.tag.name,
        is_visible: this.tag.is_visible,
      },
      {
        headers: {
          "Authorization": `Bearer ${this.$store.state.auth.token}`
        }
      })
      .then(res => {
        this.$store.dispatch("message", {
          content: "updated",
          type: "success",
          timeout: 3000
        })
        this.$router.push({name: 'tag_show', params: {tag_id: res.data.id}})
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
    this.get_tag()
  }
};
</script>
