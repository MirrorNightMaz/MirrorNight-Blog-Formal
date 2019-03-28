from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

# 用户头像的动态上传路径
def head_portrait_upload_to(instance, filename):
    return 'user/head_portrait/' + instance.username + '/' + filename


class MyUsers(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    head_portrait = models.ImageField(upload_to=head_portrait_upload_to, blank=True, default='user/head_portrait/default.jpg', verbose_name='头像')
    introduce = models.CharField(max_length=200, blank=True, null=True, verbose_name='自我介绍')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class EmailVerificationCodes(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    type = models.IntegerField(choices=((1, '账号激活'), (2, '找回密码')), verbose_name='验证码类型')
    code = models.CharField(max_length=100, verbose_name='验证码')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')
    duration = models.IntegerField(default=10, verbose_name='有效时长(分钟)')

    def __str__(self):
        return str(self.user_id) + "--" + str(self.type) + "--" + self.code + "--" + str(self.send_time)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


# 同步删除MyUsers中的上传文件
@receiver(pre_delete, sender=MyUsers)
def delete_myusers(sender, instance, **kwargs):
    if instance.head_portrait.name != 'user/head_portrait/default.jpg':
        instance.head_portrait.delete(False)