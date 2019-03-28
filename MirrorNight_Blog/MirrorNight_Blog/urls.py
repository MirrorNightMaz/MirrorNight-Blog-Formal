"""MirrorNight_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# blog应用的自定义错误视图
handler400 = 'blog.views.my_custom_bad_request_view'
handler403 = 'blog.views.my_custom_permission_denied_view'
handler404 = 'blog.views.my_custom_page_not_found_view'
handler500 = 'blog.views.my_custom_error_view'

urlpatterns = [
    path('xadmin/op/MirrorNight/', xadmin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('user/', include('user.urls', namespace='user')),
    path('blog/', include('blog.urls', namespace='blog')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)