from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('etudiant/', include("etudiant.urls", namespace='etudiant')),
    path('professeur/', include("professeur.urls", namespace='professeur')),
    path('accounts/', include("accounts.urls", namespace='accounts')),
]
