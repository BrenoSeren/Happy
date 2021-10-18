from django.shortcuts import redirect, render
from app.forms import DoacaoCompForm, DoacaoForm, InstitutionForm, UserForm
from app.models import Doacao, Institution, User

def home(req):
    data = {
        'institutions': Institution.objects.all(),
        'users' : User.objects.all(),
        'doacoes' : Doacao.objects.all()
    }
    return render(req, 'index.html', data)

def cadastro(req):
    institutions = {}
    institutions['institutions'] = InstitutionForm()    
    return render(req, 'cadastro.html', institutions)

def cadastro2(req):
    users = {'users': UserForm()}
    return render(req, 'cadastro2.html', users)

def doacao(req):
    data = {
        'institutions': Institution.objects.values('id', 'email'),
        'users' : User.objects.values('id', 'email'),
        'doacao' : DoacaoForm()
    }
    return render(req, 'doacao.html', data)

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

def createDoacao(req):
    form = DoacaoCompForm(req.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

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

def editDoacao(req, pk):
    data = {}
    data['db'] = Doacao.objects.get(pk = pk)
    data['doacao'] = DoacaoForm(instance=data['db'])
    data['institutions'] = Institution.objects.values('id', 'email')
    data['users'] = User.objects.values('id', 'email')
    return render(req, 'doacao.html', data)

def updateDoacao(req, pk):
    data = {}
    data['db'] = Doacao.objects.get(pk = pk)
    form = DoacaoCompForm(req.POST or None, instance=data['db'])
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

def deleteDoacao(req, pk):
    db = Doacao.objects.get(pk = pk)
    db.delete()
    return redirect('home')