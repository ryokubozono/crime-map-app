<template>
  <v-container
    id="dashboard"
    fluid
    tag="section"
  >
    <v-row>
      <v-col
        cols="12"
        md="12"
      >
        <base-material-card
          color="info"
          class="px-5 py-3"
        >
          <template v-slot:heading>
            <div class="display-2 font-weight-light">
              Places_0
            </div>

            <div class="subtitle-1 font-weight-light">
              人口、犯罪数
            </div>
          </template>
          <v-card-text>
            <v-data-table
              :headers="headers"
              :items="places_0"
            />
          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="12"
      >
        <base-material-card
          color="warning"
          class="px-5 py-3"
        >
          <template v-slot:heading>
            <div class="display-2 font-weight-light">
              Places_1
            </div>

            <div class="subtitle-1 font-weight-light">
              人口、犯罪数/1,000人
            </div>
          </template>
          <v-card-text>
            <v-data-table
              :headers="headers"
              :items="places_1"
            />
          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from "axios";

  export default {
    name: 'Dashboard',

    data () {
      return {
        fastApiUrl: "",
        headers: [
          {
            sortable: true,
            text: 'ID',
            value: 'id',
          },
          {
            sortable: false,
            text: 'LocName',
            value: 'locname',
          },
          {
            sortable: true,
            text: 'Population',
            value: 'population',
            align: 'right',
          },
          {
            sortable: true,
            text: 'オートバイ盗',
            value: 'crime_0',
            align: 'right',
          },
          {
            sortable: true,
            text: 'ひったくり',
            value: 'crime_1',
            align: 'right',
          },
          {
            sortable: true,
            text: '自転車盗',
            value: 'crime_2',
            align: 'right',
          },
          {
            sortable: true,
            text: '自動車盗',
            value: 'crime_3',
            align: 'right',
          },
          {
            sortable: true,
            text: '自動販売機狙い',
            value: 'crime_4',
            align: 'right',
          },
          {
            sortable: true,
            text: '車上狙い',
            value: 'crime_5',
            align: 'right',
          },
          {
            sortable: true,
            text: '部品狙い',
            value: 'crime_6',
            align: 'right',
          },
        ],
        places_0: [
        ],
        places_1: [
        ],
      }
    },

    methods: {
      async get_crime_by_type() {
        axios.get(`${this.fastApiUrl}/api/places/city?skip=0&limit=10000`)
          .then(response => response.data.forEach(row => {
            this.places_0.push({
              'id': row.id, 
              'locname': row.LocName, 
              'population': row.population, 
              'crime_0': row.crime_0, 
              'crime_1': row.crime_1,
              'crime_2': row.crime_2,
              'crime_3': row.crime_3,
              'crime_4': row.crime_4,
              'crime_5': row.crime_5,
              'crime_6': row.crime_6,
            })
            this.places_1.push({
              'id': row.id, 
              'locname': row.LocName, 
              'population': row.population, 
              'crime_0': Math.round(row.crime_0/row.population*1000000)/1000, 
              'crime_1': Math.round(row.crime_1/row.population*1000000)/1000,
              'crime_2': Math.round(row.crime_2/row.population*1000000)/1000,
              'crime_3': Math.round(row.crime_3/row.population*1000000)/1000,
              'crime_4': Math.round(row.crime_4/row.population*1000000)/1000,
              'crime_5': Math.round(row.crime_5/row.population*1000000)/1000,
              'crime_6': Math.round(row.crime_6/row.population*1000000)/1000,
            })
        })); 
        axios.get(`${this.fastApiUrl}/api/places/town?skip=0&limit=10000`)
          .then(response => response.data.forEach(row => {
            this.places_2.push({
              'id': row.id, 
              'locname': row.LocName, 
              'population': row.population, 
              'crime_0': Math.round(row.crime_0/row.population*1000000)/1000, 
              'crime_1': Math.round(row.crime_1/row.population*1000000)/1000,
              'crime_2': Math.round(row.crime_2/row.population*1000000)/1000,
              'crime_3': Math.round(row.crime_3/row.population*1000000)/1000,
              'crime_4': Math.round(row.crime_4/row.population*1000000)/1000,
              'crime_5': Math.round(row.crime_5/row.population*1000000)/1000,
              'crime_6': Math.round(row.crime_6/row.population*1000000)/1000,
            })
        })); 
      },
      complete (index) {
        this.list[index] = !this.list[index]
      },
    },
    mounted() {

      this.fastApiUrl = process.env.VUE_APP_FAST_API_URL
      Promise.all(this.get_crime_by_type())
    }
  }
</script>
