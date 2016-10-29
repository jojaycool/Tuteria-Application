from django import template

from preferences import preferences

register = template.Library()


@register.inclusion_tag('inclusion_tags/share.html')
def share():

    try:
        social_media = preferences.SitePreferences.active_social_media
    except:
        social_media = None

    return {'social_media': social_media}


@register.inclusion_tag('inclusion_tags/footer_share.html')
def footer_share():

    try:
        social_media = preferences.SitePreferences.active_social_media
    except:
        social_media = None

    return {'social_media': social_media}
