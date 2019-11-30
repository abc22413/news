from django import template
from decouple import config, Csv

register = template.Library()

def getdsn():
    return config('dsn')

register.filter('getdsn',getdsn)
