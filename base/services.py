from .models import Product

def getAllProductsService():
   return Product.objects.all()