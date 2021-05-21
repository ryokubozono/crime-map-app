<template>
  <div class="user">
    <h1>This is an user page</h1>
    <v-btn
        v-on:click="doLogout"
    >
      logout
    </v-btn>
  </div>
</template>

<script>

import firebase from 'firebase'

export default {
  name: "user",
  methods: {
    doLogout() {
      firebase.auth().signOut()
      this.$store.dispatch("auth", {
        user: '',
        token: ''
      })
      this.$store.dispatch("message", {
        content: "log out",
        type: "success",
        timeout: 3000
      })
      this.$router.push({name: 'login'});
    },
  }
};
</script>
