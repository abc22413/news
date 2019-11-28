from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
#3rd party
from profanity.validators import validate_is_profane

class Article(models.Model):
    title = models.CharField(max_length=255, validators=[validate_is_profane])
    body = models.TextField(validators=[validate_is_profane])
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140, validators=[validate_is_profane])
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
