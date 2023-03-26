from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import usercf


def usercform(request):
    if request.method == 'POST':
        frm = usercf(request.POST)
        if frm.is_valid():
            frm.save()
    else :
        frm = UserCreationForm()
    return render(request, 'resources/usercform.html', {'form': frm})