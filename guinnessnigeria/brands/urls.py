from django.conf.urls import patterns, include, url  # noqa

from guinnessnigeria.brands import views


urlpatterns = patterns(
    'django.contrib.flatpages.views',
    url(r'^how-we-make-our-brands/$',
        'flatpage',
        {'url': '/brands/how-we-make-our-brands/'},
        name='brands_how_we_make_our_brands'),

    url(r'^know-your-drink/$',
        'flatpage',
        {'url': '/brands/know-your-drink/'},
        name='brands_know_your_drink'),
)

urlpatterns += patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$',
        views.BrandList.as_view(template_name='brands/brand_list.html'),
        name='brand_list'),

    url(r'^detail/(?P<slug>[\w-]+)/$',
        views.BrandDetail.as_view(template_name='brands/brand_detail.html'),
        name='brand_detail'),
)
