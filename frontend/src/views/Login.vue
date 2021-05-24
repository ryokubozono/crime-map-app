<template>
    <v-form>
      <v-row
        justify="center"
        class="pa-2"
      >
        <v-btn
          v-on:click="signInGoogle"
          class="mx-2"
          color="error"
        >
          Google
        </v-btn>
      </v-row>
    </v-form >
</template>
<script>

import firebase from 'firebase'

export default {
  data() {
    return {
      user: {},
    };
  },
  methods: {
    signInGoogle() {
      const provider = new firebase.auth.GoogleAuthProvider()
      firebase.auth().signInWithPopup(provider)
      .then(response => {
        response.user.getIdToken(true).then(idToken => {
          this.$store.dispatch("auth", {
            user: response.user,
            token: idToken
          })
        })
        .then(() => {
          if (this.$route.query.redirect) {
            this.$router.push(this.$route.query.redirect);  
          } else {
            this.$router.push({name: 'admin_index'})
          }
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
    },
  },
  mounted() {
  },
  watch: {
  },
  computed: {
  }
};
</script>