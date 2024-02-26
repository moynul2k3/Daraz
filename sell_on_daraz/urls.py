from django.urls import path
from . import views

app_name = 'sell_on_daraz'
urlpatterns = [
    path('for_sale/', views.for_sale, name='for_sale'),
    path('inbox/<int:pk>/', views.inbox, name='inbox'),
    path('new_banner/', views.new_banner, name='new_banner'),
    path('new_category/', views.new_category, name='new_category'),
    path('new_sub_category/', views.new_sub_category, name='new_sub_category'),
    path('new_groups/', views.new_groups, name='new_groups'),
    path('new_product/', views.new_product, name='new_product'),
    
    path('<int:pk>/<int:id>/new_brand/', views.new_brand, name='new_brand'),
    path('<int:pk>/<int:id>/new_material/', views.new_material, name='new_material'),
    path('<int:pk>/<int:id>/new_warranty_period/', views.new_warranty_period, name='new_warranty_period'),
    path('<int:pk>/<int:id>/new_listed_year_season/', views.new_listed_year_season, name='new_listed_year_season'),
    path('<int:pk>/<int:id>/new_mens_trend/', views.new_mens_trend, name='new_mens_trend'),
    
    path('load_options/', views.load_options, name='load_options'),
    
    path('banner/<int:pk>/edit/', views.edit_banner, name='edit_banner'),
    path('category/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('sub_category/<int:pk>/edit/', views.edit_sub_category, name='edit_sub_category'),
    path('group/<int:pk>/edit/', views.edit_group, name='edit_group'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:pk>/manage/', views.manage_product, name='manage_product'),
    
    path('banner/<int:pk>/delete/', views.delete_banner, name='delete_banner'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('subcategory/<int:pk>/delete/', views.delete_sub_category, name='delete_sub_category'),
    path('group/<int:pk>/delete/', views.delete_group, name='delete_group'),
    
    path('brand/<int:pk>/<int:id1>/<int:id2>/delete/', views.delete_brand, name='delete_brand'),
    path('material/<int:pk>/<int:id1>/<int:id2>/delete/', views.delete_material, name='delete_material'),
    path('warranty_period/<int:pk>/<int:id1>/<int:id2>/delete/', views.delete_warranty_period, name='delete_warranty_period'),
    path('listed_year_season/<int:pk>/<int:id1>/<int:id2>/delete/', views.delete_listed_year_season, name='delete_listed_year_season'),
    path('mens_trend/<int:pk>/<int:id1>/<int:id2>/delete/', views.delete_mens_trend, name='delete_mens_trend'),
    
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
]
