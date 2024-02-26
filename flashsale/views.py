from django.shortcuts import render
from product.views import Product

# Create your views here.
def flashsale(request):
    flash_sale = Product.objects.filter(flash_sale=True)
    products = Product.objects.filter(is_sold=False).exclude(flash_sale=True)
    context = {
        'flash_sale': flash_sale,
        'products': products
    }
    return render(request, 'flashsale/flashsale.html', context)