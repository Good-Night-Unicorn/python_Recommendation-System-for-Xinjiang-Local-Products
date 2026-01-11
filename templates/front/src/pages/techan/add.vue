<template>
	<div class="add-update-preview">
		<el-form
			class="add-update-form"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="120px"
			>
			<el-form-item class="add-item" label="商品编号" prop="shangpinbianhao">
				<el-input v-model="ruleForm.shangpinbianhao" placeholder="商品编号" disabled></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="商品名称" prop="shangpinmingcheng">
				<el-input v-model="ruleForm.shangpinmingcheng" 
					placeholder="商品名称" clearable :disabled=" false  ||ro.shangpinmingcheng"></el-input>
			</el-form-item>
			<el-form-item class="add-item"  label="类型" prop="leixing">
				<el-select v-model="ruleForm.leixing" placeholder="请选择类型" :disabled=" false  ||ro.leixing" >
					<el-option
						v-for="(item,index) in leixingOptions"
						:key="index"
						:label="item"
						:value="item">
					</el-option>
				</el-select>
			</el-form-item>
			<el-form-item class="add-item" label="图片" v-if="type!='cross' || (type=='cross' && !ro.tupian)" prop="tupian">
				<file-upload
					tip="点击上传图片"
					action="file/upload"
					:limit="3"
					:multiple="true"
					:fileUrls="ruleForm.tupian?ruleForm.tupian:''"
					@change="tupianUploadChange"
					></file-upload>
			</el-form-item>
			<el-form-item class="add-item" v-else label="图片" prop="tupian">
				<img v-if="ruleForm.tupian.substring(0,4)=='http'" class="upload-img" v-bind:key="index" :src="ruleForm.tupian.split(',')[0]">
				<img v-else class="upload-img" v-bind:key="index" v-for="(item,index) in ruleForm.tupian.split(',')" :src="baseUrl+item">
			</el-form-item>
			<el-form-item class="add-item" label="产地" prop="chandi">
				<el-input v-model="ruleForm.chandi" 
					placeholder="产地" clearable :disabled=" false  ||ro.chandi"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="规格" prop="guige">
				<el-input v-model="ruleForm.guige" 
					placeholder="规格" clearable :disabled=" false  ||ro.guige"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="单限" prop="onelimittimes">
				<el-input v-model.number="ruleForm.onelimittimes" 
					placeholder="单限" clearable :disabled=" false  ||ro.onelimittimes"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="库存" prop="alllimittimes">
				<el-input v-model.number="ruleForm.alllimittimes" 
					placeholder="库存" clearable :disabled=" false  ||ro.alllimittimes"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="价格" prop="price">
				<el-input-number v-model="ruleForm.price" placeholder="价格" :disabled=" false ||ro.price"></el-input-number>
			</el-form-item>
			<el-form-item class="add-item" label="商品详情" prop="shangpinxiangqing">
				<editor 
					v-model="ruleForm.shangpinxiangqing" 
					class="editor" 
					myQuillEditor="shangpinxiangqing"
					action="file/upload">
				</editor>
			</el-form-item>

			<el-form-item class="add-btn-item">
				<el-button class="submitBtn"  type="primary" @click="onSubmit">
					<span class="icon iconfont icon-kaitongfuwu"></span>
					<span class="text">提交</span>
				</el-button>
				<el-button class="closeBtn" @click="back()">
					<span class="icon iconfont icon-shanchu1"></span>
					<span class="text">取消</span>
				</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				id: '',
				baseUrl: '',
				ro:{
					shangpinbianhao : false,
					shangpinmingcheng : false,
					leixing : false,
					tupian : false,
					chandi : false,
					guige : false,
					shangpinxiangqing : false,
					onelimittimes : false,
					alllimittimes : false,
					thumbsupnum : false,
					crazilynum : false,
					clicktime : false,
					clicknum : false,
					discussnum : false,
					totalscore : false,
					price : false,
					onshelves : false,
					storeupnum : false,
				},
				type: '',
				userTableName: localStorage.getItem('UserTableName'),
				ruleForm: {
					shangpinbianhao: this.getUUID(),
					shangpinmingcheng: '',
					leixing: '',
					tupian: '',
					chandi: '',
					guige: '',
					shangpinxiangqing: '',
					onelimittimes: Number('5') ,
					alllimittimes: Number('500') ,
					thumbsupnum: '',
					crazilynum: '',
					clicktime: '',
					clicknum: '',
					discussnum: '',
					totalscore: '',
					price: '',
					onshelves: 1,
					storeupnum: '',
				},
				leixingOptions: [],


				rules: {
					shangpinbianhao: [
					],
					shangpinmingcheng: [
					],
					leixing: [
					],
					tupian: [
					],
					chandi: [
					],
					guige: [
					],
					shangpinxiangqing: [
					],
					onelimittimes: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					alllimittimes: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					thumbsupnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					crazilynum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					clicktime: [
					],
					clicknum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					discussnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					totalscore: [
						{ validator: this.$validate.isNumber, trigger: 'blur' },
					],
					price: [
						{ required: true, message: '价格不能为空', trigger: 'blur' },
						{ validator: this.$validate.isNumber, trigger: 'blur' },
					],
					onshelves: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					storeupnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
				},
				centerType: false,
			};
		},
		computed: {



		},
		components: {
		},
		created() {
			if(this.$route.query.centerType){
				this.centerType = true
			}
			//this.bg();
			let type = this.$route.query.type ? this.$route.query.type : '';
			this.init(type);
			this.baseUrl = this.$config.baseUrl;
		},
		methods: {
			getMakeZero(s) {
				return s < 10 ? '0' + s : s;
			},
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(type) {
				this.type = type;
				if(type=='cross'){
					var obj = JSON.parse(localStorage.getItem('crossObj'));
					for (var o in obj){
						if(o=='shangpinbianhao'){
							this.ruleForm.shangpinbianhao = obj[o];
							this.ro.shangpinbianhao = true;
							continue;
						}
						if(o=='shangpinmingcheng'){
							this.ruleForm.shangpinmingcheng = obj[o];
							this.ro.shangpinmingcheng = true;
							continue;
						}
						if(o=='leixing'){
							this.ruleForm.leixing = obj[o];
							this.ro.leixing = true;
							continue;
						}
						if(o=='tupian'){
							this.ruleForm.tupian = obj[o]?obj[o].split(",")[0]:'';
							this.ro.tupian = true;
							continue;
						}
						if(o=='chandi'){
							this.ruleForm.chandi = obj[o];
							this.ro.chandi = true;
							continue;
						}
						if(o=='guige'){
							this.ruleForm.guige = obj[o];
							this.ro.guige = true;
							continue;
						}
						if(o=='shangpinxiangqing'){
							this.ruleForm.shangpinxiangqing = obj[o];
							this.ro.shangpinxiangqing = true;
							continue;
						}
						if(o=='onelimittimes'){
							this.ruleForm.onelimittimes = obj[o];
							this.ro.onelimittimes = true;
							continue;
						}
						if(o=='alllimittimes'){
							this.ruleForm.alllimittimes = obj[o];
							this.ro.alllimittimes = true;
							continue;
						}
						if(o=='thumbsupnum'){
							this.ruleForm.thumbsupnum = obj[o];
							this.ro.thumbsupnum = true;
							continue;
						}
						if(o=='crazilynum'){
							this.ruleForm.crazilynum = obj[o];
							this.ro.crazilynum = true;
							continue;
						}
						if(o=='clicktime'){
							this.ruleForm.clicktime = obj[o];
							this.ro.clicktime = true;
							continue;
						}
						if(o=='clicknum'){
							this.ruleForm.clicknum = obj[o];
							this.ro.clicknum = true;
							continue;
						}
						if(o=='discussnum'){
							this.ruleForm.discussnum = obj[o];
							this.ro.discussnum = true;
							continue;
						}
						if(o=='totalscore'){
							this.ruleForm.totalscore = obj[o];
							this.ro.totalscore = true;
							continue;
						}
						if(o=='price'){
							this.ruleForm.price = obj[o];
							this.ro.price = true;
							continue;
						}
						if(o=='onshelves'){
							this.ruleForm.onshelves = obj[o];
							this.ro.onshelves = true;
							continue;
						}
						if(o=='storeupnum'){
							this.ruleForm.storeupnum = obj[o];
							this.ro.storeupnum = true;
							continue;
						}
					}
				}else if(type=='edit'){
					this.info()
				}
				// 获取用户信息
				this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						var json = res.data.data;
					}
				});
				this.$http.get('option/leixing/leixing', {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.leixingOptions = res.data.data;
					}
				});

				if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
					localStorage.removeItem('raffleType')
					setTimeout(() => {
						this.onSubmit()
					}, 300)
				}
			},

			// 多级联动参数
			// 多级联动参数
			info() {
				this.$http.get(`techan/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.ruleForm = res.data.data;
					}
				});
			},
			// 提交
			async onSubmit() {
				if(this.ruleForm.shangpinbianhao){
					this.ruleForm.shangpinbianhao = String(this.ruleForm.shangpinbianhao)
				}
				if(this.ruleForm.price<0){
					this.$message.error("价格不能输入负数");
					return
				}
				if(this.ruleForm.alllimittimes<0){
					this.$message.error("库存不能输入负数");
					return
				}
				if(this.ruleForm.onelimittimes<0){
					this.$message.error("单次购买不能输入负数");
					return
				}
				if(!this.ruleForm.id) {
					delete this.ruleForm.userid
				}
				await this.$refs["ruleForm"].validate(async valid => {
					if(valid) {
						if(this.type=='cross'){
							var statusColumnName = localStorage.getItem('statusColumnName');
							var statusColumnValue = localStorage.getItem('statusColumnValue');
							if(statusColumnName && statusColumnName!='') {
								var obj = JSON.parse(localStorage.getItem('crossObj'));
								if(!statusColumnName.startsWith("[")) {
									for (var o in obj){
										if(o==statusColumnName){
											obj[o] = statusColumnValue;
										}
									}
									var table = localStorage.getItem('crossTable');
									await this.$http.post(table+'/update', obj).then(res => {});
								}
							}
						}


						await this.$http.post(`techan/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(async res => {
							if (res.data.code == 0) {
								this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
										
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.$router.go(-1);
			},
			tupianUploadChange(fileUrls) {
				this.ruleForm.tupian = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
			},
		}
	};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.add-update-preview {
		padding: 20px;
		margin: 10px auto;
		max-width: 1200px;
		background: none;
		width: 100%;
		position: relative;
		.add-update-form {
			padding: 20px;
			background: #FFFFFF;
			display: flex;
			gap: 20px;
			width: 100%;
			position: relative;
			flex-wrap: wrap;
			.add-item.el-form-item {
				padding: 10px;
				margin: 0 0 10px;
				background: none;
				width: calc(50% - 10px);
				/deep/ .el-form-item__label {
					padding: 0 10px 0 0;
					color: #666;
					font-weight: 500;
					width: 120px;
					font-size: 14px;
					line-height: 40px;
					text-align: right;
				}
				/deep/ .el-form-item__content {
					margin-left: 120px;
				}
				.el-input {
					width: 100%;
				}
				.el-input /deep/ .el-input__inner {
					border: 0;
					border-radius: 4px;
					padding: 0 12px;
					box-shadow: 0 0 6px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-input /deep/ .el-input__inner[readonly="readonly"] {
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 0 12px;
					box-shadow: 0 0 6px rgba(85, 85, 127, 0.5);
					outline: none;
					color: rgba(85, 85, 127, 1.0);
					width: 400px;
					font-size: 14px;
					height: 40px;
				}
				.el-input-number /deep/ .el-input__inner {
					text-align: left;
					border: 0;
					border-radius: 4px;
					padding: 0 12px;
					box-shadow: 0 0 6px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-input-number /deep/ .is-disabled .el-input__inner {
					text-align: left;
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 0 12px;
					box-shadow: 0 0 6px rgba(85, 85, 127, 0.5);
					outline: none;
					color: rgba(85, 85, 127, 1.0);
					width: 400px;
					font-size: 14px;
					height: 40px;
				}
				.el-input-number /deep/ .el-input-number__decrease {
					display: none;
				}
				.el-input-number /deep/ .el-input-number__increase {
					display: none;
				}
				.el-select {
					width: 100%;
				}
				.el-select /deep/ .el-input__inner {
					border: 0;
					border-radius: 4px;
					padding: 0 10px;
					box-shadow: 0 0 6px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-select /deep/ .is-disabled .el-input__inner {
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 0 10px;
					box-shadow: 0 0 6px rgba(85, 85, 127, 0.5);
					outline: none;
					color: rgba(85, 85, 127, 1.0);
					background: #eee;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-date-editor {
					width: 100%;
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 0;
					border-radius: 4px;
					padding: 0 10px 0 30px;
					box-shadow: 0 0 6px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 0 10px 0 30px;
					box-shadow: 0 0 6px rgba(85, 85, 127, 0.5);
					outline: none;
					color: rgba(85, 85, 127, 1.0);
					background: #eee;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				/deep/ .el-upload--picture-card {
					background: transparent;
					border: 0;
					border-radius: 0;
					width: auto;
					height: auto;
					line-height: initial;
					vertical-align: middle;
				}
				/deep/ .upload .upload-img {
					border: 1px dashed rgba(64, 158, 255, 1);
					cursor: pointer;
					border-radius: 6px;
					color: rgba(64, 158, 255, 1);
					width: 80px;
					font-size: 32px;
					line-height: 80px;
					text-align: center;
					height: 80px;
				}
				/deep/ .el-upload-list .el-upload-list__item {
					border: 1px dashed rgba(64, 158, 255, 1);
					cursor: pointer;
					border-radius: 6px;
					color: rgba(64, 158, 255, 1);
					width: 80px;
					font-size: 32px;
					line-height: 80px;
					text-align: center;
					height: 80px;
					font-size: 14px;
					line-height: 1.8;
				}
				/deep/ .el-upload .el-icon-plus {
					border: 1px dashed rgba(64, 158, 255, 1);
					cursor: pointer;
					border-radius: 6px;
					color: rgba(64, 158, 255, 1);
					width: 80px;
					font-size: 32px;
					line-height: 80px;
					text-align: center;
					height: 80px;
				}
				/deep/ .el-upload__tip {
					color: #838fa1;
				}
				.el-textarea /deep/ .el-textarea__inner {
					border: 0;
					border-radius: 4px;
					padding: 12px;
					box-shadow: 0 0 6px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 120px;
				}
				.el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
					border: 0;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 12px;
					box-shadow: 0 0 6px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 120px;
				}
				/deep/ .el-input__inner::placeholder {
					color: #123;
					font-size: 16px;
				}
				/deep/ textarea::placeholder {
					color: #123;
					font-size: 16px;
				}
				.editor {
					background-color: #fff;
					border-radius: 0;
					padding: 0;
					box-shadow: 0 0 6px rgba(75,223,201,.5);
					margin: 0;
					width: 100%;
					border-color: #ccc;
					border-width: 0;
					border-style: solid;
					height: auto;
				}
				.upload-img {
					width: 150px;
					height: 150px;
				}
				.viewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 30px;
					border-radius: 4px;
					outline: none;
					background: #80BE1B;
					width: auto;
					height: 30px;
				}
				.viewBtn:hover {
					color: #666;
					background: rgba(64, 158, 255, .5);
				}
				.unviewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 30px;
					border-radius: 4px;
					outline: none;
					background: rgba(85, 85, 127, 1.0);
					width: auto;
					height: 30px;
				}
				.unviewBtn:hover {
					color: #666;
					background: rgba(85, 85, 127, .5);
				}
			}
			.add-btn-item {
				padding: 0;
				margin: 0;
				.submitBtn {
					border: 0;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 15px;
					margin: 0 20px 0 0;
					outline: none;
					background: #80BE1B;
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
					.icon {
						color: rgba(255, 255, 255, 1);
					}
					.text {
						color: rgba(255, 255, 255, 1);
					}
				}
				.submitBtn:hover {
					background: rgba(64, 158, 255, .5);
					.icon {
						color: #000;
					}
					.text {
						color: #000;
					}
				}
				.closeBtn {
					border: none;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 15px;
					margin: 0 20px 0 0;
					outline: none;
					background: #E8E8E8;
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
					.icon {
						color: #6E6E6E;
					}
					.text {
						color: #6E6E6E;
					}
				}
				.closeBtn:hover {
					color: rgba(64, 158, 255, .5);
					border-color: rgba(64, 158, 255, .5);
					.icon {
						color: rgba(64, 158, 255, 0.5);
					}
					.text {
						color: rgba(64, 158, 255, 0.5);
					}
				}
			}
		}
	}
	.el-date-editor.el-input {
		width: auto;
	}
</style>
