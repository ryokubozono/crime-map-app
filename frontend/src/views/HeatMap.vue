<template>
  <div class="heat_map">
    <h1>This is an heat_map page</h1>

    <!--マップコンポーネント表示-->
    <MapHeat />
  </div>
</template>

<script>
    // マップコンポーネント読み込み
    import MapHeat from '@/components/MapHeat.vue'

    export default {
        name: 'heatmap',
        components: {
            MapHeat
        }
    }
</script>