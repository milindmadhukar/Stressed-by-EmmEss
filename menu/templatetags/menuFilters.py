from django import template

register = template.Library()

@register.filter()
def removespaceandspChar(value):
    tmp = ""
    for char in value:
        if char.isalnum():
            tmp = tmp + char

    return tmp.lower()
