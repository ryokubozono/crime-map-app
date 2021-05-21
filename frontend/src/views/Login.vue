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

import firebase from 'firebase'

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
      firebase.auth().signInWithEmailAndPassword(this.user.userId, this.user.password)
      .then(response => {
        response.user.getIdToken(true).then(idToken => {
          this.$store.dispatch("auth", {
            user: response.user,
            token: idToken
          })
        })
        console.log(this.$store.state.auth)
        let user = firebase.auth().currentUser
        console.log(user)
        user.getIdTokenResult(true).then(token => {
          console.log(token)
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
      .then(() => {
        this.$router.push({name: 'user'})
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