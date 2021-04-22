<template>
  <div>
    <div
      :class="$style.frameDiv"
    >
      <div
        :class="$style.mapDiv"
      >
        <l-map 
          :zoom="zoom" 
          :center="center"
          style="height: 700px; width: 1000px"    
          @update:center="centerUpdate"
          @update:zoom="zoomUpdate"
        >
          <l-tile-layer 
            :url="url"
            :attribution="attribution"
            :options="tileOptions"
          />
          <LeafletHeatmap 
            v-if="showHeat && currentZoom <= changeZoom"
            :lat-lng="latLngs" 
            :max="maxValue" 
            :radius="radiusValue" 
            :min-opacity="minValue" 
            :blur="15"
            @ready="ready"
          />
          <Vue2LeafletMarkercluster 
            v-if="currentZoom > changeZoom"
            :options="clusterOptions" 
            @clusterclick="click()" 
            @ready="ready"
          >
            <l-marker 
              v-for="l in locations" 
              :key="l.id" 
              :lat-lng="l.latlng" 
              :icon="icon"
              v-on:click="getMarker(l)"
            > 
            </l-marker>
          </Vue2LeafletMarkercluster>
          <l-circle-marker
            v-if="showText"
            :lat-lng="circleCenter"
            :radius="circleRadius"
            :color="circleColor"
            :fillColor="circleColor"
          />
        </l-map>
      </div>
    </div>
    <v-overlay
      :z-index=1000
      :value="loading"
    >
      <vue-loading v-if="loading" type="spin" color="#333" :size="{ width: '50px', height: '50px' }"></vue-loading>
    </v-overlay>
    <div
      :class="$style.btnDiv"
    >
      <v-btn v-on:click="go_by_id(0)" :disabled="crime_type == 0" :outlined="crime_type == 0">オートバイ盗</v-btn>
      <v-btn v-on:click="go_by_id(1)" :disabled="crime_type == 1" :outlined="crime_type == 1">ひったくり</v-btn>
      <v-btn v-on:click="go_by_id(2)" :disabled="crime_type == 2" :outlined="crime_type == 2">自転車盗</v-btn>
      <v-btn v-on:click="go_by_id(3)" :disabled="crime_type == 3" :outlined="crime_type == 3">自動車盗</v-btn>
      <v-btn v-on:click="go_by_id(4)" :disabled="crime_type == 4" :outlined="crime_type == 4">自動販売機狙い</v-btn>
      <v-btn v-on:click="go_by_id(5)" :disabled="crime_type == 5" :outlined="crime_type == 5">車上狙い</v-btn>
      <v-btn v-on:click="go_by_id(6)" :disabled="crime_type == 6" :outlined="crime_type == 6">部品狙い</v-btn>
      <v-btn v-on:click="go_by_mode(0)" :disabled="mode == 0" :outlined="mode == 0">件数/人口</v-btn>
      <v-btn v-on:click="go_by_mode(1)" :disabled="mode == 1" :outlined="mode == 1">件数</v-btn>
    </div>
  </div>
  
</template>

<script>

import { LMap, LTileLayer, LMarker, LCircleMarker } from "vue2-leaflet";
import { latLng, Icon, icon } from 'leaflet'
import LeafletHeatmap from '@/components/LeafletHeatmap'
import Vue2LeafletMarkercluster from '@/components/Vue2LeafletMarkercluster'
import iconUrl from 'leaflet/dist/images/marker-icon.png'
import shadowUrl from 'leaflet/dist/images/marker-shadow.png'
import axios from "axios";
import { VueLoading } from 'vue-loading-template'

export default {
  components: {
    LMap,
    LTileLayer, 
    LeafletHeatmap,
    LMarker,
    Vue2LeafletMarkercluster,
    VueLoading, 
    LCircleMarker,
  },
  data() {
    let locations = []
    let customicon = icon(Object.assign({},
    Icon.Default.prototype.options,
    {iconUrl, shadowUrl}
    ))
    console.log(locations)

    return {
        changeZoom: 15,
        locations,
        icon: customicon,
        clusterOptions: {},
        crimes: "",
        zoom: Number(this.$route.query.zoom),
        center: latLng(this.$route.query.lat, this.$route.query.lng),
        currentCenter: latLng(this.$route.query.lat, this.$route.query.lng),
        currentZoom: this.$route.query.zoom,
        maxValue: 1,
        radiusValue: 12,
        minValue: 0.3,
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:
            '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',

        staticAnchor: [16, 37],
        customText: "Foobar",
        iconSize: 64,
        latLngs: [],
        circleCenter: "",
        circleRadius: 6,
        circleColor: "red",
        showHeat: false,
        crime_type: this.$route.params['id'],
        mode: this.$route.params['mode'],
        // gradients: {0.4: 'blue', 0.65: 'lime', 1: 'red'}
        tileOptions: {
          maxZoom: 17, 
          minZoom: 5,
          minNativeZoom: 1,
          zoom:10, 
          detectRetina: true,
          updateWhenIdle: false, 
          keepBuffer: 10
        },
        fastApiUrl: "",
        loading: true,
        showText: false,
        loc: "",
        prefecture: "",
        city: "",
        street: "",
        date: "",
        hour: "",
        crime_id: "",
        object: "",
        tmp_population: 1,
    }
  },
  methods: {
    click: (e) => console.log("clusterclick", e),
    ready: function(e) {
      console.log('ready', e)
    },
    async get_crime_by_type() {
        if (Number(this.currentZoom) <= this.changeZoom){
            await axios.get(`${this.fastApiUrl}/api/places/filter?skip=0&limit=300000&lat=${this.currentCenter.lat}&lng=${this.currentCenter.lng}&zoom=${this.currentZoom}`).then(response => response.data.forEach(row => {
                switch (this.mode) {
                  case "0":
                    this.tmp_population = row.population;
                    break;
                  case "1":
                    this.tmp_population = 1;
                    break;
                  default:
                    this.tmp_population = 1;
                }
                switch (this.crime_type) {
                  case "0":
                    this.latLngs.push([row.fy, row.fx, row.crime_0/this.tmp_population]);
                    break;
                  case "1":
                    this.latLngs.push([row.fy, row.fx, row.crime_1/this.tmp_population]);
                    break;
                  case "2":
                    this.latLngs.push([row.fy, row.fx, row.crime_2/this.tmp_population]);
                    break;
                  case "3":
                    this.latLngs.push([row.fy, row.fx, row.crime_3/this.tmp_population]);
                    break;
                  case "4":
                    this.latLngs.push([row.fy, row.fx, row.crime_4/this.tmp_population]);
                    break;
                  case "5":
                    this.latLngs.push([row.fy, row.fx, row.crime_5/this.tmp_population]);
                    break;
                  case "6":
                    this.latLngs.push([row.fy, row.fx, row.crime_7/this.tmp_population]);
                    break;
                  default:
                    this.latLngs.push([row.fy, row.fx, row.population]);
                }
                this.showHeat = true;
            }));
            this.loading = false;
            console.log(this.latLngs);
        } else {
            await axios.get(`${this.fastApiUrl}/api/places/filter?skip=0&limit=300000&lat=${this.currentCenter.lat}&lng=${this.currentCenter.lng}&zoom=${this.currentZoom}`).then(response => response.data.forEach((row, i) => {
                this.locations.push({
                    id: i+1,
                    latlng: latLng(row.fy, row.fx),
                    population: row.population,
                })
            }));
            console.log(this.locations);
            this.loading = false;
        }
    },
    // @update:zoom="zoomUpdate"がcenterも更新してしまうので削除した
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
      // this.go(this.crime_type);
    },
    go_by_id(id) {
      // <router-link>では同じコンポーネントの再描画ができなかったから、URLの書き換え+リロードで実装した
      this.$router.replace({ path: `/place_map/${id}/${this.mode}`, query: { lat: this.currentCenter.lat, lng: this.currentCenter.lng, zoom: this.currentZoom }}).then(() => {
        this.$router.go(0)
      })
    },
    go_by_mode(mode) {
      // <router-link>では同じコンポーネントの再描画ができなかったから、URLの書き換え+リロードで実装した
      this.$router.replace({ path: `/place_map/${this.crime_type}/${mode}`, query: { lat: this.currentCenter.lat, lng: this.currentCenter.lng, zoom: this.currentZoom }}).then(() => {
        this.$router.go(0)
      })
    },
    getMarker: function(location) {
      this.showText = true
      this.loc = location.location
      this.prefecture = location.prefecture
      this.city = location.city
      this.street = location.street
      this.date = location.date
      this.hour = location.hour
      this.crime_id = location.crime_type
      this.object = location.object
      this.circleCenter = location.latlng
      console.log(location)
      console.log(this.circleCenter)
    },
    closeText: function() {
      this.showText = false
    },
  },
  mounted() {
    this.fastApiUrl = process.env.VUE_APP_FAST_API_URL
    Promise.all(this.get_crime_by_type())
    setTimeout(() => {
        console.log('done')
        this.$nextTick(() =>{
            this.clusterOptions = { disableClusteringAtZoom: 11 }
        });
    }, 1000);
  },
  computed: {

  },
  watch: {
    currentCenter: function () {
      this.go_by_id(this.crime_type);
    }
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

<style module>
  .frameDiv{
    position: relative;
  }
  .mapDiv{
    position: absolute;
  }
  .textDiv{
    position: absolute;
    top: 100px;
    left: 0px;
    /* background: rgba(255,255,255,0.5); */
    z-index: 800;
    /* width: 200px; */
    /* padding: 10px; */
  }
  .btnDiv{
    position: absolute;
    top: 700px;
    left: 50px;
    z-index: 700;
  }
</style>