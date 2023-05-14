from django.db import models
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   photo = models.ImageField(upload_to='profile_pics', validators=[ FileExtensionValidator(allowed_extensions=['jpg','png', 'svg', 'webp', 'gif'])],blank=True)
      
   liked = models.ManyToManyField('Product', related_name='liked', blank=True)
   trash = models.ManyToManyField('ProductType', related_name='trash', blank=True)
   
   def delete(self):
      super(Profile, self).delete() 
   
   def __str__(self):
      return self.user.username
   

class ProfileLocation(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
   
   country = models.CharField(max_length=30)
   region = models.CharField(max_length=50, blank=True)
   city = models.CharField(max_length=30)
   place = models.CharField(max_length=100)
   zip = models.CharField(max_length=10)
   
   def __str__(self):
      return self.country

class ProductImage(models.Model):
   image = models.FileField(upload_to='product_images/')   
   
   def __str__(self):
      return self.image.name

class ProductType(models.Model):
   title = models.CharField(max_length=100)
   image = models.ImageField(upload_to='product_types/{}/'.format(title),  blank=True)
   
   color = models.CharField(max_length=50, blank=True)
   material = models.CharField(max_length=50, blank=True)
   width = models.CharField(max_length=50, blank=True)
   height = models.CharField(max_length=50, blank=True)
   depth = models.CharField(max_length=50, blank=True)
   
   counts = models.IntegerField(default=0, blank=True)
   cost = models.IntegerField(default=0, blank=True)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.title

class Product(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   slug = models.SlugField(max_length=100, unique=True)
   about = models.TextField(blank=True, max_length=1000)
   
   product_types = models.ManyToManyField(ProductType, blank=True, default=[])
   images_gallery = models.ManyToManyField(ProductImage, blank=True, default=[])
   
   deliveryTime = models.CharField(max_length=30, blank=True)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def delete(self):
      # Full Delete 
      product_typess = self.product_types.all()
      images_gallerys = self.images_gallery.all()
      
      for product_type in product_typess:
         default_storage.delete(product_type.image.path)
         product_type.delete()
      
      for image in images_gallerys:
         default_storage.delete(image.image.path)
         image.delete()
      
      super(Product, self).delete() 
   
   def __str__(self):
      return self.slug
   
class Comment(models.Model):
   user  = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   body = models.TextField(max_length=1000)
   starts = models.IntegerField(default=1)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.user.username