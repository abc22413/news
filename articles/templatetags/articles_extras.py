from django import template

register = template.Library()

def sumup(a):
    if(len(a)>140):
        return a[:137]+'...'
    else:
        return a

register.filter('sumup',sumup)
