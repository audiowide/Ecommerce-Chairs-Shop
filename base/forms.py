from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, PasswordInput
from .models import Profile, ProductType, Product, ProfileLocation, ProductType


class CreateUserForm(UserCreationForm):
   username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
   email = CharField(widget=TextInput(attrs={'placeholder': 'Email'}))
   password1 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder': ' Password'}))
   password2 = CharField(widget=TextInput(attrs={'type': 'password', 'placeholder': 'Repeat your password'}))
   
   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']   
      
class UpdateUserForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email']
      
class UpdateProfileForm(ModelForm):
   class Meta:
      model = Profile
      fields = ['photo']
      
class ProductForm(ModelForm):
   class Meta: 
      model = Product
      fields = ['title', 'about', 'deliveryTime']
      
class ProfileLocationForm(ModelForm):
   class Meta:
      model = ProfileLocation
      fields = ['country', 'region', 'city', 'place', 'zip']
      
class ProductTypeForm(ModelForm):
   class Meta:
      model = ProductType
      fields = '__all__'