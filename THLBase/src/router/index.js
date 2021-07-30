import Vue from 'vue'
import Router from 'vue-router'
import Index from '../components/Index.vue'
import About from '../components/About'
import test from '../components/test'
import logIn from '../components/log_in/logIn'
import mode2 from '../components/developer_mode/mode2'
import mode1 from '../components/developer_mode/mode1'
import mode3 from '../components/developer_mode/mode3'
import mode4 from '../components/developer_mode/mode4'
import mode5 from '../components/developer_mode/mode5'
import mode6 from '../components/developer_mode/mode6'
import mode2_ from '../components/developer_mode/mode2_'
import mode7 from '../components/developer_mode/mode7'
// import modify1 from '../components/developer_modify/modify1'
import modify2 from '../components/developer_modify/modify2'
// eslint-disable-next-line camelcase
import modify3_1 from '../components/developer_modify/modify3_1'
// eslint-disable-next-line camelcase
import modify3_2 from '../components/developer_modify/modify3_2'
import jsonGet from '../components/Downloads/jsonGet'
Vue.use(Router)

var router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/index',
      meta: {
        title: 'LZWHR DM MODE',
        keepAlive: true
      }
    },
    {
      path: '/index',
      component: Index,
      meta: {
        title: 'LZWHR DM MODE',
        keepAlive: true
      }
    },
    {
      path: '/about',
      component: About
    },
    {
      path: '/developer1',
      component: logIn
    },
    {
      path: '/developer2',
      component: logIn
    },
    {
      path: '/monitor1',
      component: logIn
    },
    {
      path: '/monitor2',
      component: logIn
    },
    {
      path: '/developer1/developMode',
      component: modify2
    },
    {
      path: '/developer1/developMode/mode2',
      component: modify3_1
    },
    {
      path: '/developer1/developMode/mode3',
      component: modify3_2
    },
    {
      path: '/developer2/developMode',
      component: mode1
    },
    {
      path: '/monitor1/monitorMode',
      component: About
    },
    {
      path: '/monitor2/monitorMode',
      component: About
    },
    {
      path: '/developer2/developMode/mode2',
      component: mode2
    },
    {
      path: '/developer2/developMode/mode2/mode2_',
      component: mode2_
    },
    {
      path: '/developer2/developMode/mode2/mode2_/mode3',
      component: mode3
    },
    {
      path: '/developer2/developMode/mode2/mode2_/mode3/mode4',
      component: mode4
    },
    {
      path: '/developer2/developMode/mode2/mode2_/mode3/mode4/mode5',
      component: mode5
    },
    {
      path: '/developer2/developMode/mode2/mode2_/mode3/mode4/mode5/mode6',
      component: mode6
    },
    {
      path: '/developer2/developMode/mode2/mode2_/mode3/mode4/mode5/mode6/mode7',
      component: mode7
    },
    {
      path: '/test',
      component: test
    },
    {
      path: '/developer1/developMode/mode1',
      component: About
    },
    {
      path: '/developer1/developMode/mode2',
      component: modify2
    },
    {
      path: '/jsonGet',
      component: jsonGet
    }
  ]
})

router.beforeEach((to, form, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  } else {
    document.title = 'LZWHR DM MODE'
  }
  next()
})

export default router
