from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', lambda request: redirect('accounts:login')),
    path('', dashboard, name='dashboard'),
    path('etudiant/', include("etudiant.urls", namespace='etudiant')),
    path('professeur/', include("professeur.urls", namespace='professeur')),
    path('accounts/', include("accounts.urls", namespace='accounts')),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
