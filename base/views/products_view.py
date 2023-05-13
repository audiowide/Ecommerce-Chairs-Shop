from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from ..models import Product, ProductType, ProductImage, ProductType, Profile, Comment
from ..forms import ProductForm, ProductTypeForm
from ..utils import slug_generator, checking_slug
from ..filters import ProductFilter
from ..services import getAllProductsService


def home_view(request):
   products = getAllProductsService()
   
   filter = ProductFilter(request.GET, queryset=products)
   products = filter.qs
   
   context = {
      'filter': filter,
      'products': products
   }
   return render(request, 'base/home.html', context)

def show_one_product_view(request, slug):
   product = Product.objects.get(slug=slug)
   comments = Comment.objects.filter(product=product)
   
   liked = False
   trash_goods = []
   
   if request.user.is_authenticated:
      user = request.user
      profile = Profile.objects.get(user=user)
      
      if profile.liked.filter(id = product.id): liked = True
      trash_products_full = []
      
      if (profile.trash.filter(product = product)):
         trash_products_full = profile.trash.filter(product = product)
         
         for trash_product in trash_products_full:
            trash_goods.append(trash_product.id)
   
   if request.method == 'POST':
      type = request.POST.get('type')
      
      if request.user.is_authenticated == False:
         return redirect('base:sign-in')
      
      if type == 'like':
         if profile.liked.filter(id=product.id):
            profile.liked.remove(product.id)
            return redirect('base:show-one-product', product.slug)
         else:
            profile.liked.add(product.id)
            return redirect('base:show-one-product', product.slug)
         
      if type == 'trash':
         all_products = product.product_types.all()         
         checked_goods = [int(i) for i in request.POST.getlist('trash__products')]

         for good in all_products:
            if good.id not in  checked_goods:
               profile.trash.remove(good.id)
         
         for good in checked_goods:
            profile.trash.add(good)
         
         return redirect('base:show-one-product', product.slug)
         
      if type == 'comment':
         message = request.POST.get('message')
         stars = request.POST.getlist('star')
         
         if not message:
            return messages.error(request, 'Please enter a message')
         
         if not stars:
            return messages.error(request, 'Please choose stars')
         
         comment = Comment.objects.create(
            user = request.user,
            product = product,
            body = message,
            starts = len(stars),
         )
         
         return redirect('base:show-one-product', product.slug)
            
   context = {
      'product': product,
      
      'trash_goods': trash_goods,
      'liked': liked,
      
      'comments': comments,
   }
   return render(request, 'base/product/show_one_product.html', context)

@login_required(login_url='base:sign-in')
def delete_product_review_view(request, slug, comment_id):
   product = Product.objects.get(slug=slug)
   comment = Comment.objects.get(id=comment_id)
   
   if comment:
      if comment.user == request.user:
         comment.delete()
         
         return redirect('base:show-one-product', product.slug)
      return messages.error(request, 'you do not have permission to delete')
   return messages.error(request, 'comment not found')
         
@login_required(login_url='base:sign-in')
def add_new_product(request):
   page_type = 'add_product_part_one'
   form = ProductForm()
   
   if request.method == 'POST':
      form = ProductForm(request.POST)
      if form.is_valid():
         slug = checking_slug(slug_generator(form.cleaned_data.get('title')))
         
         product = form.save(commit=False)
         
         product.slug = slug
         product.user = request.user
         
         product.save()
         return redirect('base:update-product', product.slug)
   
   context = {
      'page_type': page_type,
      'form': form
   }
   return render(request, 'base/product/add_new_product.html', context)

@csrf_exempt
@login_required(login_url='base:sign-in')
def update_product_view(request, slug):
   page_type = 'update_info'
   product = Product.objects.get(slug=slug)
   form = ProductForm(instance=product)
      
   if request.method == 'POST':
      form = ProductForm(request.POST, instance=product)
      images = request.FILES.getlist('images')
      print('______________{}______'.format(images))
      
      if form.is_valid():
         delete_images =  request.POST.getlist('photo__check')
         
         if len(images) > 0:  
            for image in images:
               product_image = ProductImage(
                  image=image,
               )
               product_image.save()
               product.images_gallery.add(product_image)
         
         if len(delete_images) > 0:
            for image in delete_images:
               product.images_gallery.filter(id=int(image)).delete()
         
         form.save()
         # return redirect('base:all-products')
   
   context = {
      'page_type': page_type,
      'form': form,
      'product': product
   }
   return render(request, 'base/product/product_panel.html', context)

@login_required(login_url='base:sign-in')
def update_product_types_view(request, slug):
   page_type = 'update_product_types'
   product = Product.objects.get(slug=slug)
   
   context = {
      'page_type': page_type,
      'product': product,
   }
   return render(request, 'base/product/product_panel.html', context)

@login_required(login_url='base:sign-in')
def add_new_product_type_view(request, slug):
   product = Product.objects.get(slug=slug)
   page_type = 'add_new_product_type'
   form = ProductTypeForm()
   
   if request.method == 'POST':
      form = ProductTypeForm(request.POST, request.FILES)
      if form.is_valid():
         product_type = form.save()
         
         product.product_types.add(product_type.id)
         return redirect('base:product-types', product.slug)
   
   context = {
      'page_type': page_type,
      'form': form,
      'product': product,
   }
   return render(request, 'base/product/product_panel.html', context)

@login_required(login_url='base:sign-in')
def update_product_type_view(request, slug, id):
   page_type = 'add_new_product_type'
   
   product = Product.objects.get(slug=slug)
   product_type = ProductType.objects.get(id=id)
   
   form = ProductTypeForm(instance=product_type)
   
   if request.method == 'POST':
      form = ProductTypeForm(request.POST, request.FILES, instance=product_type)
      if form.is_valid():
         form.save()
         
         return redirect('base:product-types', product.slug)
   
   context = {
      'page_type': page_type,
      'form': form,
      'product': product,
   }
   return render(request, 'base/product/product_panel.html', context)

@login_required(login_url='base:sign-in')
def delete_product_type_view(request, slug, id):
   page_type = 'delete_product_type'
   
   product = Product.objects.get(slug=slug)
   product_type = ProductType.objects.get(id=id)
      
   if request.method == 'POST':
      product_type.delete()
      return redirect('base:product-types', product.slug)
   
   context = {
      'page_type': page_type,
      'product': product,
   }
   return render(request, 'base/product/product_panel.html', context)

@login_required(login_url='base:sign-in')
def delete_product_view(request, slug):
   page_type = 'delete_product'
   
   product = Product.objects.get(slug=slug)
      
   if request.method == 'POST':
      product.delete()
      return redirect('base:all-products')
   
   context = {
      'page_type': page_type,
      'product': product,
   }
   return render(request, 'base/product/product_panel.html', context)