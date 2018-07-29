import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/common/Home'
import Login from '@/components/page/Login'
import Register from '@/components/page/Register'
import Info from '@/components/page/Info'
import Resume from '@/components/page/Resume'
import Recommend from '@/components/page/Recommend'
import Search from '@/components/page/Search'

Vue.use(Router)

export default new Router({
	routes: [
	{
		path: '/',
		redirect: '/login'
	},
	{
		path: '/home',
		component: Home,
		children: [
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
		{
			path: '/info',
			component: Info
		},
		{
			path: '/resume',
			component: Resume
		},
		{
			path: '/recommend',
			component: Recommend
		},
		{
			path: '/search',
			component: Search
		},
		]
	},
	{
		path: '/HelloWorld',
		name: 'HelloWorld',
		component: HelloWorld,
	}
	]
})
