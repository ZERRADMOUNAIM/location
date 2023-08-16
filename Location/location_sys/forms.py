from django import forms
from django.forms import widgets
from .models import Client , Voiture, Transaction
from django.forms import ClearableFileInput


# add client
class ClientRegistration(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['id', 'nom', 'prenom', 'CNE', 'N_Tele', 'Email', 'Date_reservation', 'Date_retour', 'prix'] # 'Matricule','NomVoiture',
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'CNE': forms.TextInput(attrs={'class': 'form-control'}),
            'N_Tele': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'Matricule': forms.TextInput(attrs={'class': 'form-control'}),
            # 'NomVoiture': forms.TextInput(attrs={'class': 'form-control'}),
            'Date_reservation': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'Date_retour': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),

        }

# add voiture
class Registrationvoiture(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['id','genre', 'modele', 'matricule', 'description', 'prix', 'carImage']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'voitur-control'}),
            'genre': forms.TextInput(attrs={'class': 'voitur-control'}),
            'modele': forms.TextInput(attrs={'class': 'voitur-control'}),
            'matricule': forms.TextInput(attrs={'class': 'voitur-control'}),
            'description': forms.TextInput(attrs={'class': 'voitur-control'}),
            'prix': forms.NumberInput(attrs={'class': 'voitur-control'}),
        }

class ajoutertransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['id','date_add','prix']
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'date_add': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'prix': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'prix': 'Montant',
            'date_add': 'La date',
        }