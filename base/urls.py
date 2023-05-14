from django.urls import path

from .views.products_view import home_view,delete_product_review_view, add_new_product, update_product_view, update_product_types_view, update_product_type_view, add_new_product_type_view, delete_product_type_view, delete_product_view, show_one_product_view
from .views.auth_view import sign_in_view, sign_up_view, sign_out_view
from .views.user_view import profile_view, profile_update_view, profile_update_delivery_view, profile_create_delivery_view, trash_view, lower_view, all_comments_view, delete_account_view

app_name  = 'base'

urlpatterns = [
   path('', home_view, name='home'),
   
   path('sign-in', sign_in_view, name='sign-in'),
   path('sign-up', sign_up_view, name='sign-up'),
   path('sign-out', sign_out_view, name='sign-out'),
   
   path('profile', profile_view, name='profile'),
   path('profile-update', profile_update_view, name='profile-update'),
   path('profile-create-delivery', profile_create_delivery_view , name='profile-create-delivery-view'),
   path('profile-update-delivery', profile_update_delivery_view , name='profile-update-delivery-view'),
   path('profile-comments',  all_comments_view, name='comments'),
   path('profile-delete',  delete_account_view, name='delete-account'),
   
   path('lovers', lower_view , name='lowers'),
   path('trash', trash_view , name='trash'),
   
   path('add-new-product', add_new_product, name='add-new-product'),

   path('product/<str:slug>', show_one_product_view, name='show-one-product'),
   path('product/<str:slug>/reviews/<int:comment_id>/delete', delete_product_review_view, name='delete-product-review'),

   path('product/<str:slug>/update', update_product_view, name='update-product'),
   path('product/<str:slug>/delete', delete_product_view, name='delete-product'),
   path('products/<str:slug>/product-types', update_product_types_view, name='product-types'),
   
   path('products/<str:slug>/product-types/create', add_new_product_type_view, name='add-new-product-type'),
   path('products/<str:slug>/product-types/<int:id>/edit',    update_product_type_view, name='update-product-type'),
   path('products/<str:slug>/product-types/<int:id>/delete',delete_product_type_view, name='delete-product-type')
]
