from django.shortcuts import render

from product.models import Product
from mainapp.models import Category

# Create your views here.

def wholesale(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/wholesale.html', context)

def low_price(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/low_price.html', context)

def free_delivery(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/free_delivery.html', context)

def fashion(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/fashion.html', context)

def beauty(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/beauty.html', context)

def mart(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/mart.html', context)

def home_makeover(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/home_makeover.html', context)

def best_price(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/best_price.html', context)

def daraz_visa(request):
    categories = Category.objects.all()
    top_deals = Product.objects.filter()[:7]
    products = Product.objects.all()
    context = {
        'categories': categories,
        'top_deals': top_deals,
        'products': products,
    }
    return render(request, 'offer/daraz_visa.html', context)
