# ttsx1
1.0 项目创建: <br>
       /<space> 1 创建项目,修改setting中语言,时区,数据库,并在本地创建数据库,在项目的init文件下进行导包pymysql <br>
       /<space> <space> <space> <space> <space>  2 创建应用,添加url空列表,并把模块在set中进行添加配置(...apps) <br>
       /<space> <space> <space> <space>  3 项目下配置URL地址    url(r'^users/', include('apps.users.urls', namespace='users')),      # 用户模块 <br>
       /<space> <space> <space>  4 模块下配置URL地址   r"^index$",views.index, name="index" <br>
        /<space> <space> 5 views配置index函数.并render(request,"index.html") <br>
       /<space>  6 创建static静态文件目录 放入静态文件,并在SET中配置 STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")] <br>
2.0 model类创建
        /<space> <space> <space> <space> <space> 1 创建模型类基类basemodel,设为抽象类, <br>
       / <space> <space> <space> <space> 2 使用auth用户模块AbstractUser ,USER继承于basemodel和AbstractUser,并在set中设置AUTH_USER_MODEL = 'users.User' <br>
       / <space> <space> <space> 3 其他模型类创建并迁移 <br>
      / <space> <space>  4 后台使用富文本输入框,安装pip install django-tinymce==2.6.0    商品详情修改为HTMLfield便于输入商品详情 <br>
      / <space>  5 admin注册模型类在后台显示,admin.site.register(GoodsSPU) <br>

