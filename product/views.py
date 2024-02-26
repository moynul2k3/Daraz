from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from .models import Product, Brand, ColorFamily, SizeName, Size, Location, MainMaterial, WarrantyType, WarrantyPeriod, ListedYearSeason, MensTrend
from mainapp.models import Category, SubCategory, Group
from messaging.forms import ConversationForm
from messaging.models import Conversation
import random

from django.contrib.auth.models import User

# Create your views here.
def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'product/products.html', context)


def filters(request):
    categories = Category.objects.all()
    subcategory_id = request.GET.get('subcategory', 0)
    group_id = request.GET.get('group', 0)
    brand_id = request.GET.get('brand', 0)
    color_family_id = request.GET.get('color', 0)
    size_name_id = request.GET.get('size_name', 0)
    size_id = request.GET.get('size', 0)
    location_id = request.GET.get('location', 0)
    main_material_id = request.GET.get('material', 0)
    warrenty_type_id = request.GET.get('warrenty_type', 0)
    warranty_period_id = request.GET.get('warranty_period', 0)
    listed_year_season_id = request.GET.get('listed_year_season', 0)
    mens_trend_id = request.GET.get('mens_trend', 0)
    query = request.GET.get('query', ' ')
    name = request.GET.get('name', ' ')
    
    
    groups = Group.objects.none()
    header_groups = Group.objects.none()[:7]
    products = Product.objects.none()
    brands = Brand.objects.none()
    color_family = ColorFamily.objects.all() 
    size_name = SizeName.objects.none()
    size = Size.objects.none()
    location = Location.objects.all()
    main_material = MainMaterial.objects.none()
    warranty_type = WarrantyType.objects.all()
    warranty_period = WarrantyPeriod.objects.none()
    listed_year_season = ListedYearSeason.objects.none()
    mens_trend = MensTrend.objects.none()
    
    if name:
        header_groups = Group.objects.filter(Q(name__icontains=name))[:7]
        groups = Group.objects.filter(Q(name__icontains=name))
        products = Product.objects.filter(Q(name__icontains=name), is_sold=False)
        
        if brand_id:
            products = Product.objects.filter(brand_id=brand_id, is_sold=False)
        if color_family_id:
            products = Product.objects.filter(colorfamily_id=color_family_id, is_sold=False)
        if size_id:
            products = Product.objects.filter(size_id=size_id, is_sold=False)
        if main_material_id:
            products = Product.objects.filter(main_material_id=main_material_id, is_sold=False)
        if warranty_period_id:
            products = Product.objects.filter(warranty_period_id=warranty_period_id, is_sold=False)
        if listed_year_season_id:
            products = Product.objects.filter(listed_year_season_id=listed_year_season_id, is_sold=False)
        if mens_trend_id:
            products = Product.objects.filter(mens_trend_id=mens_trend_id, is_sold=False)
            
        brands = Brand.objects.filter(group_id=group_id)
        size_name = SizeName.objects.filter(group_id=group_id)
        size = Size.objects.filter(group_id=group_id)
        main_material = MainMaterial.objects.filter(group_id=group_id)
        warranty_type = WarrantyType.objects.filter(group_id=group_id)
        warranty_period = WarrantyPeriod.objects.filter(group_id=group_id)
        listed_year_season = ListedYearSeason.objects.filter(group_id=group_id)
        mens_trend = MensTrend.objects.filter(group_id=group_id)
        
    if query:
        header_groups = Group.objects.filter(Q(name__icontains=query))[:7]
        groups = Group.objects.filter(Q(name__icontains=query))
        products = Product.objects.filter(Q(name__icontains=query), is_sold=False)
        
    if subcategory_id:
        header_groups = Group.objects.filter(Q(name__icontains=name))[:7]
        groups = Group.objects.filter(subcategory_id=subcategory_id)
        products = Product.objects.filter(subcategory_id=subcategory_id, is_sold=False)
        
        if brand_id:
            products = Product.objects.filter(brand_id=brand_id, is_sold=False)
        if color_family_id:
            products = Product.objects.filter(colorfamily_id=color_family_id, is_sold=False)
        if size_id:
            products = Product.objects.filter(size_id=size_id, is_sold=False)
        if location_id:
            products = Product.objects.filter(location_id=location_id, is_sold=False)
        if main_material_id:
            products = Product.objects.filter(main_material_id=main_material_id, is_sold=False)
        if warranty_period_id:
            products = Product.objects.filter(warranty_period_id=warranty_period_id, is_sold=False)
        if listed_year_season_id:
            products = Product.objects.filter(listed_year_season_id=listed_year_season_id, is_sold=False)
        if mens_trend_id:
            products = Product.objects.filter(mens_trend_id=mens_trend_id, is_sold=False)
        brands = Brand.objects.filter(subcategory_id=subcategory_id)
        size_name = SizeName.objects.filter(subcategory_id=subcategory_id)
        size = Size.objects.filter(subcategory_id=subcategory_id)
        main_material = MainMaterial.objects.filter(subcategory_id=subcategory_id)
        warranty_type = WarrantyType.objects.filter(subcategory_id=subcategory_id)
        warranty_period = WarrantyPeriod.objects.filter(subcategory_id=subcategory_id)
        listed_year_season = ListedYearSeason.objects.filter(subcategory_id=subcategory_id)
        mens_trend = MensTrend.objects.filter(subcategory_id=subcategory_id)
        
    if group_id:
        header_groups = Group.objects.filter(Q(name__icontains=name))[:7]
        groups = Group.objects.filter(id=group_id)
        products = Product.objects.filter(group_id=group_id, is_sold=False)
        
        if brand_id:
            products = Product.objects.filter(brand_id=brand_id, is_sold=False)
        if color_family_id:
            products = Product.objects.filter(colorfamily_id=color_family_id, is_sold=False)
        if size_id:
            products = Product.objects.filter(size_id=size_id, is_sold=False)
        if location_id:
            products = Product.objects.filter(location_id=location_id, is_sold=False)
        if main_material_id:
            products = Product.objects.filter(main_material_id=main_material_id, is_sold=False)
        if warranty_period_id:
            products = Product.objects.filter(warranty_period_id=warranty_period_id, is_sold=False)
        if listed_year_season_id:
            products = Product.objects.filter(listed_year_season_id=listed_year_season_id, is_sold=False)
        if mens_trend_id:
            products = Product.objects.filter(mens_trend_id=mens_trend_id, is_sold=False)
        brands = Brand.objects.filter(group_id=group_id)
        size_name = SizeName.objects.filter(group_id=group_id)
        size = Size.objects.filter(group_id=group_id)
        main_material = MainMaterial.objects.filter(group_id=group_id)
        warranty_type = WarrantyType.objects.filter(group_id=group_id)
        warranty_period = WarrantyPeriod.objects.filter(group_id=group_id)
        listed_year_season = ListedYearSeason.objects.filter(group_id=group_id)
        mens_trend = MensTrend.objects.filter(group_id=group_id)

    if location_id:
        products = Product.objects.filter(location_id=location_id)
    context = {
        'query': query,
        'name': name,
        'categories': categories,
        'header_groups': header_groups,
        'products': products,
        'groups': groups,
        'brand_id': brand_id,
        'color_family_id': color_family_id,
        'size_name_id': size_name_id,
        'size_id': size_id,
        'location_id': location_id,
        'main_material_id': main_material_id,
        'warrenty_type_id': warrenty_type_id,
        'warranty_period_id': warranty_period_id,
        'listed_year_season_id': listed_year_season_id,
        'mens_trend_id': mens_trend_id,
        'brands': brands,
        'color_family': color_family,
        'size_name': size_name,
        'size': size,
        'location': location,
        'main_material': main_material,
        'warranty_type': warranty_type,
        'warranty_period': warranty_period,
        'listed_year_season': listed_year_season,
        'mens_trend': mens_trend,
        
    }
        
    return render(request, 'product/filters.html', context)



def details(request, product_id):
    categories = Category.objects.all()
    product_datails = get_object_or_404(Product, pk=product_id)
    products = Product.objects.filter(group=product_datails.group, is_sold=False).exclude(id=product_id)
    
    sender_id = request.user.id
    receiver_id = product_datails.created_by.id
    this_conversation = Conversation.objects.filter(product_id=product_id, sender_id=sender_id, reciever_id=receiver_id)
    if request.method == 'POST':
        if this_conversation:
            this_conversation = Conversation.objects.get(product_id=product_id, sender_id=sender_id, reciever_id=receiver_id)
            conversation_id = this_conversation.id
            return redirect('dashboard:inbox', conversation_id)
        else:
            form_data = request.POST.copy() 
            form_data['sender'] = sender_id  
            form_data['reciever'] = receiver_id  
            form_data['product'] = product_id  
            form = ConversationForm(form_data)
            if form.is_valid():
                form.save()
                id = form.save().id
                return redirect('dashboard:inbox', id)
    
    context = {
        'categories': categories,
        'product_datails': product_datails,
        'products': products,
    }
    return render(request, 'product/details.html', context)


