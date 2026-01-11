import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import AddrList from '../pages/shop-address/list'
import AddrAdd from '../pages/shop-address/addOrUpdate'
import Order from '../pages/shop-order/list'
import OrderConfirm from '../pages/shop-order/confirm'
import Cart from '../pages/shop-cart/list'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import leixingList from '../pages/leixing/list'
import leixingDetail from '../pages/leixing/detail'
import leixingAdd from '../pages/leixing/add'
import techanList from '../pages/techan/list'
import techanDetail from '../pages/techan/detail'
import techanAdd from '../pages/techan/add'
import xinjiangtechanList from '../pages/xinjiangtechan/list'
import xinjiangtechanDetail from '../pages/xinjiangtechan/detail'
import xinjiangtechanAdd from '../pages/xinjiangtechan/add'
import chargerecordList from '../pages/chargerecord/list'
import chargerecordDetail from '../pages/chargerecord/detail'
import chargerecordAdd from '../pages/chargerecord/add'
import aboutusList from '../pages/aboutus/list'
import aboutusDetail from '../pages/aboutus/detail'
import aboutusAdd from '../pages/aboutus/add'
import systemintroList from '../pages/systemintro/list'
import systemintroDetail from '../pages/systemintro/detail'
import systemintroAdd from '../pages/systemintro/add'
import discusstechanList from '../pages/discusstechan/list'
import discusstechanDetail from '../pages/discusstechan/detail'
import discusstechanAdd from '../pages/discusstechan/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'storeup',
					component: Storeup
				},
                {
                    path: 'shop-address/list',
                    component: AddrList
                },
                {
                    path: 'shop-address/addOrUpdate',
                    component: AddrAdd
                },
				{
					path: 'shop-order/order',
					component: Order
				},
				{
					path: 'cart',
					component: Cart
				},
				{
					path: 'shop-order/orderConfirm',
					component: OrderConfirm
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'leixing',
					component: leixingList
				},
				{
					path: 'leixingDetail',
					component: leixingDetail
				},
				{
					path: 'leixingAdd',
					component: leixingAdd
				},
				{
					path: 'techan',
					component: techanList
				},
				{
					path: 'techanDetail',
					component: techanDetail
				},
				{
					path: 'techanAdd',
					component: techanAdd
				},
				{
					path: 'xinjiangtechan',
					component: xinjiangtechanList
				},
				{
					path: 'xinjiangtechanDetail',
					component: xinjiangtechanDetail
				},
				{
					path: 'xinjiangtechanAdd',
					component: xinjiangtechanAdd
				},
				{
					path: 'chargerecord',
					component: chargerecordList
				},
				{
					path: 'chargerecordDetail',
					component: chargerecordDetail
				},
				{
					path: 'chargerecordAdd',
					component: chargerecordAdd
				},
				{
					path: 'aboutus',
					component: aboutusList
				},
				{
					path: 'aboutusDetail',
					component: aboutusDetail
				},
				{
					path: 'aboutusAdd',
					component: aboutusAdd
				},
				{
					path: 'systemintro',
					component: systemintroList
				},
				{
					path: 'systemintroDetail',
					component: systemintroDetail
				},
				{
					path: 'systemintroAdd',
					component: systemintroAdd
				},
				{
					path: 'discusstechan',
					component: discusstechanList
				},
				{
					path: 'discusstechanDetail',
					component: discusstechanDetail
				},
				{
					path: 'discusstechanAdd',
					component: discusstechanAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
