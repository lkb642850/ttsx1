# ttsx1
1.0 项目创建: <br>
---- 1 创建项目,修改setting中语言,时区,数据库,并在本地创建数据库,在项目的init文件下进行导包pymysql <br> 
---- 2 创建应用,添加url空列表,并把模块在set中进行添加配置(...apps) <br>
----3 项目下配置URL地址    url(r'^users/', include('apps.users.urls', namespace='users')),      # 用户模块 <br>
---- 4 模块下配置URL地址   r"^index$",views.index, name="index" <br>
----5 views配置index函数.并render(request,"index.html") <br>
----6 创建static静态文件目录 放入静态文件,并在SET中配置 STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")] <br>
2.0 model类创建
----1 创建模型类基类basemodel,设为抽象类, <br>
----2 使用auth用户模块AbstractUser ,USER继承于basemodel和AbstractUser,并在set中设置AUTH_USER_MODEL = 'users.User' <br>
---- 3 其他模型类创建并迁移 <br>
 ----4 后台使用富文本输入框,安装pip install django-tinymce==2.6.0    商品详情修改为HTMLfield便于输入商品详情 <br>
----  5 admin注册模型类在后台显示,admin.site.register(GoodsSPU) <br>
3.0 注册页面显示
---1 URL地址配置,VIEW函数配置,静态文件移动到template中 并加载静态文件,修改模板
