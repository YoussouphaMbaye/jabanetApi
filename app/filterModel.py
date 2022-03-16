from itertools import product
import django_filters
from .models import Categorie, Produit

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Produit
        fields = ['price', 'denomination','id']
class CategorieFilter(django_filters.FilterSet):
    class Meta:
        model = Categorie
        fields = ['denomination','id']