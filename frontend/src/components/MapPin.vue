<template>

  <div>

    <l-map
      :zoom="zoom"
      :center="center"
      style="height: 500px; width: 100%"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <!-- Use default icon -->

      <l-marker :lat-lng="[35.681, 139.763]" />

      <l-marker v-for="crime in crimes" v-bind:key="crime.id" v-bind:crime="crime" :lat-lng="[crime.fy, crime.fx]" />

    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";
import { latLng } from "leaflet";
import axios from "axios";

export default {
  name: "Icon",
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      zoom: 13,
      center: latLng(35.681, 139.763),
      url: 'https://tile.mierune.co.jp/mierune/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',

      staticAnchor: [16, 37],
      customText: "Foobar",
      iconSize: 64, 
      crimes: "",
    };
  },
  computed: {
    dynamicSize() {
      return [this.iconSize, this.iconSize * 1.15];
    },
    dynamicAnchor() {
      return [this.iconSize / 2, this.iconSize * 1.15];
    }
  },
  methods: {
    getCrimes() {
      axios.get("http://127.0.0.1:8000/api/crimes/?skip=0&limit=1000").then(response => this.crimes = response.data);
    },
  },
  mounted() {
    this.getCrimes();
  },
};
</script>

<style>
.someExtraClass {
  background-color: aqua;
  padding: 10px;
  border: 1px solid #333;
  border-radius: 0 20px 20px 20px;
  box-shadow: 5px 3px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: auto !important;
  height: auto !important;
  margin: 0 !important;
}
</style>