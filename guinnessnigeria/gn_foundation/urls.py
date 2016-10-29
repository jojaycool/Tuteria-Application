from django.conf.urls import patterns, include, url  # noqa

urlpatterns = patterns(
    'django.contrib.flatpages.views',
    url(r'^overview/$', 'flatpage', {'url': '/gn-foundation/overview/'},
        name='gn_foundation_overview'),

    url(r'^education/$', 'flatpage', {'url': '/gn-foundation/education/'},
        name='gn_foundation_education'),

    url(r'^health/$', 'flatpage', {'url': '/gn-foundation/health/'},
        name='gn_foundation_health'),

    url(r'^skills-for-life/$', 'flatpage', {'url': '/gn-foundation/skills-for-life/'},
        name='gn_foundation_skills_for_life'),

    url(r'^sports/$', 'flatpage', {'url': '/gn-foundation/sports/'},
        name='gn_foundation_sports'),

    url(r'^water-of-life/$', 'flatpage', {'url': '/gn-foundation/water-of-life/'},
        name='gn_foundation_water_of_life'),

    # url(r'^responsible-drinking/$',
    #     'flatpage',
    #     {'url': '/gn-foundation/responsible-drinking/'},
    #     name='gn_foundation_responsible_drinking'),

    url(r'^programmes-and-initiatives/$',
        'flatpage',
        {'url': '/gn-foundation/programmes-and-initiatives/'},
        name='gn_foundation_programmes_and_initiatives'),

    # url(r'^safety-and-quality/$',
    #     'flatpage',
    #     {'url': '/gn-foundation/safety-and-quality/'},
    #     name='gn_foundation_safety_and_quality'),

    # url(r'^compliance-and-ethics/$',
    #     'flatpage',
    #     {'url': '/gn-foundation/compliance-and-ethics/'},
    #     name='gn_foundation_compliance_and_ethics'),
    )
