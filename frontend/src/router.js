import Vue from 'vue'
import Router from 'vue-router'
import Store from '@/store/index.js'

import Home from '@/views/Home.vue'
import Event from '@/views/Event.vue'
import Crime from '@/views/Crime.vue'
import SimpleMap from '@/views/SimpleMap'
import PinMap from '@/views/PinMap'
import HeatMap from '@/views/HeatMap'
import ClusterMap from '@/views/ClusterMap'
import ChangeMap from '@/views/ChangeMap'
import User from '@/views/User.vue'
import PlaceMap from '@/views/PlaceMap.vue'
import Dashboard from '@/views/Dashboard.vue'
import PlaceList from '@/views/PlaceList.vue'
import BlogNew from '@/views/BlogNew.vue'
import BlogEdit from '@/views/BlogEdit.vue'
import TagNew from '@/views/TagNew.vue'
import TagEdit from '@/views/TagEdit.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Forget from '@/views/Forget.vue'

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
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
    path: '/change_map/:id',
    name: 'change_map_by_crime_type',
    component: ChangeMap
  },
  {
    path: '/place_map/:id/:mode',
    name: 'place_map_by_crime_type',
    component: PlaceMap
  },
  {
    path: '/user',
    name: 'user',
    component: User,
    meta: { 
      login: true,
    }
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard
  },
  {
    path: '/places/:place_type',
    name: 'places_by_type',
    component: PlaceList,
  },
  {
    path: '/blog_new',
    name: 'blog_new',
    component: BlogNew,
  },
  {
    path: '/blog_edit/:blog_id',
    name: 'blog_edit',
    component: BlogEdit,
  },
  {
    path: '/tag_new',
    name: 'tag_new',
    component: TagNew,
  },
  {
    path: '/tag_edit/:tag_id',
    name: 'tag_edit',
    component: TagEdit,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  {
    path: '/forget',
    name: 'forget',
    component: Forget,
  }
]
})

router.beforeEach((to, from, next) => {
  
  if (to.matched.some(record => record.meta.requiresAuth) && !Store.state.auth.userToken) {
    next({ path: '/login', query: { redirect: to.fullPath } });
  } else if (to.matched.some(record => record.meta.requiresAdmin) && Store.state.auth.superUser == false) {
    next(false); //ルートにリダイレクト
  } else if (to.matched.some(record => record.meta.login) && Store.state.auth.userToken) {
    next({ path: '/user'})
  } else {
    next();
  }
});

export default router
