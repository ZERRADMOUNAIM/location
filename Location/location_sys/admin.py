from django.contrib import admin
from .models import Client, Voiture, Voiture_reserver, Transaction

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'prenom', 'N_Tele', 'Email', 'Matricule', 'Date_reservation', 'Date_retour', 'prix', 'today')

@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre', 'modele', 'matricule', 'description', 'reserver')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_add', 'prix')

@admin.register(Voiture_reserver)
class VoitureReserverAdmin(admin.ModelAdmin):
    list_display = ('id', 'voiture', 'client')
