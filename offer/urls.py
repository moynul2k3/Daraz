from django.urls import path
from . import views


app_name = 'offer'
urlpatterns = [
    path('offers/wholesale_price/', views.wholesale, name='wholesale'),
    path('offers/low_price/', views.low_price, name='low_price'),
    path('offers/free_delivery/', views.free_delivery, name='free_delivery'),
    path('offers/fashion/', views.fashion, name='fashion'),
    path('offers/beauty/', views.beauty, name='beauty'),
    path('offers/mart/', views.mart, name='mart'),
    path('offers/home_makeover/', views.home_makeover, name='home_makeover'),
    path('offers/best_price/', views.best_price, name='best_price'),
    path('offers/daraz_visa/', views.daraz_visa, name='daraz_visa'),
]
