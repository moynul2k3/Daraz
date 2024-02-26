from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    # path('user/dashboard/', views.dashboard, name='dashboard'),
    path('user/manage_ac/', views.manage_ac, name='manage_ac'),
    path('user/my_profile/', views.my_profile, name='my_profile'),
    path('user/inbox/<int:pk>/', views.inbox, name='inbox'),
    path('user/address_book/', views.address_book, name='address_book'),
    path('user/payment_options/', views.payment_options, name='payment_options'),
    path('user/wallet/', views.wallet, name='wallet'),
    path('user/vouchers/', views.vouchers, name='vouchers'),
    path('user/my_orders/', views.my_orders, name='my_orders'),
    path('user/my_returns/', views.my_returns, name='my_returns'),
    path('user/my_cancellations/', views.my_cancellations, name='my_cancellations'),
    path('user/my_reviews/', views.my_reviews, name='my_reviews'),
    path('user/wishlist/', views.wishlist, name='wishlist'),
]
