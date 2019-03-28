from .forms import RegisterForm, LoginForm, ForgetForm, ResetForm, MyselfForm
from . import models
from django.shortcuts import render
from django.views import View
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
import random
import datetime

# Create your views here.


# 生成邮箱验证码
def make_code(user_id, ctype):
    seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    code = ""
    for i in range(20):
        code += random.choice(seed)
    evc = models.EmailVerificationCodes()
    evc.user_id = user_id
    evc.type = ctype
    evc.code = code
    evc.save()
    return evc


# 发送邮箱验证邮件
def send_emailverificate_email(user_id, ctype, email):
    evc = make_code(user_id, ctype)
    url = "http://www.mirrornight.site/user/emailverificate/user_id=" + str(user_id) + "/ctype=" + str(ctype) + "/" + str(evc.send_time.year) + "/" + str(evc.send_time.month) + "/" + str(evc.send_time.day) + "/" + str(evc.send_time.hour) + "/" + str(evc.send_time.minute) + "/" + str(evc.send_time.second) + "/" + evc.code + "/"
    if ctype == 1:
        title = "MirrorNight&Blog账号激活邮件"
        content = "感谢您注册MirrorNight&Blog，请访问链接，激活您的账号：" + url
    else:
        title = "MirrorNight&Blog重置密码邮件"
        content = "感谢您注册MirrorNight&Blog，请访问链接，重置您的密码：" + url
    send_mail(
        title,
        content,
        'mirrornight_ma@sina.com',
        [email]
    )


# 邮箱验证以及相关业务逻辑
class EmailVerificate(View):
    def get(self, request, user_id, ctype, year, month, day, hour, minute, second, code):
        evc = models.EmailVerificationCodes.objects.filter(user_id=user_id, type=ctype, send_time__year=year, send_time__month=month, send_time__day=day, send_time__hour=hour, send_time__minute=minute, send_time__second=second, code=code)
        if evc:
            user = models.MyUsers.objects.get(id=user_id)
            now = datetime.datetime.now()
            expiration_time = evc[0].send_time + datetime.timedelta(minutes=evc[0].duration)
            if now < expiration_time:
                # 账号激活
                if ctype == 1:
                    user.is_active = True
                    user.save()
                    return render(request, 'information.html', {'title': '账号激活', 'information': '您的账号已成功激活！', 'type': 2})
                # 重置密码
                elif ctype == 2:
                    resetform = ResetForm()
                    return render(request, 'reset.html', {'resetform': resetform, 'expiration_time': expiration_time, 'user_id': user_id, 'ctype': ctype, 'year': year, 'month': month, 'day': day, 'hour': hour, 'minute': minute, 'second': second, 'code': code})
            else:
                send_emailverificate_email(user_id, ctype, user.email)
                # 账号激活
                if ctype == 1:
                    return render(request, 'information.html', {'title': '账号激活', 'information': '激活链接失效！账号激活邮件已重新发送至您的邮箱，请查收！', 'type': 1})
                # 重置密码
                elif ctype == 2:
                    return render(request, 'information.html', {'title': '重置密码', 'information': '重置密码链接失效！重置密码邮件已重新发送至您的邮箱，请查收！', 'type': 1})
        else:
            # 账号激活
            if ctype == 1:
                return render(request, 'information.html', {'title': '账号激活', 'information': '激活链接非法！请查正后再次尝试！', 'type': 1})
            # 重置密码
            elif ctype == 2:
                return render(request, 'information.html', {'title': '重置密码', 'information': '重置密码链接非法！请查正后再次尝试！', 'type': 1})
            else:
                return render(request, 'information.html', {'title': 'URL异常', 'information': '请访问有效的URL！', 'type': 1})

    def post(self, request, user_id, ctype, year, month, day, hour, minute, second, code):
        resetform = ResetForm(request.POST)
        if resetform.is_valid():
            password = resetform.cleaned_data['password']
            password = make_password(password)
            user = models.MyUsers.objects.get(id=user_id)
            user.password = password
            user.save()
            return render(request, 'information.html', {'title': '重置密码', 'information': '重置密码成功！', 'type': 2})
        evc = models.EmailVerificationCodes.objects.filter(user_id=user_id, type=ctype, send_time__year=year, send_time__month=month, send_time__day=day, send_time__hour=hour, send_time__minute=minute, send_time__second=second, code=code)
        expiration_time = evc[0].send_time + datetime.timedelta(minutes=evc[0].duration)
        return render(request, 'reset.html', {'resetform': resetform, 'expiration_time': expiration_time, 'user_id': user_id, 'ctype': ctype, 'year': year, 'month': month, 'day': day, 'hour': hour, 'minute': minute, 'second': second, 'code': code})


# register.html业务逻辑
class Register(View):
    def get(self, request):
        registerform = RegisterForm()
        return render(request, 'register.html', {'registerform': registerform})

    def post(self, request):
        registerform = RegisterForm(request.POST, request.FILES)
        if registerform.is_valid():
            rf = registerform.save(commit=False)
            rf.password = make_password(rf.password)
            rf.is_active = False
            rf.save()
            send_emailverificate_email(rf.id, 1, rf.email)
            return render(request, 'information.html', {'title': '账号激活', 'information': '账号激活邮件已发送至您的邮箱，请查收！十分钟内有效，如未收到邮件请检查是否被误判为垃圾邮件！', 'type': 1})
        return render(request, 'register.html', {'registerform': registerform})


# 重写ModelBackend类中的authenticate方法
class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = models.MyUsers.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# login.html业务逻辑
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'information.html', {'title': '用户登录', 'information': '您已登录，请勿重复登录！', 'type': 1})
        loginform = LoginForm()
        return render(request, 'login.html', {'loginform': loginform, 'msg': '欢迎回来！'})

    def post(self, request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username_or_email = loginform.cleaned_data['username_or_email']
            password = loginform.cleaned_data['password']
            user = authenticate(username=username_or_email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'information.html', {'title': '用户登录', 'information': '登录成功！', 'type': 1})
                else:
                    return render(request, 'information.html', {'title': '用户登录', 'information': '您的账号尚未激活！', 'type': 2})
            else:
                return render(request, 'login.html', {'loginform': loginform, 'msg': '用户名或密码错误！'})
        return render(request, 'login.html', {'loginform': loginform, 'msg': '欢迎回来！'})


# 注销
class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return render(request, 'information.html', {'title': '注销', 'information': '您已退出登录！', 'type': 2})
        return render(request, 'information.html', {'title': '注销', 'information': '您尚未登录！', 'type': 2})


# forget.html业务逻辑
class Forget(View):
    def get(self, request):
        forgetform = ForgetForm()
        return render(request, 'forget.html', {'forgetform': forgetform, 'msg': '务必正确填写您在注册时提供的邮箱，稍后您将以邮件形式收到重置密码的链接，注意查收！'})

    def post(self, request):
        forgetform = ForgetForm(request.POST)
        if forgetform.is_valid():
            username = forgetform.cleaned_data['username']
            email = forgetform.cleaned_data['email']
            user = models.MyUsers.objects.filter(username=username, email=email)
            if user:
                send_emailverificate_email(user[0].id, 2, email)
                return render(request, 'information.html', {'title': '重置密码', 'information': '重置密码邮件已发送至您的邮箱，请查收！十分钟内有效，如未收到邮件请检查是否被误判为垃圾邮件！', 'type': 1})
            else:
                return render(request, 'forget.html', {'forgetform': forgetform, 'msg': '用户名或邮箱错误！'})
        return render(request, 'forget.html', {'forgetform': forgetform, 'msg': '务必正确填写您在注册时提供的邮箱，稍后您将以邮件形式收到重置密码的链接，注意查收！'})


# myself.html业务逻辑
class Myself(View):
    def get(self, request):
        if request.user.is_authenticated:
            myselfform = MyselfForm()
            return render(request, 'myself.html', {'myselfform': myselfform})
        return render(request, 'information.html', {'title': '个人中心', 'information': '您尚未登录！', 'type': 2})

    def post(self, request):
        myselfform = MyselfForm(request.POST, request.FILES)
        if myselfform.is_valid():
            has_updated = False
            username = myselfform.cleaned_data['username']
            email = myselfform.cleaned_data['email']
            password = myselfform.cleaned_data['password']
            head_portrait = myselfform.cleaned_data['head_portrait']
            if username:
                request.user.username = username
                has_updated = True
            if email:
                request.user.email = email
                has_updated = True
            if password:
                request.user.password = password
                has_updated = True
            if head_portrait:
                request.user.head_portrait = head_portrait
                has_updated = True
            request.user.save()
            if has_updated:
                return render(request, 'information.html', {'title': '个人中心', 'information': '个人信息修改成功！', 'type': 1})
            return render(request, 'information.html', {'title': '个人中心', 'information': '个人信息未作修改！', 'type': 1})
        return render(request, 'myself.html', {'myselfform': myselfform})