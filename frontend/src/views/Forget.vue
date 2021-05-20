<template>
    <v-form
      v-model="valid"
      v-on:submit.prevent="doSend"
    >
      <v-row
        justify="center"
      >
        <v-col
          cols="12"
          md="6"
        >
          <v-text-field
            v-model="user.userId" 
            label="email"
            :rules="emailRules"
            required
          />
        </v-col>
      </v-row>
      
      <v-row
        align="center"
        justify="space-around"
        class="pa-2"
      >
        <v-btn 
          color="success"
          type="submit"
          :disabled="!valid"
        >
          send mail
        </v-btn>
      </v-row>
      <v-row
        justify="center"
        class="pa-2"
      >

        <v-btn
          v-on:click="$router.push({name: 'register'})"
          text
          class="mx-2"
          color="primary"
        >
          Register
        </v-btn>
        <v-btn
          v-on:click="$router.push({name: 'login'})"
          text
          class="mx-2"
          color="success"
        >
          Login
        </v-btn>

      </v-row>
    </v-form >
</template>
<script>

import axios from "axios";

export default {
  data() {
    return {
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      user: {},
      valid: true,
    };
  },
  methods: {
    doSend() {
      axios.post(
        `${this.$config.fastApiUrl}/api/auth/forgot-password`, {
          email: `${this.user.userId}`
        }
      )
      .then(() => {
        this.$store.dispatch("message", {
          content: "send",
          type: "success",
          timeout: 3000
        })
        this.$router.push({name: 'Login'})
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
  },
  watch: {
  },
  computed: {
  }
};
</script>