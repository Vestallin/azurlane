from django import template

register = template.Library()

@register.filter
def color_filter(var):
    match var:
        case "Common":
            return 'common'
        case "Rare":
            return 'rare'
        case "Elite":
            return 'elite'
        case "Super Rare" | "Priority":
            return 'srare'
        case "Ultra Rare" | "Decisive":
            return 'urare'