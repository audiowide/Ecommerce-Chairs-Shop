from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import Profile, ProfileLocation
from ..forms import UpdateUserForm, UpdateProfileForm, ProfileLocationForm


@login_required(login_url='base:sign-in')
def profile_view(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   
   try:
      location = ProfileLocation.objects.get(user=user)
   except:
      location = ''
      print('Location not found')
   
   context = {
      'profile': profile,
      'location': location
   }
   return render(request, 'base/profile/profile.html', context)

@login_required(login_url='base:sign-in')
def profile_update_view(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   
   update_user = UpdateUserForm(instance=user)
   update_profile = UpdateProfileForm(instance=profile)
   
   if request.method == 'POST':
      update_user = UpdateUserForm(request.POST, instance=user)
      update_profile = UpdateProfileForm(request.POST, request.FILES, instance=profile)
      
      if update_user.is_valid() and update_profile.is_valid():
         update_user.save()
         update_profile.save()
         
         return redirect('base:profile')
   
   context = {
      'profile': profile,
      
      'update_user':update_user,
      'update_profile': update_profile,
   }
   return render(request, 'base/profile/update_profile.html', context)

@login_required(login_url='base:sign-in')
def profile_create_delivery_view(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   
   form = ProfileLocationForm()
   
   if request.method == 'POST':
      form = ProfileLocationForm(request.POST)
      if form.is_valid():
         delivery= form.save(commit=False)
         delivery.user = request.user
         delivery.save()
         return redirect('base:profile')
   
   context = {
      'profile': profile,
      
      'form': form ,
   }
   return render(request, 'base/profile/profile_delivery.html', context)

@login_required(login_url='base:sign-in')
def profile_update_delivery_view(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   delivery = ProfileLocation.objects.get(user=user)
   
   form = ProfileLocationForm(instance=delivery)
   
   if request.method == 'POST':
      form = ProfileLocationForm(request.POST, instance=delivery)
      if form.is_valid():
         form.save()
         return redirect('base:profile')
   
   context = {
      'profile': profile,
      
      'form': form ,
   }
   return render(request, 'base/profile/profile_delivery.html', context)

@login_required(login_url='base:sign-in')
def trash_view(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   
   if request.method == 'POST':
      products = [int(i) for i in request.POST.getlist('trash__products')]
      
      for product in products:
         profile.trash.remove(product)
         
      profile.save()
      return redirect('base:trash')
   
   context = {
      'profile': profile
   }
   return render(request, 'base/trash.html', context)


@login_required(login_url='base:sign-in')
def lower_view(request):
   user = request.user
   profile = Profile.objects.get(user=user)
   
   context = {
      'profile': profile
   }
   return render(request, 'base/profile/lower.html', context)