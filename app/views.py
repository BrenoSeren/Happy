from django.shortcuts import redirect, render
from app.forms import InstitutionForm, UserForm
from app.models import Institution, User

def home(req):
    data = {
        'institutions': Institution.objects.all(),
        'users' : User.objects.all()
    }
    return render(req, 'index.html', data)

def cadastro(req):
    institutions = {}
    institutions['institutions'] = InstitutionForm()    
    return render(req, 'cadastro.html', institutions)

def cadastro2(req):
    users = {'users': UserForm()}
    return render(req, 'cadastro2.html', users)

def create(req):
    form = InstitutionForm(req.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def create2(req):
    form = UserForm(req.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')