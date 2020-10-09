from django import template

register = template.Library()

@register.filter()
def accessItem(value,index):
    return value[index]

@register.filter()
def getSrc(value):
    word = value.split(' ')[1]
    word = word[5:len(word)-1]
    return word
