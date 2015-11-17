from django.core.management.base import BaseCommand
from qa.models import Question, Answer

def create_question(idx):
    q = Question.objects.create(title='q{}'.format(idx), text='text of question #{}'.format(idx))
    for i in range(10):
        a = Answer.objects.create(text='a{}.{} text'.format(idx, i))
        q.answers.add(a)
    q.save()
    print('#{}: created {!r}'.format(idx, q))

class Command(BaseCommand):
    def handle(self, *args, **options):
        Question.objects.all().delete()
        Answer.objects.all().delete()
        for i in range(128):
            create_question(i)
