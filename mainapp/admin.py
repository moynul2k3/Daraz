from django.contrib import admin
from . models import Category, SubCategory, Group, Banner

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Group)
admin.site.register(Banner)