from django import template

register = template.Library()

@register.filter()
def accessItem(value,index):
    return value[index]
 