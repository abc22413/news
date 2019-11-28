from django.urls import *
from .views import *

urlpatterns = [
    path('<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit')
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('', ArticleListView.as_view(), name='article_list'),
]
