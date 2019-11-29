from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


#FOR SENTRY ERROR REPORTING
from sentry_sdk import last_event_id
from django.shortcuts import render

def handler500(request, *args, **argv):
    return render(request, "500.html", {
        'sentry_event_id': last_event_id(),
    }, status=500)
