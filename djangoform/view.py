from django.shortcuts import render
from djangoform.forms import EmpForm


def home(request):
    stud = EmpForm()
    return render(request, 'index.html', {'form': stud})
