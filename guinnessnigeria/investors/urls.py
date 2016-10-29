from django.conf.urls import patterns, include, url  # noqa
from django.views.defaults import page_not_found

from guinnessnigeria.investors import views


urlpatterns = patterns(
    '',
    url(r'^financial-reports/$',
        views.FinancialReportList.as_view(
            template_name='investors/financial_reports/financial_report_list.html',
            paginate_by=10
        ),
        name='investors_financial_reports'),
    url(r'^financial-results/$',
        views.FinancialResultList.as_view(
            template_name='investors/financial_results/financial_result_list.html',
            paginate_by=10
        ),
        name='investors_financial_results'),
    url(r'^diageo-offer/$',
        #views.ShareSummaryList.as_view(
        #    template_name='investors/share_summary/share_summary_list.html',
        #    paginate_by=10
        #),
        page_not_found,
        name='investors_share_summary'),
)

# Flat pages
urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^overview/$', 'flatpage', {'url': '/investors/overview/'},
        name='investors_overview'),

    url(r'^corporate-governance/$',
        'flatpage',
        {'url': '/investors/corporate-governance/'},
        name='investors_corporate_governance'),

    url(r'^shareholders-services/$',
        'flatpage',
        {'url': '/investors/shareholders-services/'},
        name='investors_shareholders_services'),

    url(r'^investor-contacts/$',
        'flatpage',
        {'url': '/investors/investor-contacts/'},
        name='investors_investor_contacts'),

    url(r'^marketing-our-brands/$',
        'flatpage',
        {'url': '/investors/marketing-our-brands/'},
        name='investors_marketing_our_brands'),
)
