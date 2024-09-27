from django.contrib import admin
from django.urls import path

import classes.views as class_view
import etudiant.views as etudiant_view
import professeur.views as professeur_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', class_view.index, name='index'),
    path('etudiant/', etudiant_view.show, name='etudiant'),
    path('ajouterEtudiant/', etudiant_view.add, name='ajouteretudiant'),
    path('voirEtudiant/<int:etudiant_id>', etudiant_view.showone, name='showone'),
    path('professeur/', professeur_view.show, name='professeur'),
    path('addProfesseur', professeur_view.add, name='addProfesseur'),
    path('voirProf/<int:professeur_id>', professeur_view.showone, name='showoneprof'),
    path('modifierProf/<int:professeur_id>', professeur_view.modify, name='modifierprof'),
]
