from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.ColorFamily)
admin.site.register(models.SizeName)
admin.site.register(models.Size)
admin.site.register(models.Location)
admin.site.register(models.MainMaterial)
admin.site.register(models.WarrantyType)
admin.site.register(models.WarrantyPeriod)
admin.site.register(models.ListedYearSeason)
admin.site.register(models.MensTrend)
admin.site.register(models.Product)
admin.site.register(models.Rating)