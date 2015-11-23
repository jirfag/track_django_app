from django.core.management.base import BaseCommand
from qa.models import Question, Answer
from lib.models import Liker, Tag
import random

#fgrep -lr "def " . | xargs -P8 -n1 cat | perl -lne '/^def (\w+)\(/ && print $1' >/tmp/all_django_funcs.txt

with open('/tmp/all_django_funcs.txt', 'r') as f:
    all_django_funcs = f.read().splitlines()

question_text_templates = (
    'What is "{}" for?',
    'How to use "{}"?',
    'Is it error in "{}"?',
    'Why Django has function "{}"?',
    'Does RoR have analog of Django`s "{}"?',
    'Where to find definition of "{}"?',
    'Can you explain me Django function "{}"?',
)

answer_templates = (
    'Just open source code to see what "{}" does',
    'Function "{}" does nothing',
    'The function "{}" is deprecated, dont use it"',
    'There is some error in function "{}"',
    'What version of Django do you use?',
)

question_long_templates = (
    'I have googled it, searched through source code, but I cant find. Help me plz!',
    'Thanks for your responses',
    'Also I`d like to know what I need to read to easily understand all Django function. Give me an advice please.',
)

def create_question(idx):
    func_name = random.choice(all_django_funcs)
    question_title = 'Django function "{}"'.format(func_name)
    question_text = random.choice(question_text_templates).format(func_name) + ' ' + random.choice(question_long_templates)
    q = Question.objects.create(title=question_title, text=question_text)
    for _ in range(random.randint(0, 3)):
        Liker.objects.create(content_object=q, is_like=random.choice((True, True, False)))

    for _ in range(random.randint(0, 10)):
        answer_text = random.choice(answer_templates).format(func_name)
        a = Answer.objects.create(text=answer_text, question=q)
        for _ in range(random.randint(0, 3)):
            Liker.objects.create(content_object=a, is_like=random.choice((True, True, False)))
    print('#{}: created {!r}'.format(idx, q))

class Command(BaseCommand):
    def handle(self, *args, **options):
        Question.objects.all().delete()
        Answer.objects.all().delete()
        Liker.objects.all().delete()
        Tag.objects.all().delete()
        for i in range(10000):
            create_question(i)
