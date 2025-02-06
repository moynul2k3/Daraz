# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .forms import LoginForm
app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    
    path("user/signup/", views.signup, name="signup"),
    path('user/login/', auth_views.LoginView.as_view(template_name='mainapp/login.html', authentication_form=LoginForm), name='login'),
    path('user/logout/', views.logoutUser, name='logout'),
]
