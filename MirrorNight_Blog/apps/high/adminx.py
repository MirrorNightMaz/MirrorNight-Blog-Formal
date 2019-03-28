import xadmin
from .models import Articles, Comments


class ArticlesAdmin(object):
    list_display = ['title', 'category', 'archive', 'read_num', 'add_time', 'update_time']
    list_filter = ['title', 'category__title', 'archive__title', 'read_num', 'add_time', 'update_time']
    search_fields = ['title', 'category__title']
    ordering = ['-add_time']


class CommentsAdmin(object):
    list_display = ['article', 'author', 'add_time']
    list_filter = ['article__title', 'author__username', 'add_time']
    search_fields = ['article__title', 'author__username']
    ordering = ['-add_time']


xadmin.site.register(Articles, ArticlesAdmin)
xadmin.site.register(Comments, CommentsAdmin)