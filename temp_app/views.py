from django.shortcuts import render
'''
利用 Python 的内建函数 locals() 。它返回的字典对所有局部变量的名称与值进行映射
'''
# Create your views here.
def ind(request):
    # return render(request,'index.html')

    value = {'name':'this is jinja2'}
    res = 5 < 3
    lista = [1,3,5,7,9]
    return render(request,'index.html',locals())








