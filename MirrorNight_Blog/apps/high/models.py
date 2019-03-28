from django.db import models
from user.models import MyUsers
from blog.models import Categories, Archives
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Articles(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='所属分类')
    archive = models.ForeignKey(Archives, on_delete=models.CASCADE, verbose_name='所属归档')
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.ForeignKey(MyUsers, on_delete=models.CASCADE, verbose_name='作者')
    image = models.ImageField(blank=True, upload_to='high/article_image/', verbose_name='配图')
    content = RichTextUploadingField(verbose_name='正文')
    abstract = models.CharField(max_length=200, verbose_name='摘要')
    read_num = models.IntegerField(default=0, verbose_name='浏览量')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.category.title + "--" + self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='所属文章')
    content = RichTextUploadingField(verbose_name='内容')
    author = models.ForeignKey(MyUsers, on_delete=models.CASCADE, verbose_name='作者')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    def __str__(self):
        return self.article.title + "--" + self.author.username + "--" + str(self.add_time)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name


# 同步删除Articles中的上传文件
@receiver(pre_delete, sender=Articles)
def delete_articles(sender, instance, **kwargs):
    instance.image.delete(False)