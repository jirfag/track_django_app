from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericRelation
from lib.models import Tag, Liker
from django.dispatch import receiver

def _likes_rating(self):
    return self.likes_n
    r = 0
    for like in self.likes.all():
        r += (1 if like.is_like else -1)
    return r

class Question(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    likes = GenericRelation(Liker)
    likes_n = models.IntegerField(null=True)

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
    likes_n = models.IntegerField()

    likes_rating = _likes_rating

    def __str__(self):
        return self.text

@receiver(models.signals.post_save, sender=Answer)
def on_answer_creation(sender, instance, *args, **kwargs):
    if kwargs.get('created'):
        answer = instance
        from .tasks import send_email_notification
        send_email_notification.delay(
            'd.isaev@corp.mail.ru',
            'New answer to question "{}"'.format(answer.question.title),
            'You got answer with the text: "{}"'.format(answer.text)
        )
