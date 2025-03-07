from django.db import models

# Create your models here.


# Create your models here.
class etudiant(models.Model):
    Metiers=[('APD','APD'),('DBE','DBE'),('ASSC','ASSC')]
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    metier = models.CharField( choices=Metiers,max_length=100)
    Ages = models.IntegerField()
    est_inscris =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.nom} {self.prenom}'

