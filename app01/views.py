from django.shortcuts import render,HttpResponse
from .models import UserInfo

# Create your views here.

def login(request):
    msg = None
    if request.method == 'POST':
        email = request.POST.get('email', default=None)
        password = request.POST.get('password',default=None)
        try:
            user = UserInfo.objects.get(email=email,password=password)
            print(user)
            HttpResponse('ok')
        except:
            msg = '用户名密码不正确'
    return render(request, "login.html", {'msg': msg})

