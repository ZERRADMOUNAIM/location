from django.db import models
from datetime import date

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    CNE = models.CharField(max_length=70, default='')  
    N_Tele = models.CharField(max_length=70)
    Email = models.CharField(max_length=70)
    Matricule = models.CharField(max_length=70)
    NomVoiture = models.CharField(max_length=100)
    Date_reservation = models.DateTimeField()
    Date_retour = models.DateTimeField()
    client_res = models.BooleanField(default=True)
    prix = models.FloatField(default=0.0)
    today = models.DateField(default=date.today)  # Ajout de l'attribut "today" avec la valeur par défaut de la date d'aujourd'hui

    def nb_jours_reservation(self):
        return (self.Date_retour - self.Date_reservation).days 

    def __str__(self):
        return f"{self.nom} {self.prenom}"


    


class Voiture(models.Model):
    id = models.AutoField(primary_key=True)  # Clé primaire auto-incrémentée
    genre = models.CharField(max_length=70)
    modele = models.CharField(max_length=70)
    matricule = models.CharField(max_length=70, unique=True)
    description = models.CharField(max_length=70)
    reserver = models.BooleanField(default=False)
    prix = models.FloatField(default=0.0)
    carImage = models.ImageField(null = True, blank = True, upload_to = "images/")


    def __str__(self):
        return f"{self.genre} {self.modele}"



class Voiture_reserver(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)  # Clé étrangère vers la table Voiture
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Clé étrangère vers la table Client

    def __str__(self):
        return f"{self.voiture.genre} {self.voiture.modele}"


from django.db import models
class Prix(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_ajout = models.DateTimeField(auto_now_add=True)



class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    date_add = models.DateTimeField()
    prix = models.FloatField(default=0.0)