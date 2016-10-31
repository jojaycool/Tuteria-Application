from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django import forms

from preferences.admin import PreferencesAdmin

from ckeditor.widgets import CKEditorWidget

from guinnessnigeria import models


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm

try:
    admin.site.unregister(FlatPage)
except:
    pass


class FrontPageBannerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('image', 'state', 'description', 'url', 'order')
        }),
    )

    list_display = [
        'order',
        'image',
        'url',
        'state',
    ]

admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(models.SitePreferences, PreferencesAdmin)
admin.site.register(models.FrontPageBanner, FrontPageBannerAdmin)
admin.site.register(models.SocialMedia)


# # Unregister irrelevant models

# from photologue import models as photologue_models  # noqa

# admin.site.unregister(photologue_models.Gallery)
# admin.site.unregister(photologue_models.GalleryUpload)
# admin.site.unregister(photologue_models.PhotoEffect)
# admin.site.unregister(photologue_models.Photo)
# admin.site.unregister(photologue_models.Watermark)

# # from django_evolution import models as evolution_models

# # admin.site.unregister(evolution_models.Evolution)
# # admin.site.unregister(evolution_models.Version)

# from unobase import models as unobase_models  # noqa

# admin.site.unregister(unobase_models.DefaultImage)
# admin.site.unregister(unobase_models.TagModel)

# from unobase.tagging import models as tagging_models  # noqa

# admin.site.unregister(tagging_models.Tag)
