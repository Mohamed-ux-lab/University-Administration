from django.shortcuts import render, get_object_or_404
from .models import Etudiant


def show(request):
    return render(request, '', context={'etudiants': Etudiant.objects.all()})


def add(request):
    pass


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
