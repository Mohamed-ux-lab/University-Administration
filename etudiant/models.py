from django.db import models

from classes.models import Classes
from filiere.models import Filiere


# Todo -Creé le models etudiant.

class Etudiant(models.Model):
    nom = models.CharField(max_length=125)
    prenom = models.CharField(max_length=125)
    age = models.IntegerField(default=1)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"