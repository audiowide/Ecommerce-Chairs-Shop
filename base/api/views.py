from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound

from .serializers import ProductSerializer
from ..models import Product

@api_view(['GET'])
def show_endpoints(request):
   return Response({
      'products': '/api/products',
      'one product': '/api/products/<slug>'
   })

@api_view(['GET'])
def show_all_products(request):
   products = Product.objects.all()
   return Response(ProductSerializer(products, many=True).data)      

@api_view(['GET'])
def show_one_product(request, slug):
   try:
      product = Product.objects.get(slug=slug)
      return Response(ProductSerializer(product, many=False).data)  
   except:
      raise NotFound("Product does not exist")