from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .models import UserModel


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        error_msg = '用户名或口令出错'
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)

        if all((name, password)):
            user_qs = UserModel.objects.filter(name=name)
            if user_qs.exists():
                user = user_qs.first()
                if check_password(password, user.auth_key):
                    request.session['login_user'] = {
                        'id': user.id,
                        'name': user.phone
                    }

                    return redirect('/active/info/')
            else:
                error_msg = '用户名不存在，请先注册'

        return render(request, 'login.html', locals())