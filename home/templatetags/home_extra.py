from django import template
from home.info import *

register = template.Library()


@register.inclusion_tag('home/app_list.html')
def get_app_list(user_details):
    apps = []
    for app in CIS_APPS:
        if app.info.accessible_from(user_details):
            apps.append(app.info.get_app_info())
    context = {'apps': apps}
    return context
