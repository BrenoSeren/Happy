from django.shortcuts import render
from app.forms import InstitutionForm

def home(req):
    return render(req, 'index.html')

def cadastro(req):
    institutions = {}
    institutions['institution'] = InstitutionForm()
    return render(req, 'cadastro.html', institutions)
