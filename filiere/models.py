from django.db import models


class Filiere(models.Model):
    nom = models.CharField(max_length=125)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.nom
