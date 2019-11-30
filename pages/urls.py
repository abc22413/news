from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
#handler404 = 'pages.views.handler404'
#handler500 = 'pages.views.handler500'
