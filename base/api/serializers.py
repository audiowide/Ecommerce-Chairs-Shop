from rest_framework.serializers import ModelSerializer
from ..models import Product, ProductType, ProductImage

class ProductImageSerializer(ModelSerializer):
   class Meta:
      model = ProductImage
      fields = ('image', )

class ProductTypeSerializer(ModelSerializer):
   class Meta:
      model = ProductType
      fields = '__all__'

class ProductSerializer(ModelSerializer):
   product_types = ProductTypeSerializer(many=True)
   images_gallery = ProductImageSerializer(many=True)
   
   class Meta:
      model = Product
      fields = (
         'title', 
         'slug', 
         'about', 
         'product_types', 
         'images_gallery', 
         'deliveryTime', 
         'created', 
         'updated'
         )