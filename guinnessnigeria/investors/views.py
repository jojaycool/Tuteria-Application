'''
Created on 22 Mar 2013

@author: michael
'''
from django.views import generic as generic_views

from guinnessnigeria.investors import models


class FinancialReportList(generic_views.ListView):

    def get_queryset(self):
        return models.FinancialReport.objects.all()


class FinancialResultList(generic_views.ListView):

    def get_queryset(self):
        return models.FinancialResult.objects.all()


class ShareSummaryList(generic_views.ListView):

    def get_queryset(self):
        return models.ShareSummary.objects.all().order_by('date')

    def get_context_data(self, **kwargs):
        context = super(ShareSummaryList, self).get_context_data(**kwargs)

        context['downloads'] = models.ShareDownload.objects.all()
        return context
