from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="accounts/login/")
def index(request):
    return render(request, 'classe.html', context={})
