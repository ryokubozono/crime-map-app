

<template>
  <v-alert :type="type" v-show="message">
    {{ message }}
  </v-alert>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
    name: 'CoreMessage',
    computed: {
      ...mapState({
        message: state => state.message.content,
        type: state => state.message.type
      })
    },
    watch: {
      
    }
  }
</script>