from django.shortcuts import render, get_object_or_404
from .models import Etudiant
from filiere.models import Filiere
from classes.models import Classes


def show(request):
    return render(request, '', context={'etudiants': Etudiant.objects.all()})


def add(request):
    pass


def choix_disponible(request):
    filieres = Filiere.objects.all()
    classes = Classes.object.all()
    context = {"filieres": filieres, "classes": classes}
    return render(request, context)


def delete(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    etudiant.delete()
    return render(request, '')


def modify(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    pass


def showone(request, etudiant_id):
    context = {"etudiant": get_object_or_404(Etudiant, pk=etudiant_id)}
    return render(request, '', context)
