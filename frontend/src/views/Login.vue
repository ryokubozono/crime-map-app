<template>
    <v-form
      v-model="valid"
      v-on:submit.prevent="doLogin"
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
        justify="center"
      >
        <v-col
          cols="12"
          md="6"
        >
          <v-text-field
            v-model="user.password" 
            type="password"
            label="password"
            :rules="passwordRules"
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
          Sign In
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
          v-on:click="$router.push({name: 'forget'})"
          text
          class="mx-2"
          color="error"
        >
          Forget Password
        </v-btn>

      </v-row>
    </v-form >
</template>
<script>

import axios from "axios";
import Store from '@/store/index.js'

export default {
  data() {
    return {
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 6) || 'Password must be less than 6 characters',
      ],
      user: {},
      valid: true,
    };
  },
  methods: {
    doLogin() {
      let params = new URLSearchParams();
      params.append('username', `${this.user.userId}`);
      params.append('password', `${this.user.password}`);

      axios.post(
        `${this.$config.fastApiUrl}/api/auth/jwt/login`, params
        )
        .then(response => {
          // console.log(response.data.access_token)
          this.$store.dispatch("auth", {
            userId: this.user.userId,
            userToken: response.data.access_token
          })
          this.$store.dispatch("message", {
            content: "log in",
            type: "success",
            timeout: 3000
          })

          if (this.$route.query.redirect) {
            this.$router.push(this.$route.query.redirect);  
          } else {
            this.$router.push('/user')
          }
        })
        .catch(error => {
          console.log(error)
          this.$store.dispatch("message", {
            content: error,
            type: "error",
            timeout: 3000
          })
        })
        .then(() => {
          axios.get(
            `${this.$config.fastApiUrl}/api/users/me`, {
              headers: {
                "Authorization": `Bearer ${Store.state.auth.userToken}`
              }
            })
            .then(response => {
              console.log(response.data.is_superuser)
            this.$store.dispatch("admin", {
              superUser: response.data.is_superuser,
            });
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