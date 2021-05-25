import Vue from 'vue'
import Router from 'vue-router'
import Store from '@/store/index.js'
import firebase from 'firebase'
import firestore from '@/firebase.js'

import Event from '@/views/Event.vue'
import Crime from '@/views/Crime.vue'
import SimpleMap from '@/views/SimpleMap'
import PinMap from '@/views/PinMap'
import HeatMap from '@/views/HeatMap'
import ClusterMap from '@/views/ClusterMap'
import ChangeMap from '@/views/ChangeMap'
import PlaceMap from '@/views/PlaceMap.vue'
import Dashboard from '@/views/Dashboard.vue'
import PlaceList from '@/views/PlaceList.vue'

import Login from '@/views/Login.vue'


Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
  {
    path: '/blog',
    component: () => import('@/views/layouts/BlogIndex'),
    children: [
      {
        path: '/blog/',
        name: 'blog_visible',
        component: () => import('@/views/blog/BlogVisible')
      },
      {
        path: '/blog/:blog_id',
        name: 'blog_by_id',
        component: () => import('@/views/blog/BlogById'),
      },
    ]
  },
  {
    path:'/admin/blog_show/',
    component: () => import('@/views/layouts/AdminShowIndex'),
    children: [

      {
        path: '/admin/blog_show/:blog_id',
        name: 'blog_show',
        component: () => import('@/views/admin/BlogShow'),
        meta: { 
          requiresAuth: true,
        }
      },
    ]
  },
  {
    path: '/admin/',
    component: () => import('@/views/layouts/AdminIndex'),
    children: [
      {
        path: '/admin',
        name: 'admin_index',
        component: () => import('@/views/admin/Index'),
        meta: { 
          requiresAuth: true,
        }
      },
      {
        path: '/admin/user',
        name: 'user',
        component: () => import('@/views/admin/User'),
        meta: { 
          requiresAuth: true,
        }
      },
      {
        path: '/admin/blog_new',
        name: 'blog_new',
        component: () => import('@/views/admin/BlogNew'),
        meta: { 
          requiresAuth: true,
        }
      },
      {
        path: '/admin/blog_all',
        name: 'blog_all',
        component: () => import('@/views/admin/BlogAll'),
        meta: { 
          requiresAuth: true,
        }
      },
      {
        path: '/admin/blog_edit/:blog_id',
        name: 'blog_edit',
        component: () => import('@/views/admin/BlogEdit'),
        meta: { 
          requiresAuth: true,
        }
      },
      {
        path: '/admin/tag_new',
        name: 'tag_new',
        component: () => import('@/views/admin/TagNew'),
        meta: { 
          requiresAuth: true,
        }
      },
      {
        path: '/admin/tags',
        name: 'tag_all',
        component: () => import('@/views/admin/TagAll'),
        meta: { 
          requiresAuth: true,
        }
      },
      {
        path: '/admin/tag_show/:tag_id',
        name: 'tag_show',
        component: () => import('@/views/admin/TagShow'),
        meta: { 
          requiresAuth: true,
        }
      },
      {
        path: '/admin/tag_edit/:tag_id',
        name: 'tag_edit',
        component: () => import('@/views/admin/TagEdit'),
        meta: { 
          requiresAuth: true,
        }
      },
    ]
  },
  {
    path: '/',
    component: () => import('@/views/layouts/BlankIndex'),
    children: [
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
        path: '/login',
        name: 'login',
        component: Login,
      },

      {
        path: '*',
        name: 'not_found',
        component: () => import('@/views/NotFound'),
      }
    ]
  }
]
})

router.beforeEach((to, from, next) => {
  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (Store.state.auth.user !== "") {
      firestore.collection('users')
      .get()
      .then(querySnapshot => {
        const users = querySnapshot.docs.map(doc => doc.data())
        let auth = false;
        console.log(users);
        users.forEach(user => {
          if (user.email === Store.state.auth.user.email) {
            auth = true;
          }
        })
        if (auth) {
          next();
        } else {
          firebase.auth().signOut()
          Store.dispatch("auth", {
            user: '',
            token: ''
          })
          next({ name: 'login', query: { redirect: to.fullPath } });
        }
    })
    } else {
      next({ name: 'login', query: { redirect: to.fullPath } });
    }
  } else if (to.matched.some(record => record.meta.requiresAdmin) && Store.state.auth.superUser == false) {
    next(false); //ルートにリダイレクト
  } else if (to.matched.some(record => record.meta.login) && Store.state.auth.userToken) {
    next({ name: 'admin_index'})
  } else {
    next();
  }
});

export default router
