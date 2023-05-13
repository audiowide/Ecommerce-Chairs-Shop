import django_filters
from .models import Product
from django_filters import CharFilter

class ProductFilter(django_filters.FilterSet):
   title = CharFilter(field_name='title',  lookup_expr='icontains')
   
   class Meta:
      model = Product
      fields = ['title', ]