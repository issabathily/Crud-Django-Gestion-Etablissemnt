from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.AddForms, name='form'),
    path('delete/<int:id>/', views.DeleteEtudiant, name='delete'),
    path('modifier/<int:id>/', views.UpdateEtudiant, name='modifier'),
]
