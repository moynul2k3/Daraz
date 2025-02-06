from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from mainapp.models import Group, SubCategory, Category

# Create your models here.
class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    # created_by = models.ForeignKey(User, related_name="brand", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Brand'
        ordering = ['-created_at']
    def __str__(self):
        return self.name
    
class ColorFamily(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    color = ColorField(default='#01acff')
    # created_by = models.ForeignKey(User, related_name="colorfamily", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'ColorFamily'
        ordering = ['-created_at']
    def __str__(self):
        return self.name
    
class SizeName(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    # created_by = models.ForeignKey(User, related_name="size_name", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'SizeName'
        ordering = ['-created_at']
    def __str__(self):
        return self.name
    
class Size(models.Model):
    size_type = models.ForeignKey(SizeName, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    # created_by = models.ForeignKey(User, related_name="size", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Size'
        ordering = ['-created_at']
    def __str__(self):
        return self.name

class Location(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    country_name = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, related_name="location", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Country Name'
        ordering = ['-created_at']
    def __str__(self):
        return self.country_name
    
class MainMaterial(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, related_name="main_material", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Main Material'
        ordering = ['-created_at']
    def __str__(self):
        return self.name
    
class WarrantyType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, related_name="warranty_type", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Warranty Type'
        ordering = ['-created_at']
    def __str__(self):
        return self.name
    
class WarrantyPeriod(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, related_name="warranty_period", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Warranty Period'
        ordering = ['-created_at']
    def __str__(self):
        return self.name
    
class ListedYearSeason(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, related_name="listed_year_season", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Listed Year Season'
        ordering = ['-created_at']
    def __str__(self):
        return self.name
    
class MensTrend(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, related_name="mens_trend", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Men's Trend"
        ordering = ['-created_at']
    def __str__(self):
        return self.name
    
# group, name, description, price, discount, color_family, image, brand, sku, flash_sale, is_sold
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    color_family = models.ForeignKey(ColorFamily, on_delete=models.SET_NULL, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    main_material = models.ForeignKey(MainMaterial, on_delete=models.SET_NULL, blank=True, null=True)
    warranty_type = models.ForeignKey(WarrantyType, on_delete=models.SET_NULL, blank=True, null=True)
    warranty_period = models.ForeignKey(WarrantyPeriod, on_delete=models.SET_NULL, blank=True, null=True)
    listed_year_season = models.ForeignKey(ListedYearSeason, on_delete=models.SET_NULL, blank=True, null=True)
    mens_trend = models.ForeignKey(MensTrend, on_delete=models.SET_NULL, blank=True, null=True)
    
    flash_sale = models.BooleanField(default=False, verbose_name = 'Add To FlashSale', null = True)
    wholesale_price = models.BooleanField(default=False, verbose_name = 'Wholesale Price', null = True)
    everyday_low_price = models.BooleanField(default=False, verbose_name = 'Everyday Low Price!', null = True)
    free_delivery = models.BooleanField(default=False, verbose_name = 'Free Delivery', null = True)
    fashion = models.BooleanField(default=False, verbose_name = 'Fashion', null = True)
    beauty_glamour = models.BooleanField(default=False, verbose_name = 'Beauty & Glamour', null = True)
    mart = models.BooleanField(default=False, verbose_name = 'Mart', null = True)
    home_makeover = models.BooleanField(default=False, verbose_name = 'Home Makeover', null = True)
    best_price_guaranteed = models.BooleanField(default=False, verbose_name = 'Best Price Guaranteed', null = True)
    
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=2,  decimal_places=0)
    discount_price = models.IntegerField(default=0 ,blank=True, null=True)
    sell_price = models.IntegerField(blank = True, null=True)
    image = models.ImageField(upload_to='products/product_images')
    sku = models.CharField(max_length=400, verbose_name = 'SKU')
    is_sold = models.BooleanField(default=False, verbose_name = 'Out Of Stock')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']
    
    @property
    def discount_price(self):
        return int(((self.price)*(self.discount))/100)

    @property
    def sell_price(self):
        return (self.price)-(self.discount_price)
    
    def __str__(self):
        return self.name

class Rating(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, null=True, blank=True)
    
    def __int__(self):
        return self.rating
    
