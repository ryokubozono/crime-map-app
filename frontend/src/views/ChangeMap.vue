<template>
  <div class="change_map">
    <MapChange />
    <h1>This is an change_map page</h1>
  </div>
</template>

<script>
    // マップコンポーネント読み込み
    import MapChange from '@/components/MapChange.vue'

    export default {
        name: 'changemap',
        components: {
            MapChange
        }
    }
</script>