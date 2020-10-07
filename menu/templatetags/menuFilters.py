from django import template

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

