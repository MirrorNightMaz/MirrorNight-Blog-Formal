from .models import MyUsers
from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=128, min_length=6, widget=forms.PasswordInput(attrs={'class': 'form-control user-name', 'placeholder': '密码'}), error_messages={'max_length': '密码过长！', 'min_length': '密码长度至少为6位！', 'required': '请填写密码！'})
    head_portrait = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'upload'}))

    class Meta:
        model = MyUsers
        fields = ['username', 'password', 'email', 'introduce', 'head_portrait']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control user-name', 'placeholder': '用户名'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mail', 'placeholder': '邮箱'}),
            'introduce': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': '自我介绍'}),
        }
        error_messages = {
            'username': {'max_length': '用户名过长！', 'required': '请填写用户名！'},
            'email': {'invalid': '邮箱不合法！', 'required': '请填写邮箱！'},
            'introduce': {'max_length': '自我介绍过长！'},
        }

    def clean_username(self):
        data = self.cleaned_data['username']
        user = MyUsers.objects.filter(username=data)
        if user:
            raise forms.ValidationError("用户名已被注册！")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        user = MyUsers.objects.filter(email=data)
        if user:
            raise forms.ValidationError("邮箱已被注册！")
        return data


class LoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control user-name', 'placeholder': '用户名或邮箱'}), error_messages={'required': '请输入用户名或邮箱！'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control user-name', 'placeholder': '密码'}), error_messages={'required': '请输入密码！'})
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class': 'form-control user-name', 'placeholder': '请输入验证码'}), error_messages={'required': '请输入验证码！', 'invalid': '验证码错误！'})


class ForgetForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control user-name', 'placeholder': '用户名'}), error_messages={'required': '请输入用户名！'})
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mail', 'placeholder': '邮箱'}), error_messages={'required': '请输入邮箱！', 'invalid': '邮箱不合法！'})
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class': 'form-control user-name', 'placeholder': '请输入验证码'}), error_messages={'required': '请输入验证码！', 'invalid': '验证码错误！'})


class ResetForm(forms.Form):
    password = forms.CharField(max_length=128, min_length=6, widget=forms.PasswordInput(attrs={'class': 'form-control user-name', 'placeholder': '重置密码'}), error_messages={'max_length': '密码过长！', 'min_length': '密码长度至少为6位！', 'required': '请填写密码！'})
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class': 'form-control user-name', 'placeholder': '请输入验证码'}), error_messages={'required': '请输入验证码！', 'invalid': '验证码错误！'})


class MyselfForm(forms.Form):
    username = forms.CharField(required=False, max_length=20, label='修改用户名', widget=forms.TextInput(attrs={'class': 'lowin-input', 'placeholder': '不予修改请留空'}), error_messages={'max_length': '用户名过长！'})
    email = forms.EmailField(required=False, label='修改邮箱', widget=forms.EmailInput(attrs={'class': 'lowin-input', 'placeholder': '不予修改请留空'}), error_messages={'invalid': '邮箱不合法！'})
    password = forms.CharField(required=False, max_length=128, min_length=6, label='修改密码', widget=forms.PasswordInput(attrs={'class': 'lowin-input', 'placeholder': '不予修改请留空'}), error_messages={'max_length': '密码过长！', 'min_length': '密码长度至少为6位！'})
    head_portrait = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'upload', 'placeholder': '不予修改请留空'}))

    def clean_username(self):
        data = self.cleaned_data['username']
        user = MyUsers.objects.filter(username=data)
        if user:
            raise forms.ValidationError("用户名已被注册！")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        user = MyUsers.objects.filter(email=data)
        if user:
            raise forms.ValidationError("邮箱已被注册！")
        return data