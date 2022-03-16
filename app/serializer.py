from .models import Commande, ProduitItem
from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Categorie, Lieux_livraison, Produit, Produit_carateristique, Utilisateur
class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'is_staff','last_name','first_name','email','is_active','is_staff']
class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Utilisateur
        fields = "__all__"
class CategorieSerialier(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Categorie
        fields = "__all__"
class ProduitSerialier(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Produit
        fields = "__all__"
class ProduitItemSerialier(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ProduitItem
        fields = "__all__"
class CommandeSerialier(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Commande
        fields = "__all__"
class ProduitCaractSerialier(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Produit_carateristique
        fields = "__all__"
class LieuxLivSerialier(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Lieux_livraison
        fields = "__all__"
