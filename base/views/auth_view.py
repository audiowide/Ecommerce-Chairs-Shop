from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from ..models import Profile
from ..forms import CreateUserForm
from django.contrib import messages


def sign_in_view(request):
   page_type = 'sign_in'
   
   if request.method == 'POST':
      name = request.POST.get('name')
      password = request.POST.get('password')
      
      try: 
         user = User.objects.get(username=name)
         
         user = authenticate(username=name, password=password)
         
         if user is not None:
            login(request, user)
            return redirect('base:profile')
         else:
            messages.error(request, 'Password is incorrect')
      except:
         messages.error(request, 'User not found')
   
   context =  {
      'page_type': page_type
   }
   return render(request, 'base/auth.html',context)

def sign_up_view(request):
   page_type = 'sign_up'
   
   form = CreateUserForm()
   
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         user = form.save()
         
         Profile(
            user = user
         )
         login(request, user, login='django.contrib.auth.backends.ModelBackend')
         return redirect('base:profile')
   
   context =  {
      'page_type': page_type,
      'form': form,
   }
   return render(request, 'base/auth.html',context)

def sign_out_view(request):
   logout(request)
   return redirect('base:sign-in')