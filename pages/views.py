from django.views.generic import *

class HomePageView(TemplateView):
    template_name = 'home.html'


#FOR SENTRY ERROR REPORTING
from sentry_sdk import last_event_id
from django.shortcuts import render

def handler500(request, *args, **argv):
    return render(request, "500.html", {
        'sentry_event_id': last_event_id(),
    }, status=500)
