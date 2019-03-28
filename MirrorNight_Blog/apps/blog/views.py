from appearance import models as am
from blog import models as bm
from high import models as hm
from user import models as um
from django.shortcuts import render
from django.views import View
from .forms import ContactForm, SearchForm, CommentForm
from django.db.models.aggregates import Count
from pure_pagination import Paginator, EmptyPage

# Create your views here.

# 自定义错误视图
def my_custom_bad_request_view(request):
    return render(request, '400.html')


def my_custom_permission_denied_view(request):
    return render(request, '403.html')


def my_custom_page_not_found_view(request):
    return render(request, '404.html')


def my_custom_error_view(request):
    return render(request, '500.html')


# about.html业务逻辑
class About(View):
    def get(self, request):
        words = am.Words.objects.all()
        return render(request, 'about.html', {'words': words})


# welcome.html业务逻辑
class Welcome(View):
    def get(self, request):
        words = am.Words.objects.all()
        return render(request, 'welcome.html', {'words': words})


# contact.html业务逻辑
class Contact(View):
    def get(self, request):
        contactform = ContactForm()
        return render(request, 'contact.html', {'contactform': contactform})

    def post(self, request):
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            return render(request, 'information.html', {'title': '联系', 'information': '已收到您的留言，谢谢！', 'type': 1})
        return render(request, 'contact.html', {'contactform': contactform})


# blog-list.html业务逻辑——分类列表
class CategoryList(View):
    def get(self, request):
        searchform = SearchForm()
        categories = bm.Categories.objects.annotate(num=Count('articles')).order_by('-add_time')
        page_id = request.GET.get('page', 1)
        p = Paginator(categories, 10, request=request)
        categories_page = p.page(page_id)
        return render(request, 'blog-list.html', {'searchform': searchform, 'things': categories_page, 'msg': '暂无分类', 'title': '分类', 'type': 1})

    def post(self, request):
        searchform = SearchForm(request.POST)
        searchform.is_valid()
        key_words = searchform.cleaned_data['key_words']
        categories = bm.Categories.objects.annotate(num=Count('articles')).filter(title__icontains=key_words).order_by('-add_time')
        page_id = request.GET.get('page', 1)
        p = Paginator(categories, 10, request=request)
        categories_page = p.page(page_id)
        return render(request, 'blog-list.html', {'searchform': searchform, 'things': categories_page, 'msg': '没有找到符合您搜索条件的分类！', 'title': '分类', 'type': 1})


# blog-list.html业务逻辑——归档列表
class ArchiveList(View):
    def get(self, request):
        archives = bm.Archives.objects.annotate(num=Count('articles')).order_by('-title')
        page_id = request.GET.get('page', 1)
        p = Paginator(archives, 10, request=request)
        archives_page = p.page(page_id)
        return render(request, 'blog-list.html', {'things': archives_page, 'msg': '暂无归档', 'title': '归档', 'type': 2})


# blog-list.html业务逻辑——文章列表
class ArticleList(View):
    def get(self, request, type, id):
        searchform = SearchForm()
        if type == 'category':
            category = bm.Categories.objects.filter(id=id)
            if category:
                title = category[0].title
                articles = category[0].articles_set.all().order_by('-add_time')
                page_id = request.GET.get('page', 1)
                p = Paginator(articles, 10, request=request)
                articles_page = p.page(page_id)
            else:
                return render(request, 'information.html', {'title': 'URL异常', 'information': '请访问有效的URL！', 'type': 1})
        elif type == 'archive':
            archive = bm.Archives.objects.filter(id=id)
            if archive:
                title = archive[0].title
                articles = archive[0].articles_set.all().order_by('-add_time')
                page_id = request.GET.get('page', 1)
                p = Paginator(articles, 10, request=request)
                articles_page = p.page(page_id)
            else:
                return render(request, 'information.html', {'title': 'URL异常', 'information': '请访问有效的URL！', 'type': 1})
        else:
            return render(request, 'information.html', {'title': 'URL异常', 'information': '请访问有效的URL！', 'type': 1})
        return render(request, 'blog-list.html', {'searchform': searchform, 'things': articles_page, 'msg': '暂无文章', 'title': title, 'type': 0, 'tt': type, 'id': id})

    def post(self, request, type, id):
        if type == 'category':
            category = bm.Categories.objects.filter(id=id)
            title = category[0].title
            articles = category[0].articles_set.all().order_by('-add_time')
        else:
            archive = bm.Archives.objects.filter(id=id)
            title = archive[0].title
            articles = archive[0].articles_set.all().order_by('-add_time')
        searchform = SearchForm(request.POST)
        searchform.is_valid()
        key_words = searchform.cleaned_data['key_words']
        articles = articles.filter(title__icontains=key_words).order_by('-add_time')
        page_id = request.GET.get('page', 1)
        p = Paginator(articles, 10, request=request)
        articles_page = p.page(page_id)
        return render(request, 'blog-list.html', {'searchform': searchform, 'things': articles_page, 'msg': '没有找到符合您搜索条件的文章！', 'title': title, 'type': 0, 'tt': type, 'id': id})


# photo-list.html业务逻辑
class PhotoAlbumList(View):
    def get(self, request):
        searchform = SearchForm()
        photoalbums = bm.PhotoAlbums.objects.annotate(num=Count('photos')).order_by('-add_time')
        page_id = request.GET.get('page', 1)
        p = Paginator(photoalbums, 10, request=request)
        photoalbums_page = p.page(page_id)
        return render(request, 'photo-list.html', {'searchform': searchform, 'photoalbums_page': photoalbums_page, 'msg': '暂无相册'})

    def post(self, request):
        searchform = SearchForm(request.POST)
        searchform.is_valid()
        key_words = searchform.cleaned_data['key_words']
        photoalbums = bm.PhotoAlbums.objects.annotate(num=Count('photos')).filter(title__icontains=key_words).order_by('-add_time')
        page_id = request.GET.get('page', 1)
        p = Paginator(photoalbums, 10, request=request)
        photoalbums_page = p.page(page_id)
        return render(request, 'photo-list.html', {'searchform': searchform, 'photoalbums_page': photoalbums_page, 'msg': '没有找到符合您搜索条件的相册！'})


# photo.html业务逻辑
class Photos(View):
    def get(self, request, id):
        photoalbum = bm.PhotoAlbums.objects.filter(id=id)
        if photoalbum:
            photos = photoalbum[0].photos_set.all().order_by('add_time')
            return render(request, 'photo.html', {'title': photoalbum[0].title, 'photos': photos})
        else:
            return render(request, 'information.html', {'title': 'URL异常', 'information': '请访问有效的URL！', 'type': 1})


# comment.html业务逻辑
class Comment(View):
    def get(self, request, id):
        commentform = CommentForm()
        article = hm.Articles.objects.filter(id=id)
        if article:
            comments = article[0].comments_set.all().order_by('-add_time')
            return render(request, 'comment.html', {'commentform': commentform, 'title': article[0].title, 'id': id, 'num': comments.count(), 'comments': comments})
        else:
            return render(request, 'information.html', {'title': 'URL异常', 'information': '请访问有效的URL！', 'type': 1})

    def post(self, request, id):
        if request.user.is_authenticated:
            commentform = CommentForm(request.POST)
            article = hm.Articles.objects.filter(id=id)
            comments = article[0].comments_set.all().order_by('-add_time')
            if commentform.is_valid():
                comment = commentform.save(commit=False)
                comment.article = article[0]
                comment.author = request.user
                comment.save()
                return render(request, 'information.html', {'title': '发表评论', 'information': '评论已发表！', 'type': 3, 'id': id})
            return render(request, 'comment.html', {'commentform': commentform, 'title': article[0].title, 'id': id, 'num': comments.count(), 'comments': comments})
        else:
            return render(request, 'information.html', {'title': '发表评论', 'information': '您尚未登录！', 'type': 2})


# 删除评论
class DeleteComment(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            comment = hm.Comments.objects.filter(id=id)
            if comment:
                if comment[0].author == request.user or request.user.username == 'MirrorNight':
                    comment[0].delete()
                    return render(request, 'information.html', {'title': '删除评论', 'information': '评论已删除！', 'type': 3, 'id': comment[0].article_id})
                else:
                    return render(request, 'information.html', {'title': '删除评论', 'information': '您无权删除他人评论！', 'type': 3, 'id': comment[0].article_id})
            else:
                return render(request, 'information.html', {'title': 'URL异常', 'information': '请访问有效的URL！', 'type': 1})
        else:
            return render(request, 'information.html', {'title': '删除评论', 'information': '您尚未登录！', 'type': 2})


# detail.html业务逻辑
class Detail(View):
    def get(self, request, id):
        article = hm.Articles.objects.filter(id=id)
        if article:
            me =um.MyUsers.objects.filter(username='MirrorNight')
            if me:
                if request.user != me[0]:
                    article[0].read_num += 1
                    article[0].save()
            else:
                article[0].read_num += 1
                article[0].save()
            return render(request, 'detail.html', {'article': article[0]})
        else:
            return render(request, 'information.html', {'title': 'URL异常', 'information': '请访问有效的URL！', 'type': 1})


# index.html业务逻辑
class Index(View):
    def get(self, request):
        words = am.Words.objects.all()
        banners = am.Banners.objects.all().order_by('add_time')
        articles = hm.Articles.objects.all().order_by('-add_time')[:3]
        return render(request, 'index.html', {'banners': banners, 'articles': articles, 'words': words})


# mobilemsg.html业务逻辑
class MobileMsg(View):
    def get(self, request):
        return render(request, 'mobilemsg.html')