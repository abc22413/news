from django.views.generic import *
from .models import *

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'all_articles_list'
