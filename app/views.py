from urllib import request
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Commande, ProduitItem
from .serializer import CommandeSerialier, ProduitItemSerialier
from .models import Categorie, Lieux_livraison, Produit, Utilisateur
from .serializer import CategorieSerialier, LieuxLivSerialier, ProduitSerialier, UserSerializer, UtilisateurSerializer
from rest_framework import  viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class CurrentUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):                                            # added string
        return super().get_queryset().filter(id=self.request.user.id)
   
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user']
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerialier
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'denomination']
class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerialier
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['denomination','categorie']
class ProduitItemViewset(viewsets.ModelViewSet):
    queryset = ProduitItem.objects.all()
    serializer_class = ProduitItemSerialier
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['produit','commande']
class CommandeItemViewset(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerialier
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lieux_livraison']
class LieuxLivViewset(viewsets.ModelViewSet):
    queryset = Lieux_livraison.objects.all()
    serializer_class = Lieux_livraison
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['denomination']


class LieuxLivViewSet(viewsets.ModelViewSet):
    queryset = Lieux_livraison.objects.all()
    serializer_class = LieuxLivSerialier


   

    