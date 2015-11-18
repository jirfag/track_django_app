from django.db import models
from django.core.urlresolvers import reverse

class Answer(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Question(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('qa:q-detail', kwargs={'pk': self.pk})
