from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('emailverificate/user_id=<int:user_id>/ctype=<int:ctype>/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<int:second>/<str:code>/', views.EmailVerificate.as_view(), name='emailverificate'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('forget/', views.Forget.as_view(), name='forget'),
    path('myself/', views.Myself.as_view(), name='myself'),
]