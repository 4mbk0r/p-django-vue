import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListBook from '@/components/ListBook'
import Adminstrar from '@/components/Administrar'
import Main from '@/components/HelloWorld'
import Login from '@/components/Login'
import Chatbot from '@/components/Chatbot'
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
      path: '/administrar',
      name: 'Administrar',
      component: Adminstrar
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
    {
      path: '/chatbot',
      name: 'Chatbot',
      component: Chatbot
    },
  ],
  mode: 'history',
})
