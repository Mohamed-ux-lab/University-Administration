from django.urls import path
from .views import *

app_name = 'etudiant'

urlpatterns = [
    path('etudiant/', show, name='etudiant'),
    path('ajouterEtudiant/', add, name='ajouteretudiant'),
    path('modifierEtudiant/<int:etudiant_id>', modify, name='modifieretudiant'),
    path('deleteEtudiant/<int:etudiant_id>', delete, name='deleteetudiant'),
    path('voirEtudiant/<int:etudiant_id>', showone, name='showone'),
]
