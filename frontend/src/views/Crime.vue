<template>
  <div class="crime">
    <h1>This is an crime page</h1>

    <Crime v-for="crime in crimes" v-bind:key="crime.id" v-bind:crime="crime" />

  </div>
</template>

<script>
import axios from "axios";
import Crime from "@/components/crime";
// import { mapGetters } from "vuex";

export default {
  name: "crime",
  data() {
    return {
      crimes: "",
    };
  },
  components: {
    Crime
  },
  methods: {
    getCrimes() {
      axios.get("http://127.0.0.1:8000/api/crimes/").then(response => this.crimes = response.data);
    },
  },
  mounted() {
    this.getCrimes();
  },
};
</script>
