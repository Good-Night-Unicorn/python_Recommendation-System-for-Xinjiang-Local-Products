#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    money=models.FloatField   (  null=True, unique=False,default='0', verbose_name='余额' )
    pquestion=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保问题' )
    panswer=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密保答案' )
    '''
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    yonghuxingming=VARCHAR
    xingbie=VARCHAR
    nianling=Integer
    shouji=VARCHAR
    money=Float
    pquestion=VARCHAR
    panswer=VARCHAR
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class leixing(BaseModel):
    __doc__ = u'''leixing'''
    __tablename__ = 'leixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    leixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='类型' )
    '''
    leixing=VARCHAR
    '''
    class Meta:
        db_table = 'leixing'
        verbose_name = verbose_name_plural = '类型'
class techan(BaseModel):
    __doc__ = u'''techan'''
    __tablename__ = 'techan'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='商品编号' )
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    leixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='类型' )
    tupian=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    chandi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='产地' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    shangpinxiangqing=models.TextField   (  null=True, unique=False, verbose_name='商品详情' )
    onelimittimes=models.IntegerField  (  null=True, unique=False, verbose_name='单限' )
    alllimittimes=models.IntegerField  (  null=True, unique=False, verbose_name='库存' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    totalscore=models.FloatField   (  null=True, unique=False,default='0', verbose_name='评分' )
    price=models.FloatField   ( null=False, unique=False, verbose_name='价格' )
    onshelves=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='是否上架(1:上架，0:下架)' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    shangpinbianhao=VARCHAR
    shangpinmingcheng=VARCHAR
    leixing=VARCHAR
    tupian=Text
    chandi=VARCHAR
    guige=VARCHAR
    shangpinxiangqing=Text
    onelimittimes=Integer
    alllimittimes=Integer
    thumbsupnum=Integer
    crazilynum=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    totalscore=Float
    price=Float
    onshelves=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'techan'
        verbose_name = verbose_name_plural = '特产'
class xinjiangtechan(BaseModel):
    __doc__ = u'''xinjiangtechan'''
    __tablename__ = 'xinjiangtechan'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255, null=True, unique=False, verbose_name='标题' )
    imgurl=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    jiage=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    procity=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地点' )
    shopname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商家名称' )
    salesnum=models.IntegerField  (  null=True, unique=False, verbose_name='销售量' )
    salestext=models.CharField ( max_length=255, null=True, unique=False, verbose_name='销售量描述' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商家账号' )
    shipingy=models.CharField ( max_length=255, null=True, unique=False, verbose_name='食品工艺' )
    baozhuanggg=models.CharField ( max_length=255, null=True, unique=False, verbose_name='包装规格' )
    detailurl=models.TextField   (  null=True, unique=False, verbose_name='详情地址' )
    '''
    title=VARCHAR
    imgurl=Text
    jiage=Float
    procity=VARCHAR
    shopname=VARCHAR
    salesnum=Integer
    salestext=VARCHAR
    nickname=VARCHAR
    shipingy=VARCHAR
    baozhuanggg=VARCHAR
    detailurl=Text
    '''
    class Meta:
        db_table = 'xinjiangtechan'
        verbose_name = verbose_name_plural = '新疆特产'
class cart(BaseModel):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='techan', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   (  null=True, unique=False, verbose_name='单价' )
    goodtype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品类型' )
    '''
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=Text
    buynumber=Integer
    price=Float
    goodtype=VARCHAR
    '''
    class Meta:
        db_table = 'cart'
        verbose_name = verbose_name_plural = '购物车表'
class orders(BaseModel):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    orderid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='订单编号' )
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='techan', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='商品图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   ( null=False, unique=False,default='0', verbose_name='价格' )
    total=models.FloatField   ( null=False, unique=False,default='0', verbose_name='总价格' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='支付类型' )
    status=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    address=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    tel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    consignee=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货人' )
    logistics=models.TextField   (  null=True, unique=False, verbose_name='物流' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    goodtype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品类型' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    role=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户角色' )
    returnreason=models.CharField ( max_length=255, null=True, unique=False, verbose_name='退货原因' )
    '''
    orderid=VARCHAR
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=Text
    buynumber=Integer
    price=Float
    total=Float
    type=Integer
    status=VARCHAR
    address=VARCHAR
    tel=VARCHAR
    consignee=VARCHAR
    logistics=Text
    remark=VARCHAR
    goodtype=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    role=VARCHAR
    returnreason=VARCHAR
    '''
    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '订单'
class address(BaseModel):
    __doc__ = u'''address'''
    __tablename__ = 'address'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    address=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收货人' )
    phone=models.CharField ( max_length=255,null=False, unique=False, verbose_name='电话' )
    isdefault=models.CharField ( max_length=255,null=False, unique=False, verbose_name='是否默认地址[是/否]' )
    '''
    userid=BigInteger
    address=VARCHAR
    name=VARCHAR
    phone=VARCHAR
    isdefault=VARCHAR
    '''
    class Meta:
        db_table = 'address'
        verbose_name = verbose_name_plural = '地址'
class chargerecord(BaseModel):
    __doc__ = u'''chargerecord'''
    __tablename__ = 'chargerecord'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    username=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
    role=models.CharField ( max_length=255,null=False, unique=False, verbose_name='角色' )
    amount=models.FloatField   ( null=False, unique=False, verbose_name='金额' )
    '''
    userid=BigInteger
    username=VARCHAR
    role=VARCHAR
    amount=Float
    '''
    class Meta:
        db_table = 'chargerecord'
        verbose_name = verbose_name_plural = '充值记录表'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class aboutus(BaseModel):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'aboutus'
        verbose_name = verbose_name_plural = '关于我们'
class systemintro(BaseModel):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'systemintro'
        verbose_name = verbose_name_plural = '系统简介'
class discusstechan(BaseModel):
    __doc__ = u'''discusstechan'''
    __tablename__ = 'discusstechan'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    score=models.FloatField   (  null=True, unique=False, verbose_name='评分' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶(1:置顶,0:非置顶)' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    score=Float
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discusstechan'
        verbose_name = verbose_name_plural = '特产评论表'
