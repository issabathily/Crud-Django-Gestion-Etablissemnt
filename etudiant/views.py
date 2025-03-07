from django.shortcuts import render,redirect,get_object_or_404
from .models import etudiant
from .forms import EtudiantForm
# Create your views here.
def index(request):
    etudiants = etudiant.objects.all().order_by('-created_at')
    return render(request,'etudiant/index.html',{'etudiants':etudiants})



def AddForms(request):
    form = EtudiantForm()
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = EtudiantForm()
    return render(request,'etudiant/addEtudiant.html',{'forms':form})

def DeleteEtudiant(request,id):
    etudiants = get_object_or_404(etudiant, id=id)
    etudiants.delete()
    return redirect('index')


def UpdateEtudiant(request,id):
    etudiante = get_object_or_404(etudiant, id=id)
    if request.method == "POST":
        forms= EtudiantForm(request.POST,instance=etudiante)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms =EtudiantForm(instance=etudiante)
    return render(request,'etudiant/modifier.html',{'forms':forms})