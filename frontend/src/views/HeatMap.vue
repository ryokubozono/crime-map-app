<template>
  <div class="heat_map">
    <MapHeat />
    <h1>This is an heat_map page</h1>
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