from django.shortcuts import render
from app.forms import InstitutionForm, UserForm

def home(req):
    return render(req, 'index.html')

def cadastro(req):
    institutions = {}
    institutions['institutions'] = InstitutionForm()    
    return render(req, 'cadastro.html', institutions)

def cadastro2(req):
    users = {'users': UserForm()}
    return render(req, 'cadastro2.html', users)

