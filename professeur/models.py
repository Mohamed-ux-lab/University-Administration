from django.db import models

from classes.models import Classes
from filiere.models import Filiere


class Professeur(models.Model):
    nom = models.CharField(max_length=125)
    prenom = models.CharField(max_length=125)
    specialite = models.CharField(max_length=125)
    classes = models.ManyToManyField(Classes, related_name='professeur')
    filiere = models.ManyToManyField(Filiere, related_name='professeur')

    def __str__(self):
        return f"M. {self.nom} {self.prenom} professeur en {self.specialite}"
