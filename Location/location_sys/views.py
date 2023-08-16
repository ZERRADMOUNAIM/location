from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ClientRegistration, Registrationvoiture, ajoutertransaction
from .models import Client,  Voiture, Transaction
from django.core.exceptions import ValidationError
from datetime import date
# Create your views here.


@login_required
def HomePage(request):
    return render(request, 'location_sys/home.html', {})

    
def Voiture_dispo(request):
    return render(request, 'location_sys/VoitureDispo.html', {})

def bank(request):
    return render(request, 'location_sys/bank.html', {})
    
# ----------------------------
# ----------------------------
# add user
def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        sname = request.POST.get('sname')
        user_name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        new_user = User.objects.create_user(username=user_name, email=email, password=password)
        new_user.first_name = fname
        new_user.last_name = sname
        new_user.save()
        return redirect('login-page')
    return render(request, 'location_sys/register.html', {})

# login page
def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist or password is incorrect')

    return render(request, 'location_sys/login.html', {})

# logout page
def Logoutuser(request):
    logout(request)
    return redirect('login-page')

# add client
def add_client(request, id):
    voiture = Voiture.objects.get(pk=id)
    if request.method == 'POST':
        fm = ClientRegistration(request.POST)
        if fm.is_valid():
            client = fm.save(commit=False)
            client.Matricule = voiture.matricule
            client.NomVoiture =  voiture.genre +' '+ voiture.modele
            client.save()
            # Mettre à jour le statut de réservation de la voiture
            voiture.reserver = True
            voiture.save()
            return redirect('voiture_dispo-page')
    else:
        # Créer un formulaire vide
        fm = ClientRegistration()

    return render(request, 'location_sys/client.html', {'form': fm})

# list client
def Client_list(request):
    clients = Client.objects.all()
    return render(request, 'location_sys/clientlist.html', {'clients': clients})



# add voiture
def add_voiture(request):
    if request.method == 'POST':
        form = Registrationvoiture(request.POST, request.FILES)  # Pass request.FILES here
        if form.is_valid():
            # Get the image file from the form data
            image_file = request.FILES.get('image')

            # Check if the file is an image (optional)
            if image_file and not image_file.content_type.startswith('image'):
                raise ValidationError("File is not an image.")

            # Save the form data along with the image file
            new_voiture = form.save(commit=False)
            new_voiture.image = image_file
            new_voiture.save()

            return redirect('voiture_dispo-page')
    else:
        form = Registrationvoiture()
    return render(request, 'location_sys/Voiture.html', {'voiture': form})


# voiture list
def voiture_list(request):
    voitures = Voiture.objects.all()
    return render(request,'location_sys/VoitureDispo.html', {'voitures': voitures})



# delte voiture
def delete_voiture(request, id):
    if request.method == 'POST':
        pi = Voiture.objects.get(pk = id)
        pi.delete()
        # return HttpResponseRedirect('/')
        return redirect('voiture_dispo-page')


# delte client
def delete_client1(request, id):
    if request.method == 'POST':
        pi = Client.objects.get(pk = id)
        voiture = Voiture.objects.get(matricule=pi.Matricule)
        voiture.reserver = False
        voiture.save()
        pi.delete()
        # return HttpResponseRedirect('/')
        return redirect('clientres-page')
    
# delte client
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Voiture

def delete_client2(request, id):
    client = get_object_or_404(Client, pk=id)

    if  client.client_res:  # Vérifiez si le client n'est pas réservé (client_res=False)
        voiture = get_object_or_404(Voiture, matricule=client.Matricule)
        voiture.reserver = False
        voiture.save()
        
    client.delete()

    return redirect('client_list-page')

    

# update voiture.reserve and client.reserve false  
def update_reserverF(request, voiture_id):
    if request.method == 'POST':
        voiture = Voiture.objects.get(pk=voiture_id)
        voiture.reserver = False
        voiture.save()
        client = Client.objects.get(Matricule=voiture.matricule, client_res=True)
        client.client_res = False
        client.save()
        return redirect('voiture_reser-page')


# update voiture reserve true
from django.shortcuts import get_object_or_404, redirect
def update_reserverT(request, voiture_id):
    if request.method == 'POST':
        # Use get_object_or_404 to get the object or return a 404 page if not found
        voiture = get_object_or_404(Voiture, pk=voiture_id)
        voiture.reserver = True
        voiture.save()
        return redirect('voiture_dispo-page')

# voiture_list reserver
def voiture_listR(request):
    voitures = Voiture.objects.all()
    clients = Client.objects.filter(client_res=True)
    return render(request, 'location_sys/VoitureReserver.html', {'voituresR': voitures, 'clients': clients})


# modifier client  
# def update_client(request, id  ):
#     if request.method == 'POST':
#         pi = Client.objects.get(pk = id)
#         fm = ClientRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#            fm.save()   
#     else:
#             pi = Client.objects.get(pk=id)
#             fm = ClientRegistration(request.POST)
#     return render(request, 'location_sys/updateClient.html',{'form':fm})

def update_client(request,id):
    pi = get_object_or_404(Client, pk=id)

    if request.method == 'POST':
        fm = ClientRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('clientres-page')
    else:
        fm = ClientRegistration(instance=pi)

    return render(request, 'location_sys/updateClient.html',{'form':fm})


# modifier Voiture
from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404

def update_voiture(request, voiture_id):
    # Récupérer l'instance de la voiture
    instance = get_object_or_404(Voiture, pk=voiture_id)

    if request.method == 'POST':
        # Créer un formulaire en utilisant les données du POST et les fichiers téléchargés
        form = Registrationvoiture(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            # Vérifier si un nouveau fichier d'image a été téléchargé
            image_file = request.FILES.get('image')
            if image_file and not image_file.content_type.startswith('image'):
                raise ValidationError("File is not an image.")

            # Mettre à jour l'instance de la voiture avec les nouvelles données du formulaire
            instance = form.save(commit=False)
            instance.image = image_file
            instance.save()

            return redirect('voiture_dispo-page')
    else:
        form = Registrationvoiture(instance=instance)

    return render(request, 'location_sys/updateVoiture.html', {'voiture': form})




# client resrver
def filtrer_clients(request):
    clients = Client.objects.filter(client_res=True)
    return render(request, 'location_sys/Client _reserver.html', {'clients': clients})

# ajouter les donners de client en card voiture
# def ajouterinfo(request):
    
#     return render(request, 'location_sys/VoitureReserver.html', {'clients': clients})



# la somme des prix par jour
from datetime import datetime

def reservation(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        return render(request, 'location_sys/prix.html', {'date': date})
    return render(request, 'location_sys/reservation.html')

def prix_total(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        s = 0
        clients = Client.objects.filter(Date_reservation__date=date)
        for client in clients:
            s += client.prix * client.nb_jours_reservation()
        return render(request, 'location_sys/prix.html', {'prix': s})
    return render(request, 'location_sys/reservation.html')

 
#ajouter les prix au bank
from django.http import JsonResponse
from .models import Prix
def ajouter_prix(request):
    if request.method == 'POST':
        montant = request.POST.get('montant')
        if montant:
            prix = Prix.objects.create(montant=montant)
            return JsonResponse({'id': prix.id, 'montant': str(prix.montant), 'date_ajout': prix.date_ajout.strftime('%Y-%m-%d %H:%M:%S')})
    return JsonResponse({'error': 'Invalid request'})

# add transaction
def ajouter_transaction(request):
    if request.method == 'POST':
        form = ajoutertransaction(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank')
    else:
        form = ajoutertransaction()

    transactions = Transaction.objects.all()  # Récupérer toutes les transactions
    return render(request, 'location_sys/bank.html', {'form': form, 'transactions': transactions})


# modifier transaction
def update_transaction(request,id):
    pi = get_object_or_404(Transaction, pk=id)

    if request.method == 'POST':
        fm = ajoutertransaction(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('bank')
    else:
        fm = ajoutertransaction(instance=pi)

    return render(request, 'location_sys/updateTrans.html',{'form':fm})

# supprimer transaction 
def delete_transaction(request, id):
    if request.method == 'POST':
        pi = Transaction.objects.get(pk = id)
        pi.delete()
        # return HttpResponseRedirect('/')
        return redirect('bank')