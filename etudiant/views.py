from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant
from .forms_etudiant import Formsetudiant


def show(request):
    return render(request, 'etudiant.html', context={'etudiants': Etudiant.objects.all()})



def add(request):
    if request.method == 'POST':
        form = Formsetudiant(request.POST)
        if form.is_valid():
            form.save()  # Enregistrer l'étudiant avec la filière et la classe choisies

            return redirect('etudiant:etudiant')  # Rediriger vers une page de succès ou autre

    else:
        form = Formsetudiant()  # Afficher un formulaire vide si GET

    return render(request, 'ajouterEtudiant.html', {'form': form})


def delete(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    etudiant.delete()
    return redirect('etudiant:etudiant')


def modify(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    if request.method == 'POST':
        form = Formsetudiant(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiant:etudiant')
    else:
        form = Formsetudiant(instance=etudiant)
    return render(request, 'modifieretudiant.html', {'form': form})


def showone(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    print(etudiant.id)
    return render(request, 'onestudent.html', {"etudiants": etudiant})


def alletudiant(request):
    etudiant = Etudiant.objects.all()
    return render(request, 'etudiant.html', {'etudiants': etudiant})
