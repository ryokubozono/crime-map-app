<!--マップコンポーネント-->
<template>
    <div class='mapPane'>
        <!--マップ表示-->
        <div id='map'></div>
    </div>
</template>

<script>
    // Leafletを読み込み
    import L from 'leaflet'

    // デフォルトマーカーアイコン設定
    delete L.Icon.Default.prototype._getIconUrl;
    L.Icon.Default.mergeOptions({
        iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
        iconUrl: require('leaflet/dist/images/marker-icon.png'),
        shadowUrl: require('leaflet/dist/images/marker-shadow.png')
    });

    export default {
        name: 'MapPane',
        mounted: function () {
            // マップオブジェクト生成
            this.mapCreate();
        },
        methods: {
            // マップオブジェクト生成
            mapCreate: function() {
                //MIERUNE Color読み込み
                const m_color = new L.tileLayer('https://tile.mierune.co.jp/mierune/{z}/{x}/{y}.png', {
                    attribution: "Maptiles by <a href='http://mierune.co.jp/' target='_blank'>MIERUNE</a>, under CC BY. Data by <a href='http://osm.org/copyright' target='_blank'>OpenStreetMap</a> contributors, under ODbL."
                });

                //MIERUNE MONO読み込み
                const m_mono = new L.tileLayer('https://tile.mierune.co.jp/mierune_mono/{z}/{x}/{y}.png', {
                    attribution: "Maptiles by <a href='http://mierune.co.jp/' target='_blank'>MIERUNE</a>, under CC BY. Data by <a href='http://osm.org/copyright' target='_blank'>OpenStreetMap</a> contributors, under ODbL."
                });

                //MAP読み込み
                const map = L.map('map', {
                    center: [35.681, 139.763],
                    zoom: 11,
                    zoomControl: true,
                    layers: [m_mono]
                });

                //背景レイヤ
                const Map_BaseLayer = {
                    "MIERUNE Color": m_color,
                    "MIERUNE MONO": m_mono
                };

                //レイヤ設定
                L.control.layers(
                    Map_BaseLayer,
                    null
                ).addTo(map);
            }
        }
    }
</script>

<style scoped>
    /*マップサイズ*/
    #map {
        z-index: 0;
        height: 800px;
        text-align: left;
    }
</style>