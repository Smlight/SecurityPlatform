import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/page/Home'
import Login from '@/components/page/Login'
import Register from '@/components/page/Register'
import Challenges from '@/components/page/Challenges'
import CVEs from '@/components/page/CVEs'
import CveDetail from '@/components/page/CveDetail'
import AddChallenge from '@/components/page/AddChallenge'
import AddCVE from '@/components/page/AddCVE'
// import Resume from '@/components/page/Resume'
// import Recommend from '@/components/page/Recommend'
// import Search from '@/components/page/Search'

Vue.use(Router)

export default new Router({
	routes: [
	{
		path: '/',
		redirect: '/index'
	},
	{
		path: '/index',
		component: Home,
	},
	{
		path: '/login',
		component: Login
	},
	{
		path: '/register',
		component: Register
	},
	{
		path: '/challenges',
		component: Challenges
	},
	{
		path: '/cves',
		component: CVEs
	},
	{
		path: '/cves/:id',
		component: CveDetail
	},
	{
		path: '/addchallenge',
		component: AddChallenge
	},
// 	{
// 		path: '/resume',
// 		component: Resume
// 	},
// 	{
// 		path: '/recommend',
// 		component: Recommend
// 	},
// 	{
// 		path: '/search',
// 		component: Search
// 	},
	{
		path: '/HelloWorld',
		name: 'HelloWorld',
		component: HelloWorld,
	}
	]
})
