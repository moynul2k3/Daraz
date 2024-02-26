from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import Category, SubCategory, Group, Banner
from product.models import Product, Brand, MainMaterial, WarrantyPeriod, ListedYearSeason, MensTrend

from product.forms import NewColorFamily, NewProduct, EditProduct, ManageProduct
from .forms import NewBanner, NewCategory, NewSubCategory, NewGroup, NewBrand, NewMaterial, NewWarrantyPeriod, NewListedYearSeason, NewMensTrend, EditBanner, EditCategory, EditSubCategory, EditGroup

from messaging.models import Conversation, ConversationMessage
from messaging.forms import ConversationMessageForm
# Create your views here.
# .............................Daraz_On_Sale.............................
@login_required
def for_sale(request):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    sold_products = Product.objects.filter(created_by=request.user).filter(is_sold=True)
    conversations = Conversation.objects.filter(reciever=request.user)
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'sold_products': sold_products,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/for_sale.html', context)

@login_required
def inbox(request, pk):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    
    sender=request.user
    conversations = Conversation.objects.filter(reciever=request.user)
    if pk>0:
        this_conversation = Conversation.objects.get(id=pk)
    else:
        this_conversation = Conversation.objects.none()
    messages = ConversationMessage.objects.filter(conversation_id=pk)
    form = ConversationMessageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False) 
            form.instance.conversation=get_object_or_404(Conversation, pk=pk)
            form.instance.created_by=request.user
            form.save()
            return redirect('.')
    else:
        form = ConversationMessageForm()
        
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'form': form,
        'messages': messages,
        'sender': sender,
        'conversations': conversations,
        'this_conversation': this_conversation,
    }
    return render(request, 'add_new_pages/inbox.html', context)


# ................................................NEW................................................................
@login_required
def new_banner(request):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    banner_form = NewBanner(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if banner_form.is_valid():
            banner = banner_form.save(commit=False)
            banner.created_by = request.user
            banner.save()
            return redirect('sell_on_daraz:new_banner')
    else:
        banner_form = NewBanner()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'banner_form': banner_form,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/banners.html', context)

@login_required
def new_category(request):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    category_form = NewCategory(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if category_form.is_valid():
            category = category_form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('sell_on_daraz:new_category')
    else:
        category_form = NewCategory()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'category_form': category_form,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/categories.html', context)

@login_required
def new_sub_category(request):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    sub_category_form = NewSubCategory(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if sub_category_form.is_valid():
            sub_category = sub_category_form.save(commit=False)
            sub_category.created_by = request.user
            sub_category.save()
            return redirect('sell_on_daraz:new_sub_category')
    else:
        sub_category_form = NewSubCategory()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'sub_category_form': sub_category_form,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/sub_categories.html', context)


@login_required
def new_groups(request):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    new_group_form = NewGroup(request.POST, request.FILES)
    if request.method == 'POST':
        if 'new_group_form' in request.POST:
            if new_group_form.is_valid():
                group = new_group_form.save(commit=False)
                group.created_by = request.user
                group.save()
                return redirect('sell_on_daraz:new_groups')
        else:
            new_group_form = NewGroup()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'new_group_form': new_group_form,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/groups.html', context)

@login_required
def load_options(request):
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    sub_categories = SubCategory.objects.filter(category_id=category_id)
    groups = Group.objects.filter(subcategory_id=subcategory_id)
    context = {
        'sub_categories': sub_categories,
        'groups': groups,
    }
    return render(request, 'sell_on_daraz/options.html', context)

@login_required
def new_product(request):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    new_product_form = NewProduct(request.POST or None, request.FILES or None)
    new_colorfamily_form = NewColorFamily(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if 'new_product_form' in request.POST:
            if new_product_form.is_valid():
                product = new_product_form.save(commit=False)
                product.created_by = request.user
                product.save()
                return redirect('sell_on_daraz:manage_product', product.id)
        elif 'new_colorfamily_form' in request.POST:
            if new_colorfamily_form.is_valid():
                new_colorfamily_form.save()
                return redirect('sell_on_daraz:new_product')
        else:
            new_product_form = NewProduct()
            new_colorfamily_form = NewColorFamily()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'new_product_form': new_product_form,
        'new_colorfamily_form': new_colorfamily_form,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/new_product.html', context)

@login_required
def new_brand(request, pk, id):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    manage_products = Product.objects.get(id=id)
    brands = Brand.objects.filter(group_id=pk)
    form_group = get_object_or_404(Group, pk=pk)
    new_form = NewBrand(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if 'new_form' in request.POST:
            if new_form.is_valid():
                new_form.save(commit=False)
                new_form.instance.category = Category.objects.get(id=form_group.category_id)
                new_form.instance.subcategory = SubCategory.objects.get(id=form_group.subcategory_id)
                new_form.instance.group = Group.objects.get(id=form_group.id)
                new_form.created_by = request.user
                new_form.save()
                return redirect('sell_on_daraz:new_brand', pk, id)
        else:
            new_form = NewBrand()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        
        'manage_products': manage_products,
        'brands': brands,
        'new_form': new_form,
        'form_group': form_group,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/new_brand.html', context)

@login_required
def new_material(request, pk, id):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    manage_products = Product.objects.get(id=id)
    materials = MainMaterial.objects.filter(group_id=pk)
    form_group = get_object_or_404(Group, pk=pk)
    new_form = NewMaterial(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if 'new_form' in request.POST:
            if new_form.is_valid():
                new_form.save(commit=False)
                new_form.instance.category = Category.objects.get(id=form_group.category_id)
                new_form.instance.subcategory = SubCategory.objects.get(id=form_group.subcategory_id)
                new_form.instance.group = Group.objects.get(id=form_group.id)
                new_form.created_by = request.user
                new_form.save()
                return redirect('sell_on_daraz:new_material', pk, id)
        else:
            new_form = NewMaterial()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        
        'manage_products': manage_products,
        'materials': materials,
        'new_form': new_form,
        'form_group': form_group,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/new_material.html', context)

@login_required
def new_warranty_period(request, pk, id):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    manage_products = Product.objects.get(id=id)
    warranty_period = WarrantyPeriod.objects.filter(group_id=pk)
    form_group = get_object_or_404(Group, pk=pk)
    new_form = NewWarrantyPeriod(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if 'new_form' in request.POST:
            if new_form.is_valid():
                new_form.save(commit=False)
                new_form.instance.category = Category.objects.get(id=form_group.category_id)
                new_form.instance.subcategory = SubCategory.objects.get(id=form_group.subcategory_id)
                new_form.instance.group = Group.objects.get(id=form_group.id)
                new_form.created_by = request.user
                new_form.save()
                return redirect('sell_on_daraz:new_warranty_period', pk, id)
        else:
            new_form = NewWarrantyPeriod()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        
        'manage_products': manage_products,
        'warranty_period': warranty_period,
        'new_form': new_form,
        'form_group': form_group,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/new_warranty_period.html', context)

@login_required
def new_listed_year_season(request, pk, id):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    manage_products = Product.objects.get(id=id)
    listed_year_season = ListedYearSeason.objects.filter(group_id=pk)
    form_group = get_object_or_404(Group, pk=pk)
    new_form = NewListedYearSeason(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if 'new_form' in request.POST:
            if new_form.is_valid():
                new_form.save(commit=False)
                new_form.instance.category = Category.objects.get(id=form_group.category_id)
                new_form.instance.subcategory = SubCategory.objects.get(id=form_group.subcategory_id)
                new_form.instance.group = Group.objects.get(id=form_group.id)
                new_form.created_by = request.user
                new_form.save()
                return redirect('sell_on_daraz:new_listed_year_season', pk, id)
        else:
            new_form = NewListedYearSeason()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        
        'manage_products': manage_products,
        'listed_year_season': listed_year_season,
        'new_form': new_form,
        'form_group': form_group,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/new_listed_year_season.html', context)

@login_required
def new_mens_trend(request, pk, id):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    manage_products = Product.objects.get(id=id)
    mens_trend = MensTrend.objects.filter(group_id=pk)
    form_group = get_object_or_404(Group, pk=pk)
    new_form = MensTrend(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if 'new_form' in request.POST:
            if new_form.is_valid():
                new_form.save(commit=False)
                new_form.instance.category = Category.objects.get(id=form_group.category_id)
                new_form.instance.subcategory = SubCategory.objects.get(id=form_group.subcategory_id)
                new_form.instance.group = Group.objects.get(id=form_group.id)
                new_form.created_by = request.user
                new_form.save()
                return redirect('sell_on_daraz:new_mens_trend', pk, id)
        else:
            new_form = MensTrend()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        
        'manage_products': manage_products,
        'mens_trend': mens_trend,
        'new_form': new_form,
        'form_group': form_group,
        'conversations': conversations,
    }
    return render(request, 'add_new_pages/new_mens_trend.html', context)




# ................................Edit.....................................................
@login_required
def edit_banner(request, pk):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    edit_banners = get_object_or_404(Banner, pk=pk)
    banner_form = EditBanner(request.POST or None, request.FILES or None, instance=edit_banners)
    if request.method == 'POST':
        if 'banner_form' in request.POST:
            if banner_form.is_valid():
                banner_form.save()
                return redirect('sell_on_daraz:new_banner')
        else:
            banner_form = EditBanner()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'edit_banner_form': banner_form,
        'conversations': conversations,
    }
    return render(request, 'edit_pages/edit_banner.html', context)

@login_required
def edit_category(request, pk):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    edit_category = get_object_or_404(Category, pk=pk, created_by=request.user)
    category_form = EditCategory(request.POST or None, request.FILES or None, instance=edit_category)
    if request.method == 'POST':
        if 'category_form' in request.POST:
            if category_form.is_valid():
                category_form.save()
                return redirect('sell_on_daraz:new_category')
        else:
            category_form = EditCategory()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'edit_category_form': category_form,
        'conversations': conversations,
    }
    return render(request, 'edit_pages/edit_category.html', context)

@login_required
def edit_sub_category(request, pk):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    edit_sub_category = get_object_or_404(SubCategory, pk=pk, created_by=request.user)
    sub_category_form = EditSubCategory(request.POST or None, request.FILES or None, instance=edit_sub_category)
    if request.method == 'POST':
        if 'sub_category_form' in request.POST:
            if sub_category_form.is_valid():
                sub_category_form.save()
                return redirect('sell_on_daraz:new_sub_category')
        else:
            sub_category_form = EditSubCategory()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'edit_sub_category_form': sub_category_form,
        'conversations': conversations,
    }
    return render(request, 'edit_pages/edit_sub_category.html', context)

@login_required
def edit_group(request, pk):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    edit_group_form = get_object_or_404(Group, pk=pk, created_by=request.user)
    edit_group_form = EditGroup(request.POST or None, request.FILES or None, instance=edit_group_form)
    if request.method == 'POST':
        if 'group_form' in request.POST:
            if edit_group_form.is_valid():
                edit_group_form.save()
                return redirect('sell_on_daraz:new_groups')
        else:
            edit_group_form = EditGroup()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'edit_group_form': edit_group_form,
        'conversations': conversations,
    }
    return render(request, 'edit_pages/edit_group.html', context)

@login_required
def edit_product(request, pk):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    edit_products = get_object_or_404(Product, pk=pk, created_by=request.user)
    new_colorfamily_form = NewColorFamily(request.POST or None, request.FILES or None)
    edit_product_form = EditProduct(request.POST or None, request.FILES or None, instance=edit_products)
    if request.method == 'POST':
        if 'add_colorfamily_form' in request.POST:
            if new_colorfamily_form.is_valid():
                new_colorfamily_form.save()
                return redirect('sell_on_daraz:edit_product', pk)
        elif 'edit_product_form' in request.POST:
            if edit_product_form.is_valid():
                edit_product_form.save()
                return redirect('sell_on_daraz:manage_product', pk)
        else:
            edit_product_form = EditProduct()
            new_colorfamily_form = NewColorFamily()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'edit_products': edit_products,
        'edit_product_form': edit_product_form,
        'new_colorfamily_form': new_colorfamily_form,
        'conversations': conversations,
    }
    return render(request, 'edit_pages/edit_product.html', context)

@login_required
def manage_product(request, pk):
    banners = Banner.objects.all() 
    categories = Category.objects.all() 
    sub_categories = SubCategory.objects.all() 
    groups = Group.objects.all() 
    products = Product.objects.filter(created_by=request.user).filter(is_sold=False) 
    conversations = Conversation.objects.filter(reciever=request.user)
    manage_products = get_object_or_404(Product, pk=pk, created_by=request.user)
    group_id=int(manage_products.group_id)
    manage_product_form = ManageProduct(group_id=group_id, instance=manage_products)
    
    if request.method == 'POST':
        manage_product_form = ManageProduct(group_id=group_id, instance=manage_products, data=request.POST, files=request.FILES)
        if 'manage_product_form' in request.POST:
            if manage_product_form.is_valid():
                manage_product_form.save()
                return redirect('sell_on_daraz:for_sale')
        else:
            manage_product_form = ManageProduct()
    context = {
        'banners': banners,
        'categories': categories,
        'sub_categories': sub_categories,
        'groups': groups,
        'products': products,
        'manage_products': manage_products,
        'manage_product_form': manage_product_form,
        'group_id': group_id,
        'conversations': conversations,
    }
    return render(request, 'edit_pages/manage_product.html', context)



# ........................Delete......................................
@login_required
def delete_banner(request, pk):
    delete_banner = get_object_or_404(Banner, pk=pk, created_by=request.user)
    if request.method == 'POST':
        if 'delete_banner' in request.POST:
            delete_banner.delete()
            return redirect('sell_on_daraz:new_banner')
    return redirect('sell_on_daraz:new_banner')

@login_required
def delete_category(request, pk):
    delete_category = get_object_or_404(Category, pk=pk, created_by=request.user)
    if request.method == 'POST':
        if 'delete_category' in request.POST:
            delete_category.delete()
            return redirect('sell_on_daraz:new_category')
    return redirect('sell_on_daraz:new_category')

@login_required
def delete_sub_category(request, pk):
    delete_sub_category = get_object_or_404(SubCategory, pk=pk, created_by=request.user)
    if request.method == 'POST':
        if 'delete_sub_category' in request.POST:
            delete_sub_category.delete()
            return redirect('sell_on_daraz:new_sub_category')
    return redirect('sell_on_daraz:new_sub_category')

@login_required
def delete_group(request, pk):
    delete_group = get_object_or_404(Group, pk=pk, created_by=request.user)
    if request.method == 'POST':
        if 'delete_group' in request.POST:
            delete_group.delete()
            return redirect('sell_on_daraz:new_groups')
    return redirect('sell_on_daraz:new_groups')

@login_required
def delete_brand(request, pk, id1, id2):
    delete_brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        if 'delete_brand' in request.POST:
            delete_brand.delete()
            return redirect('sell_on_daraz:new_brand', id1, id2)
    return redirect('sell_on_daraz:new_brand', id1, id2)

@login_required
def delete_material(request, pk, id1, id2):
    delete_material = get_object_or_404(MainMaterial, pk=pk)
    if request.method == 'POST':
        if 'delete_material' in request.POST:
            delete_material.delete()
            return redirect('sell_on_daraz:new_material', id1, id2)
    return redirect('sell_on_daraz:new_material', id1, id2)

@login_required
def delete_warranty_period(request, pk, id1, id2):
    delete_warranty_period = get_object_or_404(WarrantyPeriod, pk=pk)
    if request.method == 'POST':
        if 'delete_warranty_period' in request.POST:
            delete_warranty_period.delete()
            return redirect('sell_on_daraz:new_warranty_period', id1, id2)
    return redirect('sell_on_daraz:new_warranty_period', id1, id2)

@login_required
def delete_listed_year_season(request, pk, id1, id2):
    delete_listed_year_season = get_object_or_404(ListedYearSeason, pk=pk)
    if request.method == 'POST':
        if 'delete_listed_year_season' in request.POST:
            delete_listed_year_season.delete()
            return redirect('sell_on_daraz:new_listed_year_season', id1, id2)
    return redirect('sell_on_daraz:new_listed_year_season', id1, id2)

@login_required
def delete_mens_trend(request, pk, id1, id2):
    delete_mens_trend = get_object_or_404(MensTrend, pk=pk)
    if request.method == 'POST':
        if 'delete_mens_trend' in request.POST:
            delete_mens_trend.delete()
            return redirect('sell_on_daraz:new_mens_trend', id1, id2)
    return redirect('sell_on_daraz:new_mens_trend', id1, id2)



@login_required
def delete_product(request, pk):
    delete_product = get_object_or_404(Product, pk=pk, created_by=request.user)
    if request.method == 'POST':
        if 'delete_product' in request.POST:
            delete_product.delete()
            return redirect('sell_on_daraz:for_sale')
    return redirect('sell_on_daraz:for_sale')