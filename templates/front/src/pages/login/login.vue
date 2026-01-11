<template>
	<div>
		<div class="login-container">
			<el-form ref="loginForm" :model="loginForm" :rules="rules" class="login_form animate__animated animate__fadeInRight">
				<div class="login_form2">
					<div class="login-title">基于Python的新疆特产推荐系统的设计与实现登录</div>
					<div v-if="loginType==1" class="list-item" prop="username">
						<div class="lable">
							账号：
						</div>
						<input v-model="loginForm.username" placeholder="请输入账号：">
					</div>
					<div v-if="loginType==1" class="list-item" prop="password">
						<div class="lable">
							密码：
						</div>
						<div class="password-box">
							<input v-model="loginForm.password" placeholder="请输入密码：" :type="showPassword?'text':'password'">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item select" v-if="roles.length>1">
						<div class="lable">
							角色：
						</div>
						<el-select v-model="loginForm.tableName" placeholder="请选择角色：" @change="selectChange">
							<el-option v-for="item,index in roles" :key="index" :label="item.roleName" :value="item.tableName" />
						</el-select>
					</div>

			
					<div class="list-btn">
						<el-button class="login_btn" v-if="loginType==1" @click="submitForm('loginForm')">登录</el-button>

						<div class="list-btn2">
							<router-link class="register_btn" :to="{path: '/register', query: {role: item.tableName,pageFlag:'register'}}" v-if="item.hasFrontRegister=='是'" v-for="(item, index) in roles" :key="index">注册{{item.roleName.replace('注册','')}}</router-link>
							<router-link class="resetpwd_btn" :to="{path: '/register', query: {pageFlag:'security1'}}">忘记密码？</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</template>

<script>
	import 'animate.css';
import menu from '@/config/menu'
export default {
	//数据集合
	data() {
		return {
            baseUrl: this.$config.baseUrl,
            loginType: 1,
			roleMenus: [],
			loginForm: {
				username: '',
				password: '',
				tableName: '',
			},
			role: '',
            roles: [],
			rules: {
				username: [
					{ required: true, message: '请输入账号', trigger: 'blur' }
				],
				password: [
					{ required: true, message: '请输入密码', trigger: 'blur' }
				]
			},
			codes: [{
				num: 1,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 2,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 3,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}, {
				num: 4,
				color: '#000',
				rotate: '10deg',
				size: '16px'
			}],
			flag: false,
			verifyCheck2: false,
			showPassword: false,
		}
	},
	components: {
	},
	created() {
		this.roleMenus = menu.list()
		for(let item in this.roleMenus) {
			if(this.roleMenus[item].hasFrontLogin=='是') {
				this.roles.push(this.roleMenus[item]);
			}
		}
		
	},
	mounted() {
	},
	//方法集合
	methods: {
		randomString() {
			var len = 4;
			var chars = [
				'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
				'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
				'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
				'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
				'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2',
				'3', '4', '5', '6', '7', '8', '9'
			]
			var colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
			var sizes = ['14', '15', '16', '17', '18']
			
			var output = []
			for (var i = 0; i < len; i++) {
				// 随机验证码
				var key = Math.floor(Math.random() * chars.length)
				this.codes[i].num = chars[key]
				// 随机验证码颜色
				var code = '#'
				for (var j = 0; j < 6; j++) {
					var key = Math.floor(Math.random() * colors.length)
					code += colors[key]
				}
				this.codes[i].color = code
				// 随机验证码方向
				var rotate = Math.floor(Math.random() * 45)
				var plus = Math.floor(Math.random() * 2)
				if (plus == 1) rotate = '-' + rotate
				this.codes[i].rotate = 'rotate(' + rotate + 'deg)'
				// 随机验证码字体大小
				var size = Math.floor(Math.random() * sizes.length)
				this.codes[i].size = sizes[size] + 'px'
			}
		},
		selectChange(e){
			for(let x in this.roles){
				if(this.roles[x].tableName == e){
					this.role = this.roles[x].roleName
				}
			}
		},
		submitForm(formName) {
			if (this.roles.length!=1) {
				if (!this.role) {
					this.$message.error("请选择登录用户类型");
					return false;
				}
			} else {
				this.role = this.roles[0].roleName;
				this.loginForm.tableName = this.roles[0].tableName;
			}
			if (!this.loginForm.username) {
				this.$message.error("请输入用户名");
				return;
			}
			if (!this.loginForm.password) {
				this.$message.error("请输入密码");
				return;
			}

			this.loginPost(formName)
		},
		loginPost(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					this.$http.get(`${this.loginForm.tableName}/login`, {params: this.loginForm}).then(res => {
						if (res.data.code === 0) {
							localStorage.setItem('frontToken', res.data.token);
							localStorage.setItem('UserTableName', this.loginForm.tableName);
							localStorage.setItem('username', this.loginForm.username);
							localStorage.setItem('frontSessionTable', this.loginForm.tableName);
							localStorage.setItem('frontRole', this.role);
							localStorage.setItem('keyPath', 0);
							this.$router.push('/');
							this.$message({
								message: '登录成功',
								type: 'success',
								duration: 1500,
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
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.login-container {
		background: url(http://codegen.caihongy.cn/20250214/0894f4d52f304dedb3b2427b02cbf318.png) center / 100% 100%;
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: flex-end;
		align-items: center;
		position: relative;
		background: url(http://codegen.caihongy.cn/20250214/0894f4d52f304dedb3b2427b02cbf318.png) center / 100% 100%;
		.login_form {
			padding: 0;
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
			.login_form2 {
				margin: 0 auto;
				width: 400px;
				.login-title {
					margin: 0 0 10px 0;
					text-shadow: none;
					color: #80BE1B;
					font-weight: 700;
					width: 100%;
					font-size: 22px;
					line-height: 33px;
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
					.lable {
						border-radius: 2px;
						margin: 0;
						color: #1A4B0D;
						flex: none;
						background: none;
						width: 100px;
						font-size: 14px;
						line-height: 28px;
						text-align: center;
					}
					input {
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
					input:focus {
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
					.password-box {
						display: flex;
						width: 100%;
						position: relative;
						align-items: center;
						input {
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
						input:focus {
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
						.iconfont {
							cursor: pointer;
							z-index: 1;
							color: #000;
							top: 0;
							font-size: 16px;
							line-height: 44px;
							position: absolute;
							right: 10px;
						}
					}
					input::placeholder {
						color: #CDCDCD;
						font-size: 14px;
					}
				}
				.select {
					border: none;
					border-radius: 5px;
					padding: 0;
					box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
					margin: 0 0 30px 0;
					background: #fff;
					display: flex;
					width: 100%;
					align-items: center;
					// select
					/deep/ .el-select {
						width: 100%;
					}
					/deep/ .el-select .el-input__inner {
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
					/deep/ .el-select .is-focus .el-input__inner {
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
					/deep/ .el-select .el-input__inner::placeholder{
						color: #CDCDCD;
						font-size: 14px;
					}
				}
				.list-btn {
					margin: 0;
					width: 100%;
					.login_btn {
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
					.login_btn:hover {
						opacity: 0.8;
					}
					.list-btn2 {
						margin: 20px 0 0;
						width: 100%;
						.register_btn {
							cursor: pointer;
							margin: 0 5px 10px;
							color: #000;
							background: none;
							text-decoration: none;
							font-size: 14px;
						}
						.register_btn:hover {
							opacity: 0.5;
						}
						.resetpwd_btn {
							cursor: pointer;
							margin: 0 5px 10px;
							color: #999;
							background: none;
							text-decoration: none;
							font-size: 14px;
							float: right;
						}
						.resetpwd_btn:hover {
							opacity: 0.5;
						}
					}
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
</style>
