<template>
  <div class="cluster_map">
    <!--マップコンポーネント表示-->
    <MapCluster></MapCluster>
    <h1>This is an cluster_map page</h1>
  </div>
</template>

<script>
    // マップコンポーネント読み込み
    import MapCluster from '@/components/MapCluster.vue'

    export default {
        name: 'clustermap',
        components: {
            MapCluster
        }
    }
</script>