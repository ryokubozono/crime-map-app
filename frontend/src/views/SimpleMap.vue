<template>
  <div class="simple_map">
    <h1>This is an simple_map page</h1>
    <!--マップコンポーネント表示-->
    <MapPlane></MapPlane>
  </div>
</template>

<script>
    // マップコンポーネント読み込み
    import MapPlane from '@/components/MapPlane.vue'

    export default {
        name: 'simplemap',
        components: {
            MapPlane
        }
    }
</script>