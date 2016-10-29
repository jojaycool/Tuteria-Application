'''
Created on 22 Mar 2013

@author: michael
'''
from django.contrib import admin

from guinnessnigeria.investors import models


class ShareSummaryAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'shares',
        'average_purchase_price',
    ]


admin.site.register(models.StockTicker)
admin.site.register(models.FinancialReport)
admin.site.register(models.FinancialResult)
admin.site.register(models.ShareSummary, ShareSummaryAdmin)
admin.site.register(models.ShareDownload)
