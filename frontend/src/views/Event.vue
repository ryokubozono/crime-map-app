<template>
  <div class="event">
    <h1>This is an event page</h1>

    <EventNew @added="getEvents()" />
    <Event v-for="event in events" v-bind:key="event.id" v-bind:event="event" />

  </div>
</template>

<script>
import axios from "axios";
import EventNew from "@/components/eventNew";
import Event from "@/components/event";
import { mapGetters } from "vuex";

export default {
  name: "event",
  computed: {
    ...mapGetters([
      "loggedIn",
    ])
  },
  data() {
    return {
      events: "",
    };
  },
  components: {
    EventNew, Event
  },
  methods: {
    getEvents() {
      axios.get("http://127.0.0.1:8000/api/events/").then(response => this.events = response.data);
    },
  },
  mounted() {
    this.getEvents();
  },
};
</script>
