import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Event from '@/views/Event.vue'
import Crime from '@/views/Crime.vue'
import SimpleMap from '@/views/SimpleMap'
import PinMap from '@/views/PinMap'
import HeatMap from '@/views/HeatMap'
import ClusterMap from '@/views/ClusterMap'
import User from '@/views/User.vue'

Vue.use(VueRouter);

// '#' in urlの対策
const mode =  'history';

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/event',
    name: 'event',
    component: Event
  },
  {
    path: '/crime',
    name: 'crime',
    component: Crime
  },
  {
    path: '/simple_map',
    name: 'simple_map',
    component: SimpleMap
  },
  {
    path: '/pin_map',
    name: 'pin_map',
    component: PinMap
  },
  {
    path: '/heat_map/:id',
    name: 'heat_map_by_crime_type',
    component: HeatMap
  },
  {
    path: '/cluster_map/:id',
    name: 'cluster_map_by_crime_type',
    component: ClusterMap
  },
  {
    path: '/user',
    name: 'user',
    component: User
  },
]

export default new VueRouter({routes, mode})
