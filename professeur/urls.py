from django.urls import path
from .views import *

app_name = 'professeur'

urlpatterns = [
    path('professeur/', show, name='professeur'),
    path('addProfesseur', add, name='addProfesseur'),
    path('voirProf/<int:professeur_id>', showone, name='showoneprof'),
    path('modifierProf/<int:professeur_id>', modify, name='modifierprof'),
    path('deleteProf/<int:professeur_id>', delete, name='deleteprof'),
]
