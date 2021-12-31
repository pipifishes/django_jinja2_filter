from  django.urls import path
from .views import ind
'''
初步理解，对于需要用到jinja2模板，需要再应用程序中新建urls.py
'''
urlpatterns = [
    path('',ind,name='inda'),
]
# newview是.views.py定义的视图函数；name是别名