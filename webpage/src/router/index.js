import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/page/HelloWorld'
import Home from '@/components/page/Home'
import Login from '@/components/page/Login'
import Register from '@/components/page/Register'
import Challenges from '@/components/page/Challenges'
import CVEs from '@/components/page/CVEs'
import CveDetail from '@/components/page/CveDetail'
import AddChallenge from '@/components/page/AddChallenge'
import AddCVE from '@/components/page/AddCVE'
import Terminal from '@/components/page/Terminal'

Vue.use(Router)

const router = new Router({
	routes: [
	{
		path: '/index',
		component: Home,
		meta: {
			title: '首页'
		}
	},
    {
		path: '/terminal',
		component: Terminal,
		meta: {
			title: '网页终端'
		}
    },
	// {
	// 	path: '/',
	// 	redirect: '/index'
	// },
	{
		path: '/login',
		component: Login,
		meta: {
			title: '登录'
		}
	},
	{
		path: '/register',
		component: Register,
		meta: {
			title: '注册'
		}
	},
	{
		path: '/challenges',
		component: Challenges,
		meta: {
			title: 'CTF赛题'
		}
	},
	{
		path: '/cves',
		component: CVEs,
		meta: {
			title: 'CVE漏洞库'
		}
	},
	{
		path: '/cves/:id',
		component: CveDetail,
		meta: {
			title: 'CVE漏洞详情'
		}
	},
	{
		path: '/addchallenge',
		component: AddChallenge,
		meta: {
			title: '添加CTF赛题'
		}
	},
	{
		path: '/HelloWorld',
		name: 'HelloWorld',
		component: HelloWorld,
	},
	{
		path: '*',
		redirect: '/index'
	}
	]
})

router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

export default router