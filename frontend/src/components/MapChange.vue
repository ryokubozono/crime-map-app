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
            :radius="10" 
            :min-opacity="0.75" 
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
        </l-map>
      </div>
      <div
        :class="$style.textDiv"
        v-if="showText"
      >
        <v-simple-table>
          <template v-slot:default>
            <tbody>
              <tr>
                <th class="text-left">犯罪種別</th>
                <td>{{type2crime(crime_id)}}</td>
              </tr>
              <tr>
                <th class="text-left">発生地名</th>
                <td>{{prefecture}}{{city}}{{street}}</td>
              </tr>
              <tr>
                <th class="text-left">発生現場</th>
                <td>{{loc}}</td>
              </tr>
              <tr>
                <th class="text-left">日時</th>
                <td>{{date}}</td>
              </tr>
              <tr>
                <th class="text-left">被害</th>
                <td>{{object}}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
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
      <v-btn v-on:click="go(0)">オートバイ盗</v-btn>
      <v-btn v-on:click="go(1)">ひったくり</v-btn>
      <v-btn v-on:click="go(2)">自転車盗</v-btn>
      <v-btn v-on:click="go(3)">自動車盗</v-btn>
      <v-btn v-on:click="go(4)">自動販売機狙い</v-btn>
      <v-btn v-on:click="go(5)">車上狙い</v-btn>
      <v-btn v-on:click="go(6)">部品狙い</v-btn>
    </div>
  </div>
  
</template>

<script>

import { LMap, LTileLayer, LMarker } from "vue2-leaflet";
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
  },
  data() {
    let locations = []
    let customicon = icon(Object.assign({},
    Icon.Default.prototype.options,
    {iconUrl, shadowUrl}
    ))
    console.log(locations)

    return {
        changeZoom: 12,
        locations,
        icon: customicon,
        clusterOptions: {},
        crimes: "",
        zoom: Number(this.$route.query.zoom),
        center: latLng(this.$route.query.lat, this.$route.query.lng),
        currentCenter: latLng(this.$route.query.lat, this.$route.query.lng),
        currentZoom: this.$route.query.zoom,
        maxValue: 1,
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:
            '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',

        staticAnchor: [16, 37],
        customText: "Foobar",
        iconSize: 64,
        latLngs: [],
        showHeat: false,
        crime_type: this.$route.params['id'],
        // gradients: {0.4: 'blue', 0.65: 'lime', 1: 'red'}
        tileOptions: {
          maxZoom: 16, 
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
    }
  },
  methods: {
    click: (e) => console.log("clusterclick", e),
    ready: function(e) {
      console.log('ready', e)
    },
    async get_crime_by_type() {
        if (Number(this.currentZoom) <= this.changeZoom){
            await axios.get(`${this.fastApiUrl}/api/crimes/${this.crime_type}?skip=0&limit=200000&lat=${this.currentCenter.lat}&lng=${this.currentCenter.lng}&zoom=${this.currentZoom}`).then(response => response.data.forEach(row => {
                this.latLngs.push([row.fy, row.fx, 1]);
                this.showHeat = true;
            }));
            this.loading = false;
        } else {
            await axios.get(`${this.fastApiUrl}/api/crimes/${this.crime_type}?skip=0&limit=200000&lat=${this.currentCenter.lat}&lng=${this.currentCenter.lng}&zoom=${this.currentZoom}`).then(response => response.data.forEach((row, i) => {
                this.locations.push({
                    id: i+1,
                    latlng: latLng(row.fy, row.fx),
                    location: row.location,
                    prefecture: row.prefecture,
                    city: row.city,
                    street: row.street,
                    date: row.date,
                    hour: row.hour,
                    crime_type: row.crime_type,
                    object: row.object,
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
    go: function(id) {
      // <router-link>では同じコンポーネントの再描画ができなかったから、URLの書き換え+リロードで実装した
      this.$router.replace({ path: `/change_map/${id}`, query: { lat: this.currentCenter.lat, lng: this.currentCenter.lng, zoom: this.currentZoom }}).then(() => {
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
      console.log(location)
    },
    type2crime: function(type) {
      let str = ""
      switch(type) {
        case 0:
          str = "オートバイ盗";
          break;
        case 1:
          str = "ひったくり";
          break;
        case 2:
          str = "自転車盗";
          break;
        case 3:
          str = "自動車盗";
          break;
        case 4:
          str = "自動販売機狙い";
          break;
        case 5:
          str = "車上狙い";
          break;
        case 6:
          str = "部品狙い";
          break;
        default:
          console.log('no match type')
      }
      return str
    }
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
      this.go(this.crime_type);
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
    left: 100px;
    z-index: 700;
  }
</style>