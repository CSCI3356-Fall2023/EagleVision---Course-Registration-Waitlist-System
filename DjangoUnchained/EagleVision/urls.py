from django.urls import path
from . import views
from django.contrib.auth import views as login_views

urlpatterns = [
    path('', views.login, name='login'), 
    path('register/', views.register, name='register/login.html'),
    path('login/', login_views.LoginVew. as_view(template_name='templates/log'), name = 'login'),
]