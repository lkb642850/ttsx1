from django.contrib import admin

# Register your models here.
# 注册模型类，让它在后台显示
from apps.goods.models import GoodsSPU

admin.site.register(GoodsSPU)