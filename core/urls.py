from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('oferta/', views.oferta, name='oferta'),
    path('produkt/<slug:slug>/', views.product_detail, name='product_detail'),
    path('szukaj/', views.search_ajax, name='search_ajax'),
]
