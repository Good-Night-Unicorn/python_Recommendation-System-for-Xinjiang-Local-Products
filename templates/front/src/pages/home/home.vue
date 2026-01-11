<template>
	<div class="home-preview">



		<!-- 关于我们 -->
		<div id="about" class="animate__animated">
			<div class="about_item">
				<div class="about_title_box">
					<div class="about_title">{{aboutUsDetail.title}}</div>
					<div class="about_subtitle">{{aboutUsDetail.subtitle}}</div>
				</div>
				<div class="about_img">
					<img :src="baseUrl + aboutUsDetail.picture1">
					<img :src="baseUrl + aboutUsDetail.picture2">
					<img :src="baseUrl + aboutUsDetail.picture3">
				</div>
				<div class="about_content ql-snow ql-editor" v-html="aboutUsDetail.content"></div>
				<div class="about_idea1" />
				<div class="about_idea2" />
				<div class="about_idea3" />
				<div class="about_idea4" />
				<div class="about_more" @click="toDetail('aboutusDetail',aboutUsDetail)">
					<span>更多</span>
					<span class="icon iconfont icon-gengduo1"></span>
				</div>
			</div>
		</div>
		<!-- 关于我们 -->

		<!-- 系统简介 -->
		<div id="system" class="animate__animated">
			<div class="system_item">
				<div class="system_title_box">
					<div class="system_title">{{systemIntroductionDetail.title}}</div>
					<div class="system_subtitle">{{systemIntroductionDetail.subtitle}}</div>
				</div>
				<div class="system_img">
					<img :src="baseUrl + systemIntroductionDetail.picture1">
					<img :src="baseUrl + systemIntroductionDetail.picture2">
					<img :src="baseUrl + systemIntroductionDetail.picture3">
				</div>
				<div class="system_content ql-snow ql-editor" v-html="systemIntroductionDetail.content"></div>
				<div class="system_idea1" />
				<div class="system_idea2" />
				<div class="system_idea3" />
				<div class="system_idea4" />
				<div class="system_more" @click="toDetail('systemintroDetail',systemIntroductionDetail)">
					<span>更多</span>
					<span class="icon iconfont icon-gengduo1"></span>
				</div>
			</div>
		</div>
		<!-- 系统简介 -->
		<!-- 商品推荐 -->
		<div id="animate_recommendtechan" class="recommend animate__animated">
			<div class="recommend_title_box">
				<span class="recommend_title">特产推荐</span>
				<span class="recommend_subhead">{{'techan'.toUpperCase()}} RECOMMEND</span>
			</div>
			<div class="list list20 index-pv1">
				<div class="list-body">
					<div class="list-item" v-for="(item,index) in techanRecommend" :key="index" @click="toDetail('techanDetail', item)">
						<div class="img">
							<img v-if="preHttp(item.tupian)" :src="item.tupian.split(',')[0]" alt="" />
							<img v-else :src="baseUrl + (item.tupian?item.tupian.split(',')[0]:'')" alt="" />
						</div>
						<div class="infoBox">
							<div class="name">{{item.shangpinmingcheng}}</div>
							<div class="name">{{item.leixing}}</div>
							<div class="price">￥{{item.price}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{item.addtime}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont icon-zan10"></span>
								<span class="label">点赞数：</span>
								<span class="text">{{item.thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont icon-shoucang10"></span>
								<span class="label">收藏量：</span>
								<span class="text">{{item.storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont icon-chakan9"></span>
								<span class="label">点击量：</span>
								<span class="text">{{item.clicknum}}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('techan')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 商品推荐 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				aboutUsDetail: {},
				systemIntroductionDetail: {},
				newsList: [],
				techanRecommend: [],





			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getAboutUs();
			this.getSystemIntroduction();
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				setTimeout(()=>{
				},750)
			},


			handleScroll() {
				let arr = [
					{id:'about',css:'animate__'},
					{id:'system',css:'animate__'},
					{id:'animate_recommendtechan',css:'animate__'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getAboutUs() {
				this.$http.get('aboutus/detail/1', {}).then(res => {
					if(res.data.code == 0) {
						this.aboutUsDetail = res.data.data;
					}
				})
			},
			getSystemIntroduction() {
				this.$http.get('systemintro/detail/1', {}).then(res => {
					if(res.data.code == 0) {
						this.systemIntroductionDetail = res.data.data;
					}
				})
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
				autoSortUrl = "techan/autoSort";
				if(localStorage.getItem('frontToken')) {
					autoSortUrl = "techan/autoSort2";
				}
				data = {
					page: 1,
					limit: 8,
					onshelves: 1,
				}
				this.$http.get(autoSortUrl, {params: data}).then(res => {
					if (res.data.code == 0) {
						this.techanRecommend = res.data.data.list;
					}
				});
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		padding: 0;
		margin: 0 auto;
		flex-direction: column;
		max-width: 1300px;
		display: flex;
		width: 100%;
		#about {
			padding: 30px 0;
			margin: 0;
			overflow: hidden;
			background: none;
			width: 100%;
			position: relative;
			order: 3;
			height: auto;
			.about_item {
				padding: 0;
				display: flex;
				width: 100%;
				position: relative;
				flex-wrap: wrap;
				.about_title_box {
					padding: 0 0 0 30px;
					margin: 0 0 20px 0;
					color: #fff;
					background: url(http://codegen.caihongy.cn/20250214/555fe47ac645441b9a9b0f549fd8c99c.png) no-repeat left center;
					width: 100%;
					line-height: 70px;
					text-align: left;
					.about_title {
						color: inherit;
						font-weight: 600;
						width: 100%;
						font-size: 22px;
					}
					.about_subtitle {
						margin: 0 0 10px;
						color: #999;
						display: none;
						width: 100%;
						font-size: 20px;
						line-height: 1.5;
						text-align: center;
					}
				}
				.about_img {
					border: none;
					padding: 0;
					grid-template-columns: 1fr 1fr;
					grid-template-rows: 1fr 1fr;
					display: grid;
					gap: 20px;
					width: 560px;
					height: 400px;
					img:nth-child(1) {
						grid-row: 1 / 2;
						border-radius: 10px;
						margin: 0;
						object-fit: cover;
						display: block;
						width: 270px;
						grid-column: 1 / 2;
						height: 190px;
					}
					img:nth-child(2) {
						grid-row: 1 / 3;
						border-radius: 10px;
						margin: 0;
						object-fit: cover;
						display: block;
						width: 100%;
						grid-column: 2 / 3;
						height: 400px;
					}
					img:nth-child(3) {
						grid-row: 2 / 3;
						border-radius: 10px;
						margin: 0;
						object-fit: cover;
						display: block;
						width: 100%;
						grid-column: 1 / 2;
						height: 190px;
					}
				}
				.about_content {
					padding: 50px;
					margin: 0 0 0 30px;
					color: #fff;
					display: flex;
					letter-spacing: 1px;
					font-size: 16px;
					overflow: hidden;
					background: #80BE1B;
					flex: auto;
					width: 0;
					justify-content: flex-start;
					align-items: flex-start;
					height: auto;
				}
				.about_idea1 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_idea2 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_idea3 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_idea4 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.about_more {
					border: 0;
					cursor: pointer;
					margin: 0;
					top: 0;
					background: #fff;
					display: none;
					width: 80px;
					line-height: 32px;
					position: absolute;
					right: 0;
					text-align: center;
					span:nth-child(1) {
						color: #0E667D;
						font-size: 12px;
					}
					span:nth-child(2) {
						color: #0E667D;
						font-size: 12px;
					}
				}
				.about_more:hover {
					opacity: 0.9;
				}
			}
		}
		#system {
			padding: 30px 0;
			margin: 0;
			overflow: hidden;
			background: none;
			width: 100%;
			position: relative;
			order: 7;
			height: auto;
			.system_item {
				padding: 0;
				display: flex;
				width: 100%;
				position: relative;
				flex-wrap: wrap;
				.system_title_box {
					padding: 0 0 0 30px;
					margin: 0 0 20px 0;
					color: #fff;
					background: url(http://codegen.caihongy.cn/20250214/555fe47ac645441b9a9b0f549fd8c99c.png) no-repeat left center;
					width: 100%;
					line-height: 70px;
					text-align: left;
					.system_title {
						color: inherit;
						font-weight: 600;
						width: 100%;
						font-size: 22px;
					}
					.system_subtitle {
						margin: 0 0 10px;
						color: #999;
						display: none;
						width: 100%;
						font-size: 20px;
						line-height: 1.5;
						text-align: center;
					}
				}
				.system_img {
					border: none;
					padding: 0;
					grid-template-columns: 1fr 1fr;
					grid-template-rows: 1fr 1fr;
					display: grid;
					gap: 20px;
					width: 560px;
					height: 400px;
					img:nth-child(1) {
						grid-row: 1 / 2;
						border-radius: 10px;
						margin: 0;
						object-fit: cover;
						display: block;
						width: 270px;
						grid-column: 1 / 2;
						height: 190px;
					}
					img:nth-child(2) {
						grid-row: 1 / 3;
						border-radius: 10px;
						margin: 0;
						object-fit: cover;
						display: block;
						width: 100%;
						grid-column: 2 / 3;
						height: 400px;
					}
					img:nth-child(3) {
						grid-row: 2 / 3;
						border-radius: 10px;
						margin: 0;
						object-fit: cover;
						display: block;
						width: 100%;
						grid-column: 1 / 2;
						height: 190px;
					}
				}
				.system_content {
					padding: 50px;
					margin: 0 0 0 30px;
					color: #fff;
					display: flex;
					letter-spacing: 1px;
					font-size: 16px;
					overflow: hidden;
					background: #80BE1B;
					flex: auto;
					width: 0;
					justify-content: flex-start;
					align-items: flex-start;
					height: auto;
				}
				.system_idea1 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_idea2 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_idea3 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_idea4 {
					background: url(http://codegen.caihongy.cn/20201114/7856ba26477849ea828f481fa2773a95.jpg) 0% 0% / cover no-repeat;
					display: none;
					width: 285px;
					height: 100px;
				}
				.system_more {
					border: 0;
					cursor: pointer;
					margin: 0;
					top: 0;
					background: #fff;
					display: none;
					width: 80px;
					line-height: 32px;
					position: absolute;
					right: 0;
					text-align: center;
					span:nth-child(1) {
						color: #0E667D;
						font-size: 12px;
					}
					span:nth-child(2) {
						color: #0E667D;
						font-size: 12px;
					}
				}
				.system_more:hover {
					opacity: 0.9;
				}
			}
		}
		.recommend {
			padding: 30px 0;
			margin: 0;
			background: none;
			width: 100%;
			position: relative;
			order: 4;
			.recommend_title_box {
				padding: 0 0 0 30px;
				margin: 0 0 20px 0;
				color: #fff;
				background: url(http://codegen.caihongy.cn/20250214/555fe47ac645441b9a9b0f549fd8c99c.png) no-repeat left center;
				font-weight: 600;
				width: 100%;
				font-size: 22px;
				line-height: 70px;
				text-align: left;
				.recommend_title {
					color: #fff;
					font-weight: 600;
					font-size: 22px;
				}
				.recommend_subhead {
					margin: 0 0 10px;
					color: #999;
					display: none;
					width: 100%;
					font-size: 20px;
					line-height: 1.5;
					text-align: center;
				}
			}
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
			
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list20 {
				margin: 0 auto;
				overflow: hidden;
				background: none;
				width: 100%;
				clear: both;
				.list-body {
					margin: 0 auto;
					display: flex;
					width: 100%;
					justify-content: space-between;
					position: relative;
					flex-wrap: wrap;
					.list-item {
						border: 10px solid #fff;
						margin: 0 0 15px;
						z-index: 99;
						overflow: hidden;
						width: calc(25% - 10px);
						position: relative;
						height: 300px;
						.img {
							border: 10px solid #fff;
							width: 100%;
							height: 100%;
							img {
								object-fit: cover;
								width: 100%;
								height: 100%;
							}
						}
						.infoBox {
							padding: 10px 0px;
							bottom: -100%;
							display: flex;
							transition: all 0.5s;
							flex-wrap: wrap;
							flex-direction: column;
							left: 0px;
							background: rgba(255, 255, 255, .8);
							width: 100%;
							justify-content: center;
							align-items: center;
							position: absolute;
							text-align: center;
							.name {
								padding: 0px 10px;
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								display: block;
								font-size: 16px;
								text-overflow: ellipsis;
							}
							.price {
								padding: 0px 10px;
								color: #f00;
								font-size: 16px;
							}
							.time_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.publisher_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.like_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.collect_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
							.view_item {
								padding: 0;
								.icon {
									margin: 0 2px 0 0;
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.label {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
						}
					}
					.list-item:hover {
						border: 10px solid #339933;
						.img {
							border: 10px solid #68bf68;
							img {
								transform: scale(0.96);
								transition: all 0.5s ease-out;
							}
						}
						.infoBox {
							bottom: 0px;
							background: rgba(0, 0, 0, .5);
							height: 100%;
						}
					}
				}
			}
			.moreBtn {
				border: 0;
				cursor: pointer;
				margin: 0;
				color: #fff;
				display: block;
				font-size: 16px;
				line-height: 70px;
				right: 0;
				top: 30px;
				background: #80BE1B;
				width: 150px;
				position: absolute;
				text-align: center;
				height: 70px;
				.text {
					color: inherit;
					font-size: inherit;
				}
				.icon {
					color: inherit;
					font-size: inherit;
				}
			}
		}
	}
</style>
