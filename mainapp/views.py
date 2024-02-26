from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Category, SubCategory, Group, Banner
from product.models import Product
from .forms import SignUpForm
from django.contrib.auth import logout
import random


def index(request):
    categories = Category.objects.all() 
    subcategories = SubCategory.objects.all() 
    banners = Banner.objects.all() 
    products = Product.objects.filter(is_sold=False) 
    flashsale = Product.objects.filter(flash_sale = True).filter(is_sold=False)[:6]
    flashsale_is_sold = Product.objects.filter(flash_sale = True, is_sold = True)[:1]
    query = request.GET.get('query', ' ')
    
    def shuffle_groups():
        groups = list(Group.objects.all())
        random.shuffle(groups)
        return groups
    random_categories = shuffle_groups()[:14]
    context = {
        'categories': categories,
        'subcategories': subcategories,
        'banners': banners,
        'random_categories': random_categories,
        
        'products': products,
        'flashsale': flashsale,
        'flashsale_is_sold': flashsale_is_sold,
        
        'query': query,
    }
    return render(request, 'mainapp/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:login')
    else:
        form = SignUpForm()
    return render(request, 'mainapp/signup.html', {'form':form})

@login_required
def logoutUser(request):
    logout(request)
    return redirect('/')