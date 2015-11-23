from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericRelation
from lib.models import Tag, Liker

def _likes_rating(self):
    r = 0
    for like in self.likes.all():
        r += (1 if like.is_like else 0)
    return r

class Question(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    likes = GenericRelation(Liker)

    likes_rating = _likes_rating

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('qa:q-detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    likes = GenericRelation(Liker)

    likes_rating = _likes_rating

    def __str__(self):
        return self.text
