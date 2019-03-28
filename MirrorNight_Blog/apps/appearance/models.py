from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

class Welcome_bg(models.Model):
    welcome_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '欢迎页面背景图'
        verbose_name_plural = verbose_name


class Banners(models.Model):
    banner = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '主页面轮播图'
        verbose_name_plural = verbose_name


class Newest_bg(models.Model):
    newest_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '主页面最新文章背景图'
        verbose_name_plural = verbose_name


class Declare_bg(models.Model):
    declare_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '主页面网站宣言背景图'
        verbose_name_plural = verbose_name


class Bloglist_bg(models.Model):
    bloglist_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '博客列表页面背景图'
        verbose_name_plural = verbose_name


class Detail_bg(models.Model):
    detail_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '文章详情页面背景图'
        verbose_name_plural = verbose_name


class Commenta_bg(models.Model):
    commenta_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '文章评论页面上部背景图'
        verbose_name_plural = verbose_name


class Commentb_bg(models.Model):
    commentb_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '文章评论页面下部背景图'
        verbose_name_plural = verbose_name


class Contact_bg(models.Model):
    contact_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '联系页面背景图'
        verbose_name_plural = verbose_name


class Login_bg(models.Model):
    login_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '登录页面背景图'
        verbose_name_plural = verbose_name


class Register_bg(models.Model):
    register_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '注册页面背景图'
        verbose_name_plural = verbose_name


class Forget_bg(models.Model):
    forget_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '忘记密码页面背景图'
        verbose_name_plural = verbose_name


class Reset_bg(models.Model):
    reset_bg = models.ImageField(upload_to='appearance/', verbose_name='图片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    def __str__(self):
        return str(self.add_time)

    class Meta:
        verbose_name = '重置密码页面背景图'
        verbose_name_plural = verbose_name


class Words(models.Model):
    welcome_title = models.CharField(max_length=100, verbose_name='欢迎页面标题')
    welcome_words = models.CharField(max_length=200, verbose_name='欢迎页面标语')
    declare_title = models.CharField(max_length=100, verbose_name='主页面网站宣言标题')
    declare_words = models.CharField(max_length=200, verbose_name='主页面网站宣言')
    about_words = models.CharField(max_length=200, verbose_name='关于页面自我介绍')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return str(self.update_time)

    class Meta:
        verbose_name = '文字外观项'
        verbose_name_plural = verbose_name


# 同步删除Welcome_bg中的上传文件
@receiver(pre_delete, sender=Welcome_bg)
def delete_welcome_bg(sender, instance, **kwargs):
    instance.welcome_bg.delete(False)


# 同步删除Banners中的上传文件
@receiver(pre_delete, sender=Banners)
def delete_banners(sender, instance, **kwargs):
    instance.banner.delete(False)


# 同步删除Newest_bg中的上传文件
@receiver(pre_delete, sender=Newest_bg)
def delete_newest_bg(sender, instance, **kwargs):
    instance.newest_bg.delete(False)


# 同步删除Declare_bg中的上传文件
@receiver(pre_delete, sender=Declare_bg)
def delete_declare_bg(sender, instance, **kwargs):
    instance.declare_bg.delete(False)


# 同步删除Bloglist_bg中的上传文件
@receiver(pre_delete, sender=Bloglist_bg)
def delete_bloglist_bg(sender, instance, **kwargs):
    instance.bloglist_bg.delete(False)


# 同步删除Detail_bg中的上传文件
@receiver(pre_delete, sender=Detail_bg)
def delete_detail_bg(sender, instance, **kwargs):
    instance.detail_bg.delete(False)


# 同步删除Commenta_bg中的上传文件
@receiver(pre_delete, sender=Commenta_bg)
def delete_commenta_bg(sender, instance, **kwargs):
    instance.commenta_bg.delete(False)


# 同步删除Commentb_bg中的上传文件
@receiver(pre_delete, sender=Commentb_bg)
def delete_commentb_bg(sender, instance, **kwargs):
    instance.commentb_bg.delete(False)


# 同步删除Contact_bg中的上传文件
@receiver(pre_delete, sender=Contact_bg)
def delete_contact_bg(sender, instance, **kwargs):
    instance.contact_bg.delete(False)


# 同步删除Login_bg中的上传文件
@receiver(pre_delete, sender=Login_bg)
def delete_login_bg(sender, instance, **kwargs):
    instance.login_bg.delete(False)


# 同步删除Register_bg中的上传文件
@receiver(pre_delete, sender=Register_bg)
def delete_register_bg(sender, instance, **kwargs):
    instance.register_bg.delete(False)


# 同步删除Forget_bg中的上传文件
@receiver(pre_delete, sender=Forget_bg)
def delete_forget_bg(sender, instance, **kwargs):
    instance.forget_bg.delete(False)


# 同步删除Reset_bg中的上传文件
@receiver(pre_delete, sender=Reset_bg)
def delete_reset_bg(sender, instance, **kwargs):
    instance.reset_bg.delete(False)