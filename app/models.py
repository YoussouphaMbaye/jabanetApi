from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Utilisateur(models.Model):
    profile=models.CharField(max_length=500,blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
   
    

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self) -> str:
        return self.profile
# Create your models here.
class Categorie(models.Model):
    denomination=models.CharField(max_length=500,blank=True,null=True)
    icone = models.FileField(upload_to='icones/', null=True,blank=True)
    

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self) -> str:
        return self.denomination
# Create your models here.
class Produit(models.Model):
    denomination=models.CharField(max_length=500,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    disponiblite=models.BooleanField(default=True)
    photos = models.FileField(upload_to='photos/')
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    prix=models.BigIntegerField(null=True,blank=True)
    promotion=models.IntegerField(null=True,blank=True,default=0)

   
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self) -> str:
        return self.denomination
# Create your models here.
class Produit_carateristique(models.Model):
    denomination=models.CharField(max_length=500,blank=True,null=True)
    valeur=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self) -> str:
        return self.denomination
# Create your models here.
class Lieux_livraison(models.Model):
    denomination=models.CharField(max_length=500,blank=True,null=True)
    region=models.CharField(max_length=500,blank=True,null=True)
    ville=models.CharField(max_length=500,blank=True,null=True)
    lat=models.CharField(max_length=500,blank=True,null=True)
    long=models.CharField(max_length=500,blank=True,null=True)
    type_lieux=models.CharField(max_length=500,blank=True,null=True)
    

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self) -> str:
        return self.denomination
# Create your models here.
class Commande(models.Model):
    lieux_livraison=models.ForeignKey(Lieux_livraison,on_delete=models.CASCADE)
    client=models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    total=models.BigIntegerField(default=0,blank=True,null=True)

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)
# Create your models here.
class ProduitItem(models.Model):
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    nb=models.IntegerField(default=1,null=True,blank=True)
    commande=models.ForeignKey(Commande,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)

 


