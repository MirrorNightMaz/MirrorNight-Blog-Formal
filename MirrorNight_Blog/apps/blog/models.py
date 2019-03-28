from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    add_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Archives(models.Model):
    title = models.DateField(unique=True, verbose_name='日期')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = '归档'
        verbose_name_plural = verbose_name


class Contacts(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    contact = models.CharField(max_length=100, blank=True, null=True, verbose_name='联系方式')
    message = models.TextField(verbose_name='留言')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')
    has_read = models.BooleanField(choices=((True, '已读'), (False, '未读')), default=False, verbose_name='状态')

    def __str__(self):
        return self.name + "--" + str(self.send_time)

    class Meta:
        verbose_name = '联系'
        verbose_name_plural = verbose_name


class PhotoAlbums(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '相册'
        verbose_name_plural = verbose_name


# 照片的动态上传路径
def photo_upload_to(instance, filename):
    return 'blog/photo/' + instance.photoalbum.title + '/' + filename


class Photos(models.Model):
    photoalbum = models.ForeignKey(PhotoAlbums, on_delete = models.CASCADE, verbose_name='所属相册')
    photo = models.ImageField(upload_to=photo_upload_to, verbose_name='照片')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name='备注')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.photoalbum.title

    class Meta:
        verbose_name = '照片'
        verbose_name_plural = verbose_name


# 同步删除Photos中的上传文件
@receiver(pre_delete, sender=Photos)
def delete_photos(sender, instance, **kwargs):
    instance.photo.delete(False)