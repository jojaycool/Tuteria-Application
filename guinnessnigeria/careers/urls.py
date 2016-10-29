from django.conf.urls import patterns, include, url  # noqa

from guinnessnigeria.careers import views

urlpatterns = patterns(
    '',
    url(r'^vacancies/$',
        views.VacancyList.as_view(template_name='careers/vacancies/vacancy_list.html',
                                  paginate_by=10),
        name='careers_vacancies'),
)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^why-guinness-nigeria/$',
        'flatpage',
        {'url': '/careers/why-guinness-nigeria/'},
        name='careers_why_guinness_nigeria'),

    url(r'^working-with-guinness-nigeria/$',
        'flatpage',
        {'url': '/careers/working-with-guinness-nigeria/'},
        name='careers_working_with_guinness_nigeria'),

    url(r'^how-to-apply/$', 'flatpage', {'url': '/careers/how-to-apply/'},
        name='careers_how_to_apply'),
)
