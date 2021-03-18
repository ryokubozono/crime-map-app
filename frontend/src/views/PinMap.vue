<template>
  <div class="pin_map">
    <h1>This is an pin_map page</h1>
    <!--マップコンポーネント表示-->
    <MapPin></MapPin>
  </div>
</template>

<script>
    // マップコンポーネント読み込み
    import MapPin from '@/components/MapPin.vue'

    export default {
        name: 'pinmap',
        components: {
            MapPin
        }
    }
</script>