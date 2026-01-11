<template>
	<div>

		<div class="container">
			<el-form class='rgs-form animate__animated animate__fadeInRight' v-if="pageFlag=='security1'">
				<div class="rgs-form2">
					<div class="title">找回密码</p></div>
					<el-form-item class="list-item" prop="username">
						<div class="label">账号：</div>
						<el-input v-model="forgetForm.username" placeholder="请您输入账号" />
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="getSecurity()">下一步</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
			<el-form class='rgs-form animate__animated animate__fadeInRight' v-if="pageFlag=='security2'">
				<div class="rgs-form2">
					<div class="title">找回密码</p></div>
					<el-form-item class="list-item" prop="pquestion">
						<div class="label">密保问题：</div>
						<el-input readonly v-model="registerForm.pquestion" placeholder="密保问题" />
					</el-form-item>
					<el-form-item class="list-item" prop="myanswer">
						<div class="label">密保答案：</div>
						<el-input v-model="registerForm.myanswer" placeholder="请您输入密保答案" />
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="validateSecurity()">下一步</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
			<el-form class='rgs-form animate__animated animate__fadeInRight' v-if="pageFlag=='security3'">
				<div class="rgs-form2">
					<div class="title">找回密码</p></div>
					<el-form-item class="list-item" prop="newpassword">
						<div class="label">新密码：</div>
						<el-input v-model="registerForm.newpassword" type="password" placeholder="请您输入新密码" />
					</el-form-item>
					<el-form-item class="list-item" prop="repassword">
						<div class="label">确认密码：</div>
						<el-input v-model="registerForm.repassword" type="password" placeholder="请您确认密码" />
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="updatePassword()">修改密码</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
			<el-form class='rgs-form animate__animated animate__fadeInRight' v-if="pageFlag=='register'" ref="registerForm" :model="registerForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">基于Python的新疆特产推荐系统的设计与实现注册</p></div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="yonghuzhanghao">
						<div class="label" :class="changeRules('yonghuzhanghao')?'required':''">用户账号：</div>
						<el-input v-model="registerForm.yonghuzhanghao"  placeholder="请输入用户账号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="yonghuxingming">
						<div class="label" :class="changeRules('yonghuxingming')?'required':''">用户姓名：</div>
						<el-input v-model="registerForm.yonghuxingming"  placeholder="请输入用户姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="nianling">
						<div class="label" :class="changeRules('nianling')?'required':''">年龄：</div>
						<el-input v-model.number="registerForm.nianling"  placeholder="请输入年龄" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="shouji">
						<div class="label" :class="changeRules('shouji')?'required':''">手机：</div>
						<el-input v-model="registerForm.shouji"  placeholder="请输入手机" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="pquestion">
						<div class="label" :class="changeRules('pquestion')?'required':''">密保问题：</div>
						<el-input v-model="registerForm.pquestion"  placeholder="请输入密保问题" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'" prop="panswer">
						<div class="label" :class="changeRules('panswer')?'required':''">密保答案：</div>
						<el-input v-model="registerForm.panswer"  placeholder="请输入密保答案" />
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="submitForm('registerForm')">注册</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</div>
</template>

<script>
	import 'animate.css';

export default {
    //数据集合
    data() {
		return {
            pageFlag : '',
			tableName: '',
			registerForm: {},
			forgetForm: {},
			rules: {},
			requiredRules: {},
            yonghuxingbieOptions: [],
		}
    },
	mounted() {
		if(this.$route.query.pageFlag=='register'){
			this.tableName = this.$route.query.role;
			if(this.tableName=='yonghu'){
				this.registerForm = {
					yonghuzhanghao: '',
					mima: '',
					mima2: '',
					yonghuxingming: '',
					xingbie: '',
					nianling: '',
					shouji: '',
					money: '',
					pquestion: '',
					panswer: '',
				}
			}
			if ('yonghu' == this.tableName) {
				this.rules.yonghuzhanghao = [{ required: true, message: '请输入用户账号', trigger: 'blur' }];
				this.requiredRules.yonghuzhanghao = [{ required: true, message: '请输入用户账号', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.yonghuxingming = [{ required: true, message: '请输入用户姓名', trigger: 'blur' }];
				this.requiredRules.yonghuxingming = [{ required: true, message: '请输入用户姓名', trigger: 'blur' }]
			}
			this.yonghuxingbieOptions = "男,女".split(',');
			if ('yonghu' == this.tableName) {
				this.rules.nianling = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
			}
			if ('yonghu' == this.tableName) {
				this.rules.shouji = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
			}
			if ('yonghu' == this.tableName) {
				this.rules.money = [{ required: true, validator: this.$validate.isNumber, trigger: 'blur' }];
			}
			if(`yonghu` == this.tableName){
				this.rules.pquestion = [{ required: true, message: '请输入密保问题', trigger: 'blur' }];
				this.requiredRules.pquestion = [{ required: true, message: '请输入密保问题', trigger: 'blur' }]
			}
			if(`yonghu` == this.tableName){
				this.rules.panswer = [{ required: true, message: '请输入密保答案', trigger: 'blur' }];
				this.requiredRules.panswer = [{ required: true, message: '请输入密保答案', trigger: 'blur' }]
			}
		}
	},
    created() {
		this.pageFlag = this.$route.query.pageFlag;
    },
    //方法集合
    methods: {
		changeRules(name){
			if(this.requiredRules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
        // 下二随

		// 多级联动参数


//获取密保问题
		getSecurity(){
			this.tableName = 'yonghu'
			if(!this.tableName) {
				this.$message.error("请选择角色");
				return false
			}
			if(!this.forgetForm.username){
				this.$message.error("请输入账号");
				return false
			}
			this.$http({
				url: this.tableName+`/security?username=` + this.forgetForm.username,
				method: "get",
			}).then(({
				data
			}) => {
				if (data.data && data.code === 0) {
					this.registerForm = data.data;
					this.pageFlag="security2"
				} else {
					if(!data.data) {
						this.$message.error("用户不存在");
					} else {
						this.$message.error(data.msg);
					}
				}
			});
		},
		//验证密保问题
		validateSecurity(){
			let that = this
			if(this.registerForm.panswer!=this.registerForm.myanswer){
				this.$message.error("答案输入不正确");
				return false
			}
			this.$message.success("答案正确");
			setTimeout(()=>{
				this.pageFlag="security3";
			},1000)
		},
		// 修改密码
		updatePassword() {
			if (!this.registerForm.newpassword) {
				this.$message.error("请输入新密码");
				return;
			}
			if (this.registerForm.newpassword != this.registerForm.repassword) {
				this.$message.error("两次密码输入不一致");
				return;
			}
			this.registerForm.mima = this.registerForm.newpassword;
			this.registerForm.password = this.registerForm.newpassword;
			this.$http.post(this.tableName+`/update`, this.registerForm).then(res => {
			  if (res.data.code === 0) {
				this.$message({
					message: "密码修改成功",
					type: "success",
					duration: 1500,
					onClose: () => {
					  this.$router.push('/login');
					}
				});
			  } else {
				this.$message.error(res.data.msg);
			  }
			});
		},
		submitForm(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					var url=this.tableName+"/register";
					if(`yonghu` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					this.$http.post(url, this.registerForm).then(res => {
						if (res.data.code === 0) {
							this.$message({
								message: '注册成功',
								type: 'success',
								duration: 1500,
								onClose: () => {
									this.$router.push('/login');
								}
							});
						} else {
							this.$message.error(res.data.msg);
						}
					});
				} else {
					return false;
				}
			});
		},
		resetForm(formName) {
			this.$refs[formName].resetFields();
		}
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
		background: url(http://codegen.caihongy.cn/20250214/0894f4d52f304dedb3b2427b02cbf318.png) center / 100% 100%;
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: flex-end;
		align-items: center;
		position: relative;
		background: url(http://codegen.caihongy.cn/20250214/0894f4d52f304dedb3b2427b02cbf318.png) center / 100% 100%;
		.rgs-form {
			padding: 30px 0;
			margin: 0;
			display: flex;
			border-color: rgb(134, 190, 125);
			min-height: 100vh;
			border-radius: 90px 0 0 90px;
			box-shadow: none;
			background: url(http://codegen.caihongy.cn/20250214/3b9d5a0c8c574096bc0d0773734e2bd3.png) no-repeat bottom right,#fff;
			width: 50%;
			border-width: 0 0 0 30px;
			align-items: center;
			border-style: solid;
			height: 100%;
			.rgs-form2 {
				margin: 0 auto;
				width: 400px;
				.title {
					margin: 0 0 10px 0;
					text-shadow: none;
					color: #80BE1B;
					font-weight: 700;
					width: 100%;
					font-size: 22px;
					line-height: 33px;
					text-align: center;
				}
				.subtitle {
					margin: 0 0 10px 0;
					text-shadow: 4px 4px 2px rgba(64, 158, 255, .5);
					color: rgba(64, 158, 255, 1);
					width: 100%;
					font-size: 20px;
					line-height: 44px;
					text-align: center;
				}
				.list-item {
					border: none;
					border-radius: 5px;
					padding: 0;
					box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
					margin: 0 0 30px 0;
					background: #fff;
					display: flex;
					width: 100%;
					align-items: center;
					/deep/.el-form-item__content {
						display: flex;
						width: 100%;
						.label {
							border-radius: 2px;
							margin: 8px 0 0;
							color: #1A4B0D;
							flex: none;
							background: none;
							width: 120px;
							font-size: 14px;
							line-height: 28px;
							text-align: center;
							height: 28px;
						}
						
						.required {
							position: relative;
						}
						.required::after{
							color: red;
							left: 2px;
							position: absolute;
							content: "*";
						}
						.el-input {
							width: 100%;
						}
						.el-input .el-input__inner {
							border: none;
							padding: 0 10px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.el-input .el-input__inner:focus {
							border: none;
							padding: 0 10px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.el-input-number {
							width: 100%;
						}
						.el-input-number .el-input__inner {
							text-align: left;
							border: none;
							padding: 0 10px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.el-input-number .el-input-number__decrease {
							display: none;
						}
						.el-input-number .el-input-number__increase {
							display: none;
						}
						.el-select {
							width: 100%;
						}
						.el-select .el-input__inner {
							border: none;
							padding: 0 10px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.el-select .el-input__inner:focus {
							border: none;
							padding: 0 10px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.el-date-editor {
							width: 100%;
						}
						.el-date-editor .el-input__inner {
							border: none;
							padding: 0 10px 0 40px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.el-date-editor .el-input__inner:focus {
							border: none;
							padding: 0 10px 0 40px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.el-upload--picture-card {
							background: transparent;
							border: 0;
							border-radius: 0;
							width: auto;
							height: auto;
							line-height: initial;
							vertical-align: middle;
						}
						.upload .upload-img {
							border: 1px dashed #000;
							cursor: pointer;
							border-radius: 8px;
							color: rgba(64, 158, 255, 1);
							width: 80px;
							font-size: 32px;
							line-height: 80px;
							text-align: center;
							height: 80px;
						}
						.el-upload-list .el-upload-list__item {
							border: 1px dashed #000;
							cursor: pointer;
							border-radius: 8px;
							color: rgba(64, 158, 255, 1);
							width: 80px;
							font-size: 32px;
							line-height: 80px;
							text-align: center;
							height: 80px;
							font-size: 14px;
							line-height: 1.8;
						}
						.el-upload .el-icon-plus {
							border: 1px dashed #000;
							cursor: pointer;
							border-radius: 8px;
							color: rgba(64, 158, 255, 1);
							width: 80px;
							font-size: 32px;
							line-height: 80px;
							text-align: center;
							height: 80px;
						}
						.el-upload__tip {
							color: #838fa1;
						}
						.emailInput {
							border: none;
							padding: 0 10px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.emailInput:focus {
							border: none;
							padding: 0 10px;
							outline: none;
							color: #000;
							flex: auto;
							background: none;
							width: 100%;
							font-size: 14px;
							height: 44px;
						}
						.el-btn {
							border: 0;
							cursor: pointer;
							padding: 0;
							margin: 0;
							color: #000;
							font-size: 12px;
							border-radius: 0 4px 4px 0;
							box-shadow: none;
							outline: none;
							background: #80BE1B;
							flex: none;
							width: 100px;
							height: 44px;
						}
						.el-btn:hover {
							opacity: 0.7;
						}
						
						.el-input__inner::placeholder {
							color: #CDCDCD;
							font-size: 14px;
						}
						input::placeholder {
							color: #CDCDCD;
							font-size: 14px;
						}
						.editor {
							width: 100%;
							height: auto;
						}
					}
				}
				.register-btn {
					padding: 0 0 20px 0;
					width: 100%;
				}
				.register-btn1 {
					width: 100%;
				}
				.register-btn2 {
					margin: 6px 0 0;
					width: 100%;
				}
				.register_btn {
					border: none;
					cursor: pointer;
					padding: 0 30px;
					margin: 0;
					color: #fff;
					font-weight: 600;
					letter-spacing: 2px;
					font-size: 20px;
					border-radius: 4px;
					outline: none;
					background: #80BE1B;
					width: 100%;
					height: 50px;
				}
				.register_btn:hover {
					opacity: 0.5;
				}
				.has_btn {
					cursor: pointer;
					padding: 0;
					color: #000;
					display: inline-block;
					text-decoration: none;
					font-size: 14px;
					line-height: 1;
				}
				.has_btn:hover {
					opacity: 0.5;
				}
			}
			.idea1 {
				background: red;
				display: none;
				width: 100%;
				height: 40px;
			}
			.idea2 {
				background: blue;
				display: none;
				width: 100%;
				height: 40px;
			}
		}
	}
	
	::-webkit-scrollbar {
		display: none;
	}
</style>
