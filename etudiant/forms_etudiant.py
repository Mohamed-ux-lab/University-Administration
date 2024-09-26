from django import forms
from filiere.models import Filiere  # Import du modèle Filiere
from classes.models import Classes  # Import du modèle Classe
from .models import Etudiant  # Import du modèle Etudiant (dans cette application)


class Formsetudiant(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'age', 'filiere', 'classes']

        filiere = forms.ModelChoiceField(queryset=Filiere.objects.all(), label='filiere')
        classes = forms.ModelChoiceField(queryset=Classes.objects.all(), label='classes')
