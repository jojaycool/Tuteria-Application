'''
Created on 27 Mar 2013

@author: michael
'''
from django.views import generic as generic_views
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404  # noqa

from guinnessnigeria.brands import models

from unobase import mixins as unobase_mixins


class BrandList(unobase_mixins.AgeGateMixin, generic_views.ListView):

    age_gate_url = '/age_gate'

    def get_context_data(self, **kwargs):
        context = super(BrandList, self).get_context_data(**kwargs)
        context['brand_categories'] = models.BrandCategory.objects.filter(
            ~Q(slug__exact='carousel'))

        slug = self.kwargs['slug']

        # if slug == 'all':
        #    brand_category_name = 'All'
        # else:
        try:
            brand_category_name = models.BrandCategory.objects.get(slug=slug).name
        except models.BrandCategory.DoesNotExist:
            brand_category_name = ''

        context['brand_category_name'] = brand_category_name
        context['slug'] = slug
        return context

    def get_queryset(self):
        slug = self.kwargs['slug']

        # if slug == 'all':
        #    return models.Brand.permitted.all()

        return [brand_category_through.brand for brand_category_through in
                models.BrandCategoryThrough.objects.filter(brand_category__slug=slug)]


class BrandDetail(unobase_mixins.AgeGateMixin, generic_views.DetailView):

    age_gate_url = '/age_gate'

    def get_context_data(self, **kwargs):
        context = super(BrandDetail, self).get_context_data(**kwargs)
        context['brand_categories'] = models.BrandCategory.objects.filter(
            ~Q(slug__exact='carousel'))

        context['brand_category_name'] = self.object.get_first_category().name if self.object is not None else 'All'  # noqa
        context['slug'] = self.object.get_first_category().slug if self.object is not None else 'all'  # noqa

        return context

    def get_object(self):
        try:
            return models.Brand.permitted.get(slug=self.kwargs['slug'])
        except models.Brand.DoesNotExist:
            raise Http404('No Brand matches the given query.')
