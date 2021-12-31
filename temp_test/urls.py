from django.contrib import admin
from django.urls import path, include
'''
这里我们发现，当temp_app不需要urls.py ，我们一般从views.py中导入函数
           当temp_app需要urls。py, 我们需要再temp_test中的urls.py指向temp_app的urls.py
'''
# 导入项目应用下视图函数中定义的函数
# from temp_app.views import ind
urlpatterns = [
    path('admin/', admin.site.urls),

    # 这里一定要加上别名（index.html没有模板继承的不用）,在templates/index.html能用到别名
    # path('',ind)

    # 指向temp_app的路由文件urls.py
    path('',include(('temp_app.urls','temp_app'),namespace='temp_app'))
]
