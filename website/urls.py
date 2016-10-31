from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url  # noqa
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('guinnessnigeria.urls')),
    (r'^pages/', include('django.contrib.flatpages.urls')),
    (r'^secure/ckeditor/', include('ckeditor.urls')),
    (r'^comments/', include('unobase.commenting.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

