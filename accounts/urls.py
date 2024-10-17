from django.contrib.auth import views as auth_views
from django.urls import path
from . views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login_user, name='login'),
    # path('register/', register_user, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
