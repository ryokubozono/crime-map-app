<template>
  <div class="column is-8 is-offset-2">
    <div class="card">
      <div class="card-content">
        <h3 class="title is-3">“{{event.address}}”</h3>
        <p class="subtitle">{{crime_name}}</p>
      </div>
      <footer class="card-footer">
        <p class="card-footer-item">
          <span>
            {{event}}
          </span>
        </p>
      </footer>
    </div>
  </div>
</template>

<script>
// import moment from 'moment/moment';

export default {
  name: "Event",
  props: ["event"],
  computed: {
    crime_name: function() {
      switch(this.event.crime_type){
        case 0:
          return "オートバイ盗"
        case 1:
          return "ひったくり"
        case 2:
          return "自転車盗"
        case 3:
          return "自動車盗"
        case 4:
          return "自動販売機狙い"
        case 5:
          return "車上狙い"
        case 6:
          return "部品狙い"
        default:
          return "nashi"
      }
    }
  },
};
</script>
