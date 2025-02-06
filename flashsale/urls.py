from django.urls import path
from . import views
app_name = 'flashsale'
urlpatterns = [
    path('flashsale/', views.flashsale, name='flashsale')
]
