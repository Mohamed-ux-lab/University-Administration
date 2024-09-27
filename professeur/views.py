from django.shortcuts import render, redirect, get_object_or_404

from professeur.forms_professeur import FormsProf
from professeur.models import Professeur


def show(request):
    return render(request, 'professeur.html', {"profs": Professeur.objects.all()})


def add(request):
    if request.method == 'POST':
        form = FormsProf(request.POST)
        if form.is_valid():
            form.save()

            return redirect('professeur')

    else:
        form = FormsProf()

    return render(request, 'addProfesseur.html', {'form': form})


def delete(request, professeur_id):
    pass


def modify(request, professeur_id):
    professeur = get_object_or_404(Professeur, id=professeur_id)
    if request.method == 'POST':
        form = FormsProf(request.POST, instance=professeur)
        if form.is_valid():
            form.save()
            return redirect('professeur')  # Rediriger vers la liste ou autre page
    else:
        form = FormsProf(instance=professeur)
    return render(request, 'modifierprof.html', {'form': form})


def showone(request, professeur_id):
    professeur = get_object_or_404(Professeur, id=professeur_id)
    return render(request, 'oneProfesseur.html', {"profs": professeur})