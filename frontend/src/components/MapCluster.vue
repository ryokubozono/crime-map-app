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
  
  <v-map 
    :zoom="zoom"
    :center="center" 
    style="height: 700px; width: 700px"
    @update:center="centerUpdate"
    @update:zoom="zoomUpdate"
  >
    <v-icondefault></v-icondefault>
    <v-tilelayer 
      :url="url"
      :attribution="attribution"
      :options="tileOptions"
    />
    <v-marker-cluster :options="clusterOptions" @clusterclick="click()" @ready="ready">
      <v-marker v-for="l in locations" :key="l.id" :lat-lng="l.latlng" :icon="icon">
        <v-popup :content="l.text"></v-popup>
      </v-marker>
    </v-marker-cluster>
  </v-map>
</div>
</template>

<script>
  import * as Vue2Leaflet from 'vue2-leaflet'
  import { latLng, Icon, icon } from 'leaflet'
  import Vue2LeafletMarkercluster from '@/components/Vue2LeafletMarkercluster'
  import iconUrl from 'leaflet/dist/images/marker-icon.png'
  import shadowUrl from 'leaflet/dist/images/marker-shadow.png'
  import axios from "axios";

  export default {
    components: {
      'v-map': Vue2Leaflet.LMap,
      'v-tilelayer': Vue2Leaflet.LTileLayer,
      'v-icondefault': Vue2Leaflet.LIconDefault,
      'v-marker': Vue2Leaflet.LMarker,
      'v-popup': Vue2Leaflet.LPopup,
      'v-marker-cluster': Vue2LeafletMarkercluster
    },
    data () {
      let locations = []
      let customicon = icon(Object.assign({},
        Icon.Default.prototype.options,
        {iconUrl, shadowUrl}
      ))
      console.log(locations)
      return {
        locations,
        icon: customicon,
        clusterOptions: {},
        zoom: this.$route.query.zoom,
        center: latLng(this.$route.query.lat, this.$route.query.lng),
        currentCenter: latLng(this.$route.query.lat, this.$route.query.lng),
        currentZoom: this.$route.query.zoom,
        url: 'https://tile.mierune.co.jp/mierune/{z}/{x}/{y}.png',
        attribution:
            '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        crime_type: this.$route.params['id'],
        tileOptions: {
          maxZoom: 13, 
          minZoom: 9,
          minNativeZoom: 1,
          zoom:10, 
          detectRetina: true,
          updateWhenIdle: false, 
          keepBuffer: 10
        },
      }
    },
    methods: {
      click: (e) => console.log("clusterclick", e),
      ready: (e) => console.log('ready', e),
      async getCrimes() {
          await axios.get(`http://127.0.0.1:8000/api/crimes/${this.crime_type}?skip=0&limit=100000&lat=${this.currentCenter.lat}&lng=${this.currentCenter.lng}`).then(response => response.data.forEach((row, i) => {
              this.locations.push({
                id: i+1,
                latlng: latLng(row.fy, row.fx),
                text: row.location,
              })
          }));
          console.log(this.locations)
      },
      // @update:zoom="zoomUpdate"がcenterも更新してしまうので削除した
      zoomUpdate(zoom) {
        this.currentZoom = zoom;
      },
      centerUpdate(center) {
        this.currentCenter = center;
        this.go(this.crime_type);
      },
      go: function(id) {
        // <router-link>では同じコンポーネントの再描画ができなかったから、URLの書き換え+リロードで実装した
        this.$router.replace({ path: `/cluster_map/${id}`, query: { lat: this.currentCenter.lat, lng: this.currentCenter.lng, zoom: this.currentZoom }}).then(() => {
          this.$router.go(0)
        })
      },
    },
    mounted() {
      Promise.all(this.getCrimes())
      setTimeout(() => {
        console.log('done')
        this.$nextTick(() =>{
          this.clusterOptions = { disableClusteringAtZoom: 11 }
        });
      }, 1000);
    },
    watch: {
      // currentCenter: function () {
      //   this.go(this.crime_type);
      // }
    },
  }
</script>

<style>
  @import "~leaflet/dist/leaflet.css";
  @import "~leaflet.markercluster/dist/MarkerCluster.css";
  @import "~leaflet.markercluster/dist/MarkerCluster.Default.css";
  html, body {
    height: 100%;
    margin: 0;
  }
</style>