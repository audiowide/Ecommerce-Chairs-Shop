from django.urls import path
from . import views

urlpatterns = [
   path('endpoints', views.show_endpoints),
   path('products', views.show_all_products),
   path('products/<str:slug>/', views.show_one_product),
]
