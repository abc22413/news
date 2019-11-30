from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
handler404 = 'pages.views.handler404'
handler500 = 'pages.views.handler500'
