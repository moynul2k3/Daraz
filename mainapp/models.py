# models.py
from django.db import models
from django.contrib.auth.models import User


class Banner(models.Model):
    name = models.CharField(max_length=255) 
    image = models.ImageField(upload_to='banner')
    created_by = models.ForeignKey(User, related_name="banner", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Banners'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name="category", on_delete = models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name="sub_category", on_delete = models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Sub Categories'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class Group(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/group')
    created_by = models.ForeignKey(User, related_name="group", on_delete = models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Groups'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name
    

    
