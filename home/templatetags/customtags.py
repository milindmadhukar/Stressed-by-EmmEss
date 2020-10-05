from django import template

register = template.Library()

@register.filter()
def accessItem(value,index):
    return value[index]

@register.filter()
def linkCorrector(value):
    value = str(value)
    return "https://github.com/milindmadhukar/Stressed-by-EmmEss/blob/master/media/home/images/" + value[12:]
 
