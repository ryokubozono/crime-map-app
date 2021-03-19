<template>
  <div>
    <button v-on:click="go(0)">オートバイ盗</button>
    <button v-on:click="go(1)">ひったくり</button>
    <button v-on:click="go(2)">自転車盗</button>
    <button v-on:click="go(3)">自動車盗</button>
    <button v-on:click="go(4)">自動販売機狙い</button>
    <button v-on:click="go(5)">車上狙い</button>
    <button v-on:click="go(6)">部品狙い</button>


    <p>Center is at {{ currentCenter }} and the zoom is: {{ currentZoom }}</p>
    <l-map 
        :zoom="zoom" 
        :center="center"
        style="height: 700px; width: 700px"    
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate"
    >
        <l-tile-layer 
            :url="url"
            :attribution="attribution"
            :options="tileOptions"
        />
        <LeafletHeatmap 
            v-if="showHeat"
            :lat-lng="latLngs" 
            :max="maxValue" 
            :radius="10" 
            :min-opacity="0.75" 
            :blur="15"
        />
    </l-map>
  </div>
</template>

<script>

import { LMap, LTileLayer } from "vue2-leaflet";
import LeafletHeatmap from '@/components/LeafletHeatmap'
import axios from "axios";
import { latLng } from "leaflet";

export default {
  components: {
    LMap,
    LTileLayer, 
    LeafletHeatmap
  },
  data() {
    return {
        crimes: "",
        zoom: Number(this.$route.query.zoom),
        center: latLng(this.$route.query.lat, this.$route.query.lng),
        currentCenter: latLng(this.$route.query.lat, this.$route.query.lng),
        currentZoom: this.$route.query.zoom,
        maxValue: 1,
        url: 'https://tile.mierune.co.jp/mierune/{z}/{x}/{y}.png',
        attribution:
            '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',

        staticAnchor: [16, 37],
        customText: "Foobar",
        iconSize: 64,
        latLngs: [],
        loading: true,
        showHeat: false,
        crime_type: this.$route.params['id'],
        // gradients: {0.4: 'blue', 0.65: 'lime', 1: 'red'}
        tileOptions: {
          maxZoom: 13, 
          minZoom: 9,
          minNativeZoom: 1,
          zoom:10, 
          detectRetina: true,
          updateWhenIdle: false, 
          keepBuffer: 10
        },
        fastApiUrl: "",
    }
  },
  methods: {
    // getCrimes() {
    //     axios.get("http://127.0.0.1:8000/api/crimes/?skip=0&limit=2000").then(response => response.data.forEach(row => {
    //         this.latLngs.push([row.fy, row.fx, 0.1])
    //     }));
    // },
    async get_crime_by_type() {
        await axios.get(`${this.fastApiUrl}/api/crimes/${this.crime_type}?skip=0&limit=10000&lat=${this.currentCenter.lat}&lng=${this.currentCenter.lng}`).then(response => response.data.forEach(row => {
            this.latLngs.push([row.fy, row.fx, 1]);
            this.showHeat = true;
        }));
    },
    // @update:zoom="zoomUpdate"がcenterも更新してしまうので削除した
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
      // this.go(this.crime_type);
    },
    go: function(id) {
      // <router-link>では同じコンポーネントの再描画ができなかったから、URLの書き換え+リロードで実装した
      this.$router.replace({ path: `/heat_map/${id}`, query: { lat: this.currentCenter.lat, lng: this.currentCenter.lng, zoom: this.currentZoom }}).then(() => {
        this.$router.go(0)
      })
    },

  },
  mounted() {
    this.fastApiUrl = process.env.VUE_APP_FAST_API_URL
    Promise.all(this.get_crime_by_type())
    // setTimeout(() => {
    //   this.loading = false;
    // }, 2000);
  },
  computed: {
  },
  watch: {
    currentCenter: function () {
      this.go(this.crime_type);
    }
  },
}

</script>