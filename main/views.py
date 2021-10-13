from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import RqForm

def index(request):
    if request.method=='POST':
        form=RqForm(request.POST)
        if form.is_valid():
            form.save()
    form=RqForm()
    data={
        'form':form
    }
    return render(request, 'main/index.html',data)

