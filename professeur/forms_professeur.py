from django import forms

from classes.models import Classes
from filiere.models import Filiere
from professeur.models import Professeur


class FormsProf(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = ['nom', 'prenom', 'specialite', 'classes', 'filiere']

        classes = forms.ModelChoiceField(queryset=Classes.objects.all(), label='classes')
        filiere = forms.ModelChoiceField(queryset=Filiere.objects.all(), label='filiere')
