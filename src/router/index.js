import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListBook from '@/components/ListBook'

import Main from '@/components/HelloWorld'
import Login from '@/components/Login'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/books',
      name: 'ListBook',
      component: ListBook
    },
    {
      path: '/inicio',
      name: 'Inicio',
      component: Main
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
  ],
  mode: 'history',
})
