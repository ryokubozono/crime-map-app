<template>
  <div class="place_map">
    <MapPlace />
  </div>
</template>

<script>
    // マップコンポーネント読み込み
    import MapPlace from '@/components/MapPlace.vue'

    export default {
        name: 'placemap',
        components: {
            MapPlace
        }
    }
</script>