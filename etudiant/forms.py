from django import forms
from .models import etudiant


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = etudiant
        fields = ['nom','prenom','metier','Ages','est_inscris']


