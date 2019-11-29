from django import template

register = template.Library()

def sumup(a):
    if(len(a)>140):
        return a[:137]+'...'
    else:
        return a

def cutup(x):
    if len(x)>3:
        return x[:3]
    else:
        if len(x)>0:
            return x

register.filter('sumup',sumup)
register.filter('cutup',cutup)
