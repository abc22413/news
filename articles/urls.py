from django.urls import *
from django.conf.urls import *
from .views import *

urlpatterns = [
    path('<int:pk>/edit/',
    ArticleUpdateView.as_view(), name='article_edit'), # new

    path('<int:pk>/',
    ArticleDetailView.as_view(), name='article_detail'), # new

    path('<int:pk>/delete/',
    ArticleDeleteView.as_view(), name='article_delete'), # new

    path('new/', ArticleCreateView.as_view(), name='article_new'),

    path('', ArticleListView.as_view(), name='article_list'),
]


handler500 = 'articles.views.handler500'
