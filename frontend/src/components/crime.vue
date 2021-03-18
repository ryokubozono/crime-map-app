<template>
  <div class="column is-8 is-offset-2">
    <div class="card">
      <div class="card-content">
        <h3 class="title is-3">“{{crime.id}}”</h3>
        <p class="subtitle">{{crime.location}}</p>
      </div>
      <footer class="card-footer">
        <p class="card-footer-item">
          <span>
            {{crime}}
          </span>
        </p>
      </footer>
    </div>
  </div>
</template>

<script>
// import moment from 'moment/moment';

export default {
  name: "Crime",
  props: ["crime"],
};
</script>
