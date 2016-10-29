'''
Created on 22 Mar 2013

@author: michael
'''
from django.contrib import admin

from guinnessnigeria.brands import models


class BrandCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class BrandCategoryInline(admin.TabularInline):
    model = models.BrandCategoryThrough


class BrandAdmin(admin.ModelAdmin):
    inlines = [
        BrandCategoryInline,
    ]

    list_display = ("title", "order_list",)

    def order_list(self, model):
        return ', '.join(['%s: %s' % (brand_category_through.brand_category.name, brand_category_through.order) for brand_category_through in models.BrandCategoryThrough.objects.filter(brand=model)])  # noqa

admin.site.register(models.BrandCategory, BrandCategoryAdmin)
admin.site.register(models.Brand, BrandAdmin)
