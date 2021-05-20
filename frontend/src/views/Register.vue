<template>
    <v-form
      v-model="valid"
      v-on:submit.prevent="doRegister"
      ref="form"
    >
      <v-row
        justify="center"
      >
        <v-col
          cols="12"
          md="6"
        >
          <v-text-field
            v-model="user.displayName" 
            label="displayName"
            :rules="displayNameRules"
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
        justify="center"
      >
        <v-col
          cols="12"
          md="6"
        >
          <v-text-field
            v-model="user.passwordConf" 
            type="password"
            label="password(confirm)"
            :rules="passwordConfRules"
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
          Register
        </v-btn>
      </v-row>
      <v-row
        justify="center"
        class="pa-2"
      >

        <v-btn
          v-on:click="$router.push({name: 'login'})"
          text
          class="mx-2"
          color="primary"
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
      displayNameRules: [
        v => !!v || 'displayName is required',
      ],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 6) || 'Password must be less than 6 characters',
        v => (this.user.passwordConf.length) && ((this.user.passwordConf === v) || 'password must match')
      ],
      passwordConfRules: [
        v => !!v || 'Password(confirm) is required',
        v => (v && v.length >= 6) || 'Password must be less than 6 characters',
        v => (this.user.password.length) && ((this.user.password === v) || 'password must match')
      ],
      user: {},
      valid: true,
    };
  },
  methods: {
    doRegister() {
      axios.post(
        `${this.$config.fastApiUrl}/api/auth/register`, {
          display_name: `${this.user.displayName}`,
          email: `${this.user.userId}`,
          password: `${this.user.password}`
        }
      )
      .then(() => {
        this.$store.dispatch("message", {
          content: "Registerd",
          type: "success",
          timeout: 3000
        })
        // this.$refs.form.reset()
        // this.$router.push({name: 'Login'})
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
          this.$store.dispatch("admin", {
            superUser: false,
          });
          this.$router.push({name: 'User'})
        })
        .catch(error => {
          console.log(error)
          this.$store.dispatch("message", {
            content: error,
            type: "error",
            timeout: 3000
          })
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