from django import template
register = template.Library()

@register.filter(name='phone_number')
def phone_number(number):
    number = str(number)
    """Convert a 10 character string into (xxx) xxx-xxxx ext. xxxxxx"""
    first = number[0:3]
    second = number[3:6]
    third = number[6:10]
    extension = number[10:]
    return '(' + first + ')' + ' ' + second + '-' + third + ' ext. ' + extension

@register.filter(name='meters_to_miles')
def meters_to_miles(meters):
    meters = str(number)
    """Convert a 10 character string into (xxx) xxx-xxxx ext. xxxxxx"""
    miles = meters * 0.00062137
    return miles