from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from professeur.models import Professeur
from etudiant.models import Etudiant


def index(request):
    return render(request, 'index.html', {})


@login_required(login_url='accounts:login')
def dashboard(request):
    nombre_etudiant = Etudiant.objects.count()
    nombre_prof = Professeur.objects.count()

    context = {
        'etudiant': nombre_etudiant,
        'professeur': nombre_prof
    }
    return render(request, 'dashboard.html', context)