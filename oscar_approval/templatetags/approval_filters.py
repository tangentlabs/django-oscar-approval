from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='user_from_profile')
def user_from_profile(profile, attribute):
    profile_user_related_name = settings.PROFILE_USER_RELATED_NAME
    user = getattr(profile, profile_user_related_name, None)
    return getattr(user, attribute, None)
