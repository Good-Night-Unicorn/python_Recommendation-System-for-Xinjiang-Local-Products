<template>
	<div :style='{"width":"100%","padding":"20px","margin":"10px auto","position":"relative","background":"none","maxWidth":"1200px"}'>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="section-title" :style='{"padding":"0 0 0 90px","margin":"0 0 20px 0","color":"#fff","textAlign":"left","background":"url(http://codegen.caihongy.cn/20250215/e708fb800ede46ebb777ef963256613d.png) no-repeat left center","width":"100%","letterSpacing":"2px","lineHeight":"70px","fontSize":"22px","fontWeight":"600"}'>我的订单</div>
		<el-tabs v-model="activeName" @tab-click="handleClick">
			<el-tab-pane label="未支付" name="未支付"></el-tab-pane>
			<el-tab-pane label="已支付" name="已支付"></el-tab-pane>
			<el-tab-pane label="已发货" name="已发货"></el-tab-pane>
			<el-tab-pane label="已完成" name="已完成"></el-tab-pane>
			<el-tab-pane label="已退款" name="已退款"></el-tab-pane>
			<el-tab-pane label="已取消" name="已取消"></el-tab-pane>
		</el-tabs>
		<el-table :data="tableData" style="width: 100%">
			<el-table-column label="订单编号" prop="orderid"></el-table-column>
			<el-table-column label="商品" align="center" width="200px">
				<template slot-scope="scope">
					<div class="shangpin">
						<el-image style="width: 100px; height: 100px;flex: 1" :src="baseUrl + scope.row.picture" fit="fill"></el-image>
						<span style="margin-left: 10px;flex: 1" >{{ scope.row.goodname }}</span>
					</div>
				</template>
			</el-table-column>
			<el-table-column label="价格">
				<template slot-scope="scope">
					<span v-if="(scope.row.type == 1 || scope.row.type == 3)&&scope.row.price>0"><span :style='{"fontSize":"12px"}'>￥</span>{{ scope.row.price }}</span>
					<span v-if="scope.row.type == 2&&scope.row.price>0">{{ scope.row.price }}积分</span>
				</template>
			</el-table-column>
			<el-table-column label="数量" prop="buynumber"></el-table-column>
			<el-table-column label="总价">
				<template slot-scope="scope">
					<span v-if="(scope.row.type == 1 || scope.row.type == 3)&&scope.row.total>0"><span :style='{"fontSize":"12px"}'>￥</span>{{ scope.row.total }}</span>
					<span v-if="scope.row.type == 2&&scope.row.total>0">{{ scope.row.total }}积分</span>
				</template>
			</el-table-column>
			<el-table-column label="地址" prop="address"></el-table-column>
			<el-table-column label="电话" prop="tel"></el-table-column>
			<el-table-column label="收货人" prop="consignee"></el-table-column>
			<el-table-column label="下单时间" prop="addtime"></el-table-column>
			<el-table-column label="备注" prop="remark"></el-table-column>
			<el-table-column label="退货审核" prop="sfsh" v-if="changeReturnGoods()">
				<template slot-scope="scope">
					<el-tag type="success" v-if="scope.row.sfsh=='是'">已通过</el-tag>
					<el-tag type="warning" v-if="scope.row.sfsh=='待审核'">待审核</el-tag>
					<el-tag type="danger" v-if="scope.row.sfsh=='否'">未通过</el-tag>
				</template>
			</el-table-column>
			<el-table-column label="审核回复" prop="shhf"></el-table-column>
			<el-table-column label="操作" width="150">
				<template slot-scope="scope">
					<el-button v-show="activeName == '未支付'" type="success" :style='{"margin":"2px auto",}' size="mini" @click="pay(scope.row)">支付</el-button>
					<el-button v-show="activeName == '未支付'" type="danger" :style='{"margin":"2px auto",}' size="mini" @click="cancel(scope.row)">取消</el-button>
					<el-button v-show="activeName == '已支付'" type="danger" :style='{"margin":"2px auto",}' size="mini" @click="refund(scope.row)">{{scope.row.total>0?'退款':'退订'}}</el-button>
					<el-button v-if="scope.row.logistics" type="warning" :style='{"margin":"2px auto",}' size="mini" @click="logistics(scope.row)">物流</el-button>
					<el-button v-if="activeName == '已完成'&&scope.row.sfsh==''&&changeReturnGoods()" type="danger" :style='{"margin":"2px auto",}' size="mini" @click="returnGood(scope.row)">退货</el-button>
					<el-button v-show="activeName == '已完成'" type="primary" :style='{"margin":"2px auto",}' size="mini" @click="toDetail(scope.row)">评价</el-button>
					<el-button v-show="activeName == '已发货'" type="success" :style='{"margin":"2px auto",}' size="mini" @click="confirm(scope.row)">确认收货</el-button>
				</template>
			</el-table-column>
		</el-table>
		<el-pagination
			background
			id="pagination" class="pagination"
			:pager-count="7"
			:page-size="pageSize"
			:page-sizes="pageSizes"
			prev-text="<"
			next-text=">"
			:hide-on-single-page="true"
			:layout='["total","prev","pager","next","sizes","jumper"].join()'
			:total="total"
			:style='{"padding":"0","margin":"10px auto","whiteSpace":"nowrap","color":"#333","width":"100%","fontWeight":"500","order":"6","maxWidth":"1300px"}'
			@current-change="curChange"
			@size-change="sizeChange"
			@prev-click="prevClick"
			@next-click="nextClick"
			></el-pagination>

		<el-dialog title="物流信息" :visible.sync="logisticsVisible" width="30%">
			<div class="ql-snow ql-editor" v-html="logisticsText"></div>
		</el-dialog>
		<el-dialog title="退货理由" :visible.sync="returngoodVisible" width="30%">
			<el-input v-model="returnGoodForm.returnreason" type="textarea" placeholder="退货理由"></el-input>
			<div style="margin: 20px 0 0">
				<el-button type="primary" style="margin-left: 10px;" @click="returnGoodSave">确认</el-button>
				<el-button type="danger" style="margin-left: 10px;" @click="returngoodVisible=false">取消</el-button>
			</div>
		</el-dialog>
	
	</div>
</template>

<script>
	import config from '@/config/config'
	export default {
		data() {
			return {
				layouts: '',
				baseUrl: config.baseUrl,
				activeName: '未支付',
				tableData: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				session: {},
				userTableName: localStorage.getItem('UserTableName'),
				logisticsVisible: false,
				logisticsText: '',
				returngoodVisible: false,
				returnGoodForm: {},
			}
		},
		created() {
			this.getSession();
			this.getMyOrderList(1);
		},
		methods: {
			backClick() {
				this.$router.push('/index/center')
			},
			getSession() {
				this.$http.get(this.userTableName+'/session', {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.session = res.data.data;
					}
				});
			},
			handleClick(tab, event) {
				tab.activeName = event.target.outerText;
				this.getMyOrderList(1);
			},
			toDetail(row) {
				this.$router.push({path: '/index/'+row.tablename+'Detail', query: {id: row.goodid}});
			},
			handleAction(index, row) {
				if (index == '已支付' && this.session.money < row.total) {
					this.$message.error('余额不足，请先充值');
					return;
				}
	
				row.status = index;
				this.$http.post('orders/update', row).then(res => {
					if (res.data.code == 0) {
						if (index == '已支付') this.session.money -= row.total;
						if (index == '已退款' && row.type == 1) this.session.money += row.total;
						if (index == '已退款' && row.type == 2) this.session.jifen += row.total;
						if (index == '已支付' || index == '已退款') {
							this.session.money = this.session.money.toFixed(2);
							this.$http.post(this.userTableName+'/update', this.session).then(res => {});
						}
						this.$message({
							message: '操作成功',
							type: 'success',
							duration: 1500,
							onClose: () => {
								this.getMyOrderList(1);
							}
						});
					}
				});
			},
			// 退款
			refund(item) {
				this.$confirm(`${item.total>0?'确定退款吗？退款金额将返回账户中。':'是否退订？'}`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(() => {
					// 获取商品详情信息
					this.$http.get(item.tablename+'/info/'+item.goodid, {}).then(res => {
						// 商品信息
						let good = res.data.data;
						// 用户当前用户信息
						let table = localStorage.getItem("UserTableName");
						this.$http.get(table+'/session', {}).then(res => {
							this.user = res.data.data;
							if(item.type==1||item.type==3) {
								// 如果该商品存在积分
								if (good.jf) {
									this.user.jf = (Number(this.user.jf) - Number(item.total)).toFixed(2);
								}
								this.user.money = (Number(this.user.money) + Number(item.total)).toFixed(2);
								// 更新用户余额
								this.$http.post(table+'/update', this.user).then(res => {
									item.status = '已退款'
									localStorage.setItem('sessionForm',JSON.stringify(this.user))
									this.$http.post(`orders/update`, item).then(res => {
										if(item.tablename == `techan`){
											// 加回库存数量
											good.alllimittimes = good.alllimittimes + item.buynumber;
											this.$http.post(`techan/update`, good).then(res => {
											});
										}
										this.$message({
											message: `${item.total>0?'退款成功':'退订成功'}`,
											type: 'success',
											duration: 1500,
											onClose: () => {
												this.getMyOrderList(1);
											}
										});
									});
								});
							} else if(item.type==2) {
								this.user.jf = Number(this.user.jf) + Number(item.total);
								// 更新用户余额
								this.$http.post(table+'/update', this.user).then(res => {
									item.status = '已退款'
									localStorage.setItem('sessionForm',JSON.stringify(this.user))
									this.$http.post(`orders/update`, item).then(res => {
										if(item.tablename == `techan`){
											// 加回库存数量
											good.alllimittimes = good.alllimittimes + item.buynumber;
											this.$http.post(`techan/update`, good).then(res => {
											});
										}
										this.$message({
											message: `${item.total>0?'退款成功':'退订成功'}`,
											type: 'success',
											duration: 1500,
											onClose: () => {
												this.getMyOrderList(1);
											}
										});
									});
								});
							}
						});
					});
				});
			},
			//物流
			logistics(row) {
				this.logisticsText = row.logistics;
				this.logisticsVisible = true;
			},
			//退货
			returnGood(item){
				this.returnGoodForm = item
				this.returngoodVisible = true
			},
			returnGoodSave() {
				this.$confirm(`确定退货吗？审核通过后退款金额将返回账户中。`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(() => {
					this.returnGoodForm.sfsh = '待审核'
					this.$http.post(`orders/update`, this.returnGoodForm).then(res => {
						this.$message({
							message: '申请成功',
							type: 'success',
							duration: 1500,
							onClose: () => {
								this.getMyOrderList(1);
								this.returngoodVisible = false
							}
						});
					})
				});
			},

			// 支付
			pay(item) {
				// 获取商品详情信息
				this.$http.get(item.tablename+'/info/'+item.goodid, {}).then(res => {
					// 商品信息
					let data = res.data.data;
					// 用户当前用户信息
					let table = localStorage.getItem("UserTableName");
					this.$http.get(table+'/session', {}).then(res => {
						this.user = res.data.data;
						// 判断余额是否充足
						if (Number(this.user.money) < Number(item.total)) {
							this.$message({
								message: '余额不足，请先充值',
								type: 'error',
								duration: 1500
							});
							return
						}
						// 如果该商品存在积分
						if (data.jf) {
							this.user.jf = Number((Number(this.user.jf) + Number(item.total)).toFixed(2));
						}
						this.user.money = Number((Number(this.user.money) - Number(item.total)).toFixed(2));
						// 更新用户余额
						this.$http.post(table+'/update', this.user).then(res => {
							item.status = '已支付'
							localStorage.setItem('sessionForm',JSON.stringify(this.user))
							this.$http.post(`orders/update`, item).then(res => {
								this.$message({
									message: '支付成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.getMyOrderList(1);
									}
								});
							});
						});
					});
				});
			},
			confirm(item){
				this.$confirm(`是否确定收货？`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(() => {
					item.status = '已完成'
					this.$http.post(`orders/update`, item).then(res => {
						this.$message({
							message: '确认收货成功',
							type: 'success',
							duration: 1500,
							onClose: () => {
								this.getMyOrderList(1);
							}
						});
					});
				});
			},
			cancel(item){
				this.$confirm(`是否取消订单？`, "提示", {
					confirmButtonText: "确定",
					cancelButtonText: "取消",
					type: "warning"
				}).then(() => {
					item.status = '已取消'
					this.$http.post(`orders/update`, item).then(res => {
						// 获取商品详情信息
						this.$http.get(item.tablename+'/info/'+item.goodid, {}).then(res => {
							// 商品信息
							let good = res.data.data;
							if(item.tablename == `techan`){
								// 加回库存数量
								good.alllimittimes = good.alllimittimes + item.buynumber;
								this.$http.post(`techan/update`, good).then(res => {
								});
							}
							this.$message({
								message: '订单取消成功',
								type: 'success',
								duration: 1500,
								onClose: () => {
									this.getMyOrderList(1);
								}
							});
						});
					});
				});
			},
			getMyOrderList(page) {
				this.$http.get('orders/list', {params: {page, limit: this.pageSize,sort:'addtime',order:'desc', userid: Number(localStorage.getItem('frontUserid')), status: this.activeName}}).then(res => {
					if (res.data.code == 0) {
						this.tableData = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			curChange(page) {
				this.getMyOrderList(page);
			},
			prevClick(page) {
				this.getMyOrderList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getMyOrderList(1);
			},
			nextClick(page) {
				this.getMyOrderList(page);
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.section {
		width: 1000px;
		margin: 0 auto;
	}

	.shangpin {
		display: flex;
	}
	
</style>
