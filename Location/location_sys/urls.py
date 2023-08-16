from django.urls import path
from .views import HomePage, Register , Login, Logoutuser,add_client, voiture_list, Client_list, add_voiture, delete_voiture, voiture_listR, delete_client1, update_reserverF, update_reserverT, update_client, update_voiture, filtrer_clients, delete_client2, prix_total, reservation, ajouter_transaction, ajouter_prix, update_transaction, delete_transaction




urlpatterns = [
    path('home/', HomePage, name="home-page" ),
    path('register/', Register, name="register-page" ),
    path('clientres/', filtrer_clients, name="clientres-page" ),
    path('', Login, name="login-page" ),
    path('logout/', Logoutuser, name="logout-page" ),
    path('Clientregister/<int:id>', add_client, name="register_client-page" ),
    path('Clientlist/', Client_list, name="client_list-page" ),
    path('voiture_dispo/',  voiture_list, name="voiture_dispo-page" ),
    path('voiture_reser/',  voiture_listR, name="voiture_reser-page" ),
    path('voiture/',  add_voiture , name="voiture-page" ),
    path('delete_v/<int:id>',  delete_voiture , name="delete_v-page" ),
    path('delete_C/<int:id>',  delete_client1 , name="delete_cl1-page" ),
    path('delete_C2/<int:id>',  delete_client2 , name="delete_cl2-page" ),
    path('update_reserver/<int:voiture_id>/', update_reserverF, name='update_reserver'),
    path('update_reserverT/<int:voiture_id>/', update_reserverT, name='update_reserverT'),
    path('<int:id>/', update_client, name='update_client'),
    path('update_voiture/<int:voiture_id>/',update_voiture, name='update_voiture'),
    path('reservation/', reservation, name='reservation'),
    path('prix_total/', prix_total, name='prix_total'),
    path('transaction_list/', ajouter_transaction, name='bank'),  
    path('ajouter_prix/', ajouter_prix, name='ajouter_prix'),
    path('update_transaction/<int:id>/', update_transaction, name='update_transaction'),
    path('delete_tran/<int:id>',  delete_transaction , name="delete_tran" ),
 
]