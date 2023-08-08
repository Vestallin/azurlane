from django import template

register = template.Library()

@register.filter
def link_filter(var):
    return var.replace('(Retrofit)', '').replace(' ', '_')