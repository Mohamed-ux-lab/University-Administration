from django.contrib import admin
from django.urls import path

import classes.views as class_view
import etudiant.views as etudiant_view
import filiere.views as filiere_view
import professeur.views as professeur_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', class_view.index, name='index')
]

# Todo installer htmx pour le rafraichissement sans recharger la page
