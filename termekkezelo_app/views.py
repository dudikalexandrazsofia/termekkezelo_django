from django.shortcuts import get_object_or_404, redirect, render

from .forms import TermekForm
from .models import Termek

def kezdolap(request):
    return render(request, 'termekkezelo_app/kezdolap.html')

def termek_lista(request):
    termekek = Termek.objects.all()
    return render(request, 'termekkezelo_app/termek_list.html', {'termekek': termekek})


def termek_reszletek(request, pk):
    termek = get_object_or_404(Termek, pk=pk)
    return render(request, 'termekkezelo_app/termek_detail.html', {'object': termek})


def termek_uj(request):
    if request.method == 'POST':
        form = TermekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('termek_lista')
    else:
        form = TermekForm()
    return render(request, 'termekkezelo_app/termek_form.html', {'form': form, 'cim': 'Új termék'})


def termek_szerkesztes(request, pk):
    termek = get_object_or_404(Termek, pk=pk)
    if request.method == 'POST':
        form = TermekForm(request.POST, instance=termek)
        if form.is_valid():
            form.save()
            return redirect('termek_lista')
    else:
        form = TermekForm(instance=termek)
    return render(request, 'termekkezelo_app/termek_form.html', {'form': form, 'cim': 'Szerkesztés'})


def termek_torles(request, pk):
    termek = get_object_or_404(Termek, pk=pk)
    if request.method == 'POST':
        termek.delete()
        return redirect('termek_lista')
    return render(request, 'termekkezelo_app/termek_confirm_delete.html', {'object': termek})