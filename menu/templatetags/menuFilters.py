from django import template
from math import ceil

register = template.Library()

@register.filter()
def categoryFormat(value,index):
    value = value[index]
    tmp = ""
    for char in value:
        if char.isalnum():
            tmp = tmp + char

    print(tmp.lower())
    return tmp.lower()


@register.filter()
def getRange(value):
    n = len(value)
    nSlides = n//2 + ceil((n/2)-(n//2))
    return range(1,nSlides+1)

@register.filter()
def getNoOfSlides(value):
    n = len(value)
    nSlides = n//2 + ceil((n/2)-(n//2))
    return nSlides

@register.filter()
def isOdd(value):
    if len(value) % 2 == 1:
        return True
    else:
        return False

@register.filter()
def getOddItem(value,index):
    return value[(2*index) - 2]

@register.filter()
def getEvenItem(value,index):
    return value[(2*index) - 1]

@register.filter()
def getValue(value, valueName):
    return value.get(valueName)

@register.filter()
def getSrc(value):
    word = value.split(' ')[1]
    word = word[5:len(word)-1]
    return word




