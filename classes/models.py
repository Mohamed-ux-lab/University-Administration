from django.db import models


# Todo Cree le models d'une classe.

class Classes(models.Model):
    niveau = models.CharField(max_length=25)

    def __str__(self):
        return self.niveau
