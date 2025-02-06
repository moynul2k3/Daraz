from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('products/', views.products, name='products'),
    path('filters/', views.filters, name='filters'),
    path('products/<int:product_id>/', views.details, name='details'),
]
