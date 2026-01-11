<template>
	<div :style='{"width":"100%","padding":"20px","margin":"10px auto","position":"relative","background":"none","maxWidth":"1200px"}'>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="section-title" :style='{"padding":"0 0 0 90px","margin":"0 0 20px 0","color":"#fff","textAlign":"left","background":"url(http://codegen.caihongy.cn/20250215/e708fb800ede46ebb777ef963256613d.png) no-repeat left center","width":"100%","letterSpacing":"2px","lineHeight":"70px","fontSize":"22px","fontWeight":"600"}'>我的地址</div>
		<el-button type="primary" icon="el-icon-plus" @click="toAddAddr">添加新地址</el-button>
		<el-table
			:data="tableData"
			style="width: 100%">
			<el-table-column
				label="联系人"
				prop="name"
				width="100">
			</el-table-column>
			<el-table-column
				label="手机号"
				prop="phone"
				width="120">
			</el-table-column>
			<el-table-column
				label="地址"
				prop="address">
			</el-table-column>
			<el-table-column
				label="默认"
				prop="isdefault"
				width="80">
				<template slot-scope="scope">
					<el-tag :type="scope.row.isdefault === '是' ? 'primary' : 'success'" size="medium">{{ scope.row.isdefault }}</el-tag>
				</template>
			</el-table-column>
			<el-table-column label="操作">
				<template slot-scope="scope">
					<el-button
						size="mini"
						@click="handleEdit(scope.$index, scope.row)">编辑</el-button>
					<el-button
						size="mini"
						type="danger"
						@click="handleDelete(scope.$index, scope.row)">删除</el-button>
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
			@prev-click="prevClick"
			@size-change="sizeChange"
			@next-click="nextClick"
			></el-pagination>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				layouts: '',
				tableData: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1
			}
		},
		created() {
			this.getAddr(1);
		},
		methods: {
			backClick() {
				this.$router.push('/index/center')
			},
			getAddr(page) {
				this.$http.get('address/list', {params: {page, limit: this.pageSize, userid: Number(localStorage.getItem('frontUserid'))}}).then(res => {
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
				this.getAddr(page);
			},
			prevClick(page) {
				this.getAddr(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getAddr(1);
			},
			nextClick(page) {
				this.getAddr(page);
			},
			handleEdit(index, row) {
				this.$router.push({path: '/index/shop-address/addOrUpdate', query: {id: row.id, editObj: JSON.stringify(row)}})
			},
			handleDelete(index, row) {
				this.$confirm('是否确认删除?', '提示', {
					confirmButtonText: '确定',
					cancelButtonText: '取消',
					type: 'warning'
				}).then(() => {
					let delIds = new Array();
					delIds.push(row.id);
					this.$http.post('address/delete', delIds).then(res => {
						if (res.data.code == 0) {
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									this.getAddr(1);
								}
							});
						}
					});
				});
			},
			toAddAddr() {
				this.$router.push('/index/shop-address/addOrUpdate');
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
