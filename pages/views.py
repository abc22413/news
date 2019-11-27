from django.views.generic import *

class HomePageView(TemplateView):
    template_name = 'home.html'
