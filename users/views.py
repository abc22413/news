from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
