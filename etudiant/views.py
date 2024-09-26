from http.client import HTTPResponse

from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant
from .forms_etudiant import Formsetudiant


def show(request):
    return render(request, 'etudiant/etudiant.html', context={'etudiants': Etudiant.objects.all()})


def add(request):
    if request.method == 'POST':
        form = Formsetudiant(request.POST)
        if form.is_valid():
            form.save()  # Enregistrer l'étudiant avec la filière et la classe choisies

            return redirect('etudiant/etudiant.html')  # Rediriger vers une page de succès ou autre

    else:
        form = Formsetudiant()  # Afficher un formulaire vide si GET

    return render(request, 'etudiant/ajouterEtudiant.html', {'form': form})


def delete(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    etudiant.delete()
    return render(request, '')


def modify(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    pass


def showone(request, etudiant_id):
    context = {"etudiant": get_object_or_404(Etudiant, pk=etudiant_id)}
    return render(request, 'etudiant/onestudent.html', context)


def alletudiant(request):
    etudiant = Etudiant.objects.all()
    return render(request,'etudiant/etudiant.html', {'etudiants': etudiant})