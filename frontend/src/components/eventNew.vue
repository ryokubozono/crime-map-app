<template>
  <div class="column is-10 is-offset-1">
    <div class="box">
      <article class="media">
        <div class="media-content">
          <div class="content">
            <div class="field has-addons has-addons-centered">
              <div class="control is-expanded">
                <input class="input" type="text" v-model="text" placeholder="Add new event" />
                <select class="input" type="number" v-model="crime_type" placeholder="no.">
                  <option value="0">オートバイ盗</option>
                  <option value="1">ひったくり</option>
                  <option value="2">自転車盗</option>
                  <option value="3">自動車盗</option>
                  <option value="4">自動販売機狙い</option>
                  <option value="5">車上狙い</option>
                  <option value="6">部品狙い</option>
                </select>
                <input class="input" type="number" step="0.000001" v-model="lat" placeholder="lat" />
                <input class="input" type="number" step="0.000001" v-model="long" placeholder="long" />
                <input class="input" type="date" v-model="date" placeholder="date" />
              </div>
              <div class="control">
                <button class="button is-link" @click="submit">Add</button>
              </div>
            </div>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "newEvent",
  data() {
    return {
      text: "test",
      crime_type: 0,
      id: 0,
      lat: 0,
      long: 0,
      created_at: 0,
      updated_at: 0,
      date: null,
    };
  },
  methods: {
    submit() {
      axios.post("http://127.0.0.1:8000/api/events/", {
        crime_type: this.crime_type, 
        address: this.text, 
        id: this.id, 
        long: this.long, 
        lat: this.lat, 
        date: this.date,
        created_at: this.created_at, 
        updated_at: this.updated_at
      }).then(() => {
        this.text = "test";
        this.$emit('added');
      });
    }
  }
};
</script>
