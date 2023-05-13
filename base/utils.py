from random import randrange
from .models import Product

# Transform in normal slug
def slug_generator(string):
   return '-'.join(string.lower().split(' '))

# Checking Slug
def checking_slug(slug):
   products = Product.objects.filter(slug=slug)
   
   if (products.count() > 0):
      slug += str(randrange(10000))
      return slug 
   else:
      return slug 