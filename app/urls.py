from django.contrib import admin
from django.urls import path,include
from .views import CommandeItemViewset, CurrentUser, LieuxLivViewSet, ProduitItemViewset
from app.views import CategorieViewSet, ProduitViewSet, UserViewSet, UtilisateurViewSet
from rest_framework import routers, serializers, viewsets



router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('utilisateurs', UtilisateurViewSet)
router.register('categories',CategorieViewSet)
router.register('produits',ProduitViewSet)
router.register('produitItems',ProduitItemViewset)
router.register('lieux_livraisons',LieuxLivViewSet)
router.register('commandes',CommandeItemViewset)
router.register('currentUser',CurrentUser)


urlpatterns = [

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]