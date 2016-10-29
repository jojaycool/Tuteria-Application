import datetime

from django.views import generic as generic_views
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound  # noqa
from django.shortcuts import get_object_or_404  # noqa
from django.conf import settings  # noqa
from django.contrib.sites.models import get_current_site  # noqa
from django.contrib.auth.models import Group  # noqa
from django.contrib.auth.decorators import login_required  # noqa
from django.shortcuts import render_to_response  # noqa
from django.template import RequestContext  # noqa
from django.utils.encoding import smart_str  # noqa

from unobase import utils as unobase_utils  # noqa
from unobase import mixins as unobase_mixins  # noqa
from unobase import models as unobase_models  # noqa
from unobase import constants as unobase_constants  # noqa
from unobase.age_gate.views import AgeGate as BaseAgeGate

from guinnessnigeria import automatic_emails
from guinnessnigeria import forms, models  # noqa
from guinnessnigeria.brands import models as brand_models
from guinnessnigeria.investors import models as investor_models
from guinnessnigeria.news_and_media import models as news_and_media_models

from preferences import preferences


class Index(generic_views.TemplateView):

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['banners'] = models.FrontPageBanner.permitted.all()
        context['press_releases'] = news_and_media_models.PressRelease.permitted.all()[:2]
        context['brands'] = [brand_category_through.brand for brand_category_through in
            brand_models.BrandCategoryThrough.objects.filter(brand_category__slug='carousel')]  # noqa
        # context['stock_ticker'] = preferences.SitePreferences.active_stock_ticker
        context['stock_reports'] = investor_models.FinancialReport.objects.all()[:5]
        return context


class ContactUs(generic_views.FormView):

    def form_valid(self, form):
        self.send_email(form)
        messages.success(self.request, 'Contact message sent.')

        form = forms.ContactUsForm()
        return self.render_to_response(self.get_context_data(form=form))

    def send_email(self, form):
        automatic_emails.email_contact_message(
            form.cleaned_data['email'],
            form.cleaned_data['name'],
            form.cleaned_data['contact_number'],
            form.cleaned_data['subject'],
            form.cleaned_data['message']
        )


class AgeGate(BaseAgeGate):
    """Fix unobase bugs"""

    def form_valid(self, form):
        self.request.session['user_date_of_birth'] = datetime.datetime(int(form.cleaned_data['birth_year']), 
                                                                       int(form.cleaned_data['birth_month']), 
                                                                       int(form.cleaned_data['birth_day']))
        age = settings.COUNTRY_LEGAL_AGES.get(form.cleaned_data['location'], 18)
        self.request.session['country_date_of_birth_required'] = datetime.datetime.now() - datetime.timedelta(days=age*365)
        return HttpResponseRedirect(self.get_success_url())
