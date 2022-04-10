from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={
        'message':'初めてのDjangoアプリ作成',
        'members':['asuka','katatumuri','kanabun']
        }
    return render(request, 'mysns/index.html',context)