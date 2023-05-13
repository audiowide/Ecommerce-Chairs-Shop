from django.contrib import admin
from .models import Product, ProductImage, ProductType, Profile, ProfileLocation, Comment

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Profile)
admin.site.register(ProfileLocation)
admin.site.register(Comment)
admin.site.register(ProductType)