from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('about/', views.About.as_view(), name='about'),
    path('welcome/', views.Welcome.as_view(), name='welcome'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('archives/', views.ArchiveList.as_view(), name='archives'),
    path('<str:type>_id=<int:id>/articles/', views.ArticleList.as_view(), name='articles'),
    path('photoalbums/', views.PhotoAlbumList.as_view(), name='photoalbums'),
    path('photoalbum_id=<int:id>/photos/', views.Photos.as_view(), name='photos'),
    path('article_id=<int:id>/comments/', views.Comment.as_view(), name='comments'),
    path('delete/comment_id=<int:id>', views.DeleteComment.as_view(), name='deletecomment'),
    path('article/<int:id>/', views.Detail.as_view(), name='detail'),
    path('index/', views.Index.as_view(), name='index'),
    path('mobilemsg/', views.MobileMsg.as_view(), name='mobilemsg'),
]