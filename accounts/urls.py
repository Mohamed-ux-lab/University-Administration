from django.urls import path
from . views import *

app_name = 'accounts'

urlpattern = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
]