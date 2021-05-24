<template>
  <v-container>
    <v-row>
      <v-col>    
        Google Accout: {{$store.state.auth.user.email}}
      </v-col>    
    </v-row> 
    <v-row>
      <v-col>    
        <v-btn
          v-on:click="doLogout"
        >
          logout
        </v-btn>
      </v-col>    
    </v-row>
  </v-container>
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
