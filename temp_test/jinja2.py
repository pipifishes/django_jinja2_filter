from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
'''
好像就是配置jinja2的环境
'''
#定义函数myreplace
def myreplace(l,old,new):
    return str(l).replace(old,new)

# 将jinja2模板设置到项目环境
def environment(**option):
    env = Environment(**option)
    env.globals.update({
        'static':staticfiles_storage.url,
        'url':reverse,
    })
    # 注册自定义过滤器myreplace
    env.filters['myreplace'] = myreplace

    return env