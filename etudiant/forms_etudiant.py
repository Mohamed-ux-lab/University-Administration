from django import forms
from filiere.models import Filiere  # Import du modèle Filiere
from classes.models import Classes  # Import du modèle Classe
from .models import Etudiant  # Import du modèle Etudiant (dans cette application)


class Formsetudiant(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'age', 'filiere', 'classes']

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6', 'placeholder': 'Nom ...'}),
            'prenom': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6', 'placeholder': 'Prenom ...'})
        }

        filiere = forms.ModelChoiceField(queryset=Filiere.objects.all(), label='filiere')
        classes = forms.ModelChoiceField(queryset=Classes.objects.all(), label='classes')
