from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import BoletinForm
from .logic.boletin_logic import get_boletines, get_boletin, create_boletin
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def boletin_list(request):
    role = getRole(request)
    if role == "Profesor" or "Miembro Comunidad":
        boletines = get_boletines()
        context = {
            'boletin_list': boletines
        }
        return render(request, 'Boletin/boletines.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def single_boletin(request, id=0):
    boletin = get_boletin(id)
    context = {
        'boletin': boletin
    }
    return render(request, 'Boletin/boletin.html', context)

@login_required
def boletin_create(request):
    role = getRole(request)
    if role == "Profesor":
        if request.method == 'POST':
            form = BoletinForm(request.POST)
            if form.is_valid():
                create_boletin(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created boletin')
                return HttpResponseRedirect(reverse('boletinCreate'))
            else:
                print(form.errors)
        else:
            form = BoletinForm()

        context = {
            'form': form,
        }
        return render(request, 'Boletin/boletinCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
