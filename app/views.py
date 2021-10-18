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

def doacao(req):
    data = {
        'institutions': Institution.objects.values('id', 'email'),
        'users' : User.objects.values('id', 'email')
    }
    return render(req, 'doacao.html', data)

def edit(req, pk):
    data = {}
    data['db'] = Institution.objects.get(pk = pk)
    data['institutions'] = InstitutionForm(instance=data['db'])
    return render(req, 'cadastro.html', data)

def update(req, pk):
    data = {}
    data['db'] = Institution.objects.get(pk = pk)
    form = InstitutionForm(req.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def edit2(req, pk):
    data = {}
    data['db'] = User.objects.get(pk = pk)
    data['users'] = UserForm(instance=data['db'])
    return render(req, 'cadastro2.html', data)

def update2(req, pk):
    data = {}
    data['db'] = User.objects.get(pk = pk)
    form = UserForm(req.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(req, pk):
    db = Institution.objects.get(pk = pk)
    db.delete()
    return redirect('home')

def delete2(req, pk):
    db = User.objects.get(pk = pk)
    db.delete()
    return redirect('home')