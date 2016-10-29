from django.conf.urls import patterns, include, url  # noqa

from guinnessnigeria.news_and_media import views

urlpatterns = patterns(
    '',
    url(r'^press-releases/$',
        views.PressReleaseList.as_view(
            template_name='news_and_media/press_releases/press_release_list.html',
            paginate_by=10
        ),
        name='news_and_media_press_releases'),

    url(r'^press-releases/detail/(?P<pk>\d+)/$',
        views.PressReleaseDetail.as_view(
            template_name='news_and_media/press_releases/press_release_detail.html'),
        name='news_and_media_press_releases_detail'),

    url(r'^publications/$',
        views.PublicationList.as_view(
            template_name='news_and_media/publications/publication_list.html',
            paginate_by=10
        ),
        name='news_and_media_publications'),
)

urlpatterns += patterns(
    'django.contrib.flatpages.views',
    url(r'^overview/$', 'flatpage', {'url': '/news-and-media/overview/'},
        name='news_and_media_overview'),

    url(r'^news/$', 'flatpage', {'url': '/news-and-media/news/'},
        name='news_and_media_news'),

    url(r'^media-contact/$', 'flatpage', {'url': '/news-and-media/media-contact/'},
        name='news_and_media_media_contact'),

    url(r'^media-enquiries/$', 'flatpage', {'url': '/news-and-media/media-enquiries/'},
        name='news_and_media_media_enquiries'),
)
