from django.conf.urls import patterns, include, url  # noqa

from guinnessnigeria.about import views


urlpatterns = patterns(
    'django.contrib.flatpages.views',
    # About Pages

    url(r'^overview/$', 'flatpage', {'url': '/about/overview/'},
        name='about_overview'),

    url(r'^our-values/$', 'flatpage', {'url': '/about/our-values/'},
        name='about_our_values'),

    url(r'^our-strategy/$', 'flatpage', {'url': '/about/our-strategy/'},
        name='about_our_strategy'),

    url(r'^management/$', 'flatpage', {'url': '/about/management/'},
        name='about_management'),

    url(r'^history-moments/$', 'flatpage', {'url': '/about/history-moments/'},
        name='about_history_moments'),

    url(r'^awards/$', 'flatpage', {'url': '/about/awards/'},
        name='about_awards'),

    url(r'^compliance-and-ethics/$', 'flatpage', {'url': '/about/compliance-and-ethics/'},
        name='about_compliance_and_ethics'),

    url(r'^faqs/$', 'flatpage', {'url': '/about/faqs/'},
        name='about_faqs'),

    url(r'^country-information/$', 'flatpage', {'url': '/about/country-information/'},
        name='about_country_information'),

    url(r'^safety-and-quality/$', 'flatpage', {'url': '/about/safety-and-quality/'},
        name='about_safety_and_quality'),

    url(r'^responsible-drinking/$', 'flatpage', {'url': '/about/responsible-drinking/'},
        name='about_responsible_drinking'),
)

urlpatterns += patterns(
    '',
    url(r'^board-of-directors/$',
        views.BoardOfDirectorsList.as_view(
            template_name='about/board_of_directors_list.html'),
        name='about_board_of_directors'),

    url(r'^board-of-directors/detail/(?P<slug>[\w-]+)/$',
        views.BoardOfDirectorsDetail.as_view(
            template_name='about/board_of_directors_detail.html',),
        name='about_board_of_directors_detail'),

    url(r'^executives/$',
        views.ExecutiveList.as_view(template_name='about/executive_list.html'),
        name='about_executives'),

    url(r'^executives/detail/(?P<slug>[\w-]+)/$',
        views.ExecutiveDetail.as_view(template_name='about/executive_detail.html',),
        name='about_executives_detail'),
)
