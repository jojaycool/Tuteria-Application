from django.conf.urls import patterns, include, url
from django.conf import settings  # noqa
from django.views import generic as generic_views

from unobase.questionnaire import views as competition_views
from unobase.questionnaire import forms as competition_forms  # noqa
from unobase.questionnaire import models as competition_models

from guinnessnigeria import forms, views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.Index.as_view(template_name='guinnessnigeria/index.html'),
        name='index'),

    url(r'^contact-us/$',
        views.ContactUs.as_view(form_class=forms.ContactUsForm,
                                template_name='guinnessnigeria/contact_us.html'),
        name='contact_us'),

    (r'^about/', include('guinnessnigeria.about.urls')),
    (r'^brands/', include('guinnessnigeria.brands.urls')),
    (r'^careers/', include('guinnessnigeria.careers.urls')),
    (r'^investors/', include('guinnessnigeria.investors.urls')),
    (r'^news-and-media/', include('guinnessnigeria.news_and_media.urls')),
    (r'^gn-foundation/', include('guinnessnigeria.gn_foundation.urls')),
    (r'^poll/', include('unobase.poll.urls')),

    url(r'^competitions/(?P<slug>[\w-]+)/thanks/$',
        generic_views.DetailView.as_view(
            model=competition_models.Questionnaire,
            template_name='questionnaire/questionnaire_thanks.html'
        ),
        name='questionnaire_thanks'),

    url(r'^competitions/(?P<slug>[\w-]+)/already_completed/$',
        generic_views.DetailView.as_view(
            model=competition_models.Questionnaire,
            template_name='questionnaire/questionnaire_already_completed.html'
        ),
        name='questionnaire_already_completed'),

    url(r'^competitions/(?P<slug>[\w-]+)/rules/$',
        generic_views.DetailView.as_view(
            model=competition_models.Questionnaire,
            template_name='questionnaire/questionnaire_rules.html'
        ),
        name='questionnaire_rules'),

    url(r'^competitions/(?P<slug>[\w-]+)/$',
        competition_views.Questionnaire.as_view(
            form_class=forms.CustomQuestionnaire,
            template_name='questionnaire/questionnaire_form.html',
            success_url='thanks/'
        ),
        name='questionnaire_form'),

    # Add more countries to age gateway by using a custom form
    url(r'^age_gate/$',
        views.AgeGate.as_view(form_class=forms.AgeGateForm,
                              template_name='age_gate/age_gate_form.html'),
        name='age_gate'),

)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^accessibility/$', 'flatpage', {'url': '/accessibility/'},
        name='accessibility'),

    url(r'^privacy-policy/$', 'flatpage', {'url': '/privacy-policy/'},
        name='privacy_policy'),

    url(r'^terms-and-conditions/$', 'flatpage', {'url': '/terms-and-conditions/'},
        name='terms_and_conditions'),
)
