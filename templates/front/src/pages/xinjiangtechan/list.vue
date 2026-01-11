<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'Ξ'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div v-if="centerType" class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="list-preview">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="list-item">
					<div class="lable">标题：</div>
					<el-input v-model="formSearch.title" placeholder="标题" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-form-item class="list-item">
					<div class="lable">地点：</div>
					<el-input v-model="formSearch.procity" placeholder="地点" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-form-item class="list-item">
					<div class="lable">商家名称：</div>
					<el-input v-model="formSearch.shopname" placeholder="商家名称" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-button class="list-search-btn" v-if=" true " type="primary" @click="getList(1, curFenlei)">
					<i class="el-icon-search"></i>
					查询
				</el-button>
				<el-button class="list-add-btn" v-if="btnAuth('xinjiangtechan','新增')" type="primary" @click="add('/index/xinjiangtechanAdd')">
					<i class="el-icon-circle-plus-outline"></i>
					添加
				</el-button>
			</el-form>
			<div class="select2">
				<div class="select2-list" v-for="(item,index) in selectOptionsList" :key="index">
					<div class="label">{{item.name}}：</div>
					<div class="item-body">
						<div class="item" @click="selectClick2(item,-1)" :class="item.check ==-1 ? 'active' : ''">全部</div>
						<div class="item" @click="selectClick2(item,index1)" :class="item.check == index1 ? 'active' : ''" v-for="item1,index1 in item.list" :key="index1">{{item1}}</div>
					</div>
				</div>
			</div>
			<div class="list">
				<!-- 样式三 -->
				<div class="list3 index-pv1">
					<div v-for="(item, index) in dataList" :key="index" @click.stop="toDetail(item)" class="list-item animation-box">
						<div class="img">
							<img @click.stop="imgPreView(item.imgurl)" v-if="item.imgurl && item.imgurl.substr(0,4)=='http'&&item.imgurl.split(',w').length>1" :src="item.imgurl" class="image" />
							<img @click.stop="imgPreView(item.imgurl.split(',')[0])" v-else-if="item.imgurl && item.imgurl.substr(0,4)=='http'" :src="item.imgurl.split(',')[0]" class="image" />
							<img @click.stop="imgPreView(baseUrl + (item.imgurl?item.imgurl.split(',')[0]:''))" v-else :src="baseUrl + (item.imgurl?item.imgurl.split(',')[0]:'')" class="image" />
						</div>
						<div class="item-info">
							<div>
								<div class="name">{{item.title}}</div>
								<div class="name">价格:{{item.jiage}}</div>
								<div class="name">地点:{{item.procity}}</div>
								<div class="name">商家名称:{{item.shopname}}</div>
								<div class="time_item">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="label">发布时间：</span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
							</div>
							<div class="desc ql-snow ql-editor" v-html="item.detailurl"></div>
						</div>
					</div>
				</div>
			</div>

	
			<el-pagination
				background
				id="pagination"
				class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				prev-text="<"
				next-text=">"
				:hide-on-single-page="true"
				:layout='["total","prev","pager","next","sizes","jumper"].join()'
				:total="total"
				:page-sizes="pageSizes"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>
		</div>
		<el-dialog title="预览图" :visible.sync="previewVisible" width="50%">
			<img :src="previewImg" alt="" style="width: 100%;">
		</el-dialog>
	</div>
</template>
<script>
	export default {
		//数据集合
		data() {
			return {
				selectIndex2: 0,
				selectOptionsList: [],
				layouts: '',
				swiperIndex: -1,
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '新疆特产'
					}
				],
				formSearch: {
					title: '',
					procity: '',
					shopname: '',
				},
				fenlei: [],
				dataList: [],
				total: 1,
				pageSize: 4,
				pageSizes: [],
				totalPage: 1,
				curFenlei: '全部',
				isPlain: false,
				indexQueryCondition: '',
				timeRange: [],
				centerType:false,
				previewImg: '',
				previewVisible: false,
				sortType: 'id',
				sortOrder: 'desc',
			}
		},
		async created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0){
				this.centerType = true
			}
			this.baseUrl = this.$config.baseUrl;
			await this.getFenlei();
			let fenlei = '全部'
			if(this.$route.query.homeFenlei){
				fenlei = this.$route.query.homeFenlei
			}
			this.getList(1, fenlei);
		},
		watch:{
			$route(newValue){
				this.getList(1, newValue.query.homeFenlei);
			}
		},
		//方法集合
		methods: {
			selectClick2(row,index) {
				row.check = index
				if(index == -1){
					this.formSearch[row.tableName] = ''
				}else {
					this.formSearch[row.tableName] = row.list[index]
				}
				this.getList()
			},
			add(path) {
				let query = {}
				if(this.centerType){
					query.centerType = 1
				}
				this.$router.push({path: path,query:query});
			},
			async getFenlei() {
			},
			getList(page, fenlei, ref = '') {
				let params = {
					page,
					limit: this.pageSize,
				};
				let searchWhere = {};
				if (this.formSearch.title != '') searchWhere.title = '%' + this.formSearch.title + '%';
				if (this.formSearch.procity != '') searchWhere.procity = '%' + this.formSearch.procity + '%';
				if (this.formSearch.shopname != '') searchWhere.shopname = '%' + this.formSearch.shopname + '%';
				let user = JSON.parse(localStorage.getItem('sessionForm'))
				if (this.sortType) searchWhere.sort = this.sortType
				if (this.sortOrder) searchWhere.order = this.sortOrder
				this.$http.get(`xinjiangtechan/${this.centerType?'page':'list'}`, {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.dataList = res.data.data.list;
						this.total = Number(res.data.data.total);
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			curChange(page) {
				this.getList(page);
			},
			prevClick(page) {
				this.getList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getList(1);
			},
			nextClick(page) {
				this.getList(page);
			},
			imgPreView(url){
				this.previewImg = url
				this.previewVisible = true
			},
			toDetail(item) {
				let params = {
					id: item.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/xinjiangtechanDetail', query: params});
			},
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			backClick() {
				this.$router.push({path: '/index/center'});
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.list-preview {
		padding: 0;
		margin: 10px auto;
		flex-direction: column;
		max-width: 1300px;
		background: none;
		display: flex;
		width: 100%;
		position: relative;
		.list-form-pv {
			padding: 10px 0;
			margin: 20px 0 0;
			background: none;
			display: flex;
			gap: 10px 0;
			width: 100%;
			align-items: center;
			flex-wrap: wrap;
			height: auto;
			order: 1;
			.list-item {
				margin: 0 10px;
				/deep/.el-form-item__content {
					display: flex;
				}
				.lable {
					padding: 0 10px;
					color: #80BE1B;
					flex: none;
					display: inline-block;
					width: auto;
					line-height: 42px;
				}
				.el-input {
					width: 100%;
				}
				.datetimerange {
					border: 1px solid #56857A;
					border-radius: 8px;
					padding: 3px 10px;
					outline: none;
					background: #fff;
					width: auto;
					justify-content: center;
				}
				.el-input /deep/ .el-input__inner {
					border: 1px solid #80BE1B;
					border-radius: 8px;
					padding: 0 10px;
					margin: 0;
					outline: none;
					color: #333;
					width: 140px;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
				.el-select {
					width: 100%;
				}
				.el-select /deep/ .el-input__inner {
				}
				.el-date-editor {
					width: 100%;
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 1px solid #56857A;
					border-radius: 8px;
					padding: 0 30px;
					margin: 0;
					outline: none;
					color: #333;
					width: 140px;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
			}
			.list-search-btn {
				cursor: pointer;
				border: 0;
				border-radius: 4px;
				padding: 0px 15px;
				margin: 0 10px 0 0;
				outline: none;
				color: #fff;
				background: #86BE7D;
				width: auto;
				font-size: 14px;
				line-height: 42px;
				height: 42px;
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: 14px;
				}
			}
			.list-add-btn {
				cursor: pointer;
				border: 0;
				border-radius: 4px;
				padding: 0px 15px;
				margin: 0 10px 0 0;
				outline: none;
				color: #fff;
				background: #80BE1B;
				width: auto;
				font-size: 14px;
				line-height: 42px;
				height: 42px;
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: 14px;
				}
			}
		}
		.select2 {
			padding: 0;
			margin: 10px 0;
			background: #EAF4E9;
			width: 100%;
			height: auto;
			order: 2;
			.select2-list {
				border-radius: 0;
				padding: 6px 0;
				margin: 0;
				background: none;
				display: flex;
				width: 100%;
				border-color: #80BE1B;
				border-width: 0 0 5px 0;
				position: relative;
				border-style: solid;
				height: auto;
				.label {
					padding: 0 5px;
					color: #80BE1B;
					flex: none;
					display: inline;
					font-size: 14px;
					line-height: 32px;
					position: relative;
				}
				.item-body {
					display: flex;
					gap: 10px;
					width: 100%;
					flex-wrap: wrap;
					height: auto;
					.item {
						cursor: pointer;
						border: none;
						border-radius: 4px;
						padding: 0 5px;
						color: #80BE1B;
						background: none;
						font-size: 14px;
						line-height: 32px;
					}
					.item:hover {
						color: #fff;
						background: #80BE1B;
					}
					.item.active {
						color: #fff;
						background: #80BE1B;
					}
				}
			}
		}
		.list {
			margin: 0 0 10px;
			background: none;
			order: 5;
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
				
			.index-pv1 .animation-box:hover {
				transform: rotate(0) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
				
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list3 {
				border-radius: 10px;
				padding: 20px;
				margin: 20px 0 ;
				background: #fff;
				display: flex;
				gap: 20px;
				width: 100%;
				flex-wrap: wrap;
				height: auto;
				.list-item {
					cursor: pointer;
					padding: 10px;
					margin: 0;
					background: #f5f5f5;
					display: flex;
					width: calc(50% - 10px);
					font-size: 0;
					position: relative;
					height: auto;
					.img {
						overflow: hidden;
						.image {
							border: 1px solid #80BE1B;
							padding: 10px;
							object-fit: cover;
							display: block;
							width: 280px;
							height: 220px;
						}
					}
					.item-info {
						padding: 0 10px;
						overflow: hidden;
						flex: 1;
						display: flex;
						width: 0;
						height: auto;
						.name {
							padding: 0 10px;
							color: #333;
							font-size: 14px;
							border-color: #80BE1B;
							border-width: 0 0 1px 0;
							line-height: 36px;
							border-style: solid;
						}
						.price {
							padding: 0 10px;
							color: #f00;
							font-size: 16px;
							line-height: 1.5;
						}
						.time_item {
							padding: 0 10px;
							border-color: #80BE1B;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
						}
						.publisher_item {
							padding: 0 10px;
							border-color: #80BE1B;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
						}
						.like_item {
							padding: 0 10px;
							border-color: #80BE1B;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
						}
						.collect_item {
							padding: 0 10px;
							border-color: #80BE1B;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
						}
						.view_item {
							padding: 0 10px;
							border-color: #80BE1B;
							border-width: 0 0 1px 0;
							border-style: solid;
							.icon {
								margin: 0 2px 0 0;
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
							.label {
								color: #666;
								font-size: 12px;
								line-height: 1.5;
							}
							.text {
								color: #666;
								font-size: 12px;
								line-height: 28px;
							}
						}
					}
					.desc {
						color: #666;
						flex: auto;
						display: none;
						width: 50%;
						font-size: 12px;
						line-height: 1.5;
					}
				}
				.list-item:hover {
					background: #52bb9d;
					.item-info {
						.name {
							color: #fff;
						}
						.price {
							color: #fff;
						}
						.time_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
						.publisher_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
						.like_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
						.collect_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
						.view_item {
							.icon {
								color: #fff;
							}
							.label {
								color: #fff;
							}
							.text {
								color: #fff;
							}
						}
					}
					.desc {
						color: #fff;
					}
				}
			}
		}
	}
</style>
